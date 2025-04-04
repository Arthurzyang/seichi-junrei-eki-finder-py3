import json
import os
from collections import Counter
from src.utils import haversine
from src.api_client import fetchNearestStations
from src.logging_config import configureLogging

logger = configureLogging()
OUTPUT_DIR = "../Outputs"

def findNearestStation(targetLat, targetLon, initialRadius=1000):
    radius = initialRadius

    for _ in range(3):  # 尝试 1000m, 2000m, 4000m
        data = fetchNearestStations(targetLat, targetLon, radius)
        if not data:
            return None

        stations = []
        for element in data["elements"]:
            if element["type"] == "node":
                stationLat = element["lat"]
                stationLon = element["lon"]
                distance = haversine(targetLat, targetLon, stationLat, stationLon)
                stations.append({
                    "name": element.get("tags", {}).get("name", "Unknown"),
                    "lat": stationLat,
                    "lon": stationLon,
                    "distanceKm": distance
                })

        if stations:
            nearest = min(stations, key=lambda x: x["distanceKm"])
            logger.info(f"在 {radius}m 范围内找到最近站点: {nearest['name']} (距离: {nearest['distanceKm']:.3f} 千米)")
            return nearest

        logger.warning(f"在 ({targetLat}, {targetLon}) 周围 {radius}m 范围内未找到站点，已扩大搜索半径")
        radius *= 2

    logger.warning(f"在 ({targetLat}, {targetLon}) 周围 {radius}m 半径范围内仍未找到站点，已标记为 null")
    return None

def analyzeAnitabiStations(subjectId, initialRadius=1000):
    from src.api_client import fetchAnitabiLandmarks

    bangumiData = fetchAnitabiLandmarks(subjectId)
    if not bangumiData or not isinstance(bangumiData, list):
        logger.error("无法获取有效的地标数据")
        return

    title = f"作品_{subjectId}"
    logger.info(f"开始分析作品: {title} (ID: {subjectId})")

    stationDetails = []

    for point in bangumiData:
        pointId = point["id"]
        pointName = point.get("name", f"未命名地标 (ID: {pointId})")
        lat, lon = point["geo"]
        origin = point.get("origin", "未知来源")
        originUrl = point.get("originURL", "")

        logger.info(f"处理地标: {pointName} (ID: {pointId}, 来源: {origin})")

        station = findNearestStation(lat, lon, initialRadius)
        stationInfo = {
            "landmarkId": pointId,
            "landmarkName": pointName,
            "stationName": station["name"] if station else None,
            "stationLat": station["lat"] if station else None,
            "stationLon": station["lon"] if station else None,
            "distanceKm": station["distanceKm"] if station else None,
            "origin": origin,
            "originUrl": originUrl
        }
        stationDetails.append(stationInfo)

    stationsFile = os.path.join(OUTPUT_DIR, f"{subjectId}_stations.json")
    with open(stationsFile, 'w', encoding='utf-8') as f:
        json.dump(stationDetails, f, ensure_ascii=False, indent=2)
    logger.info(f"站点详细信息已保存至: {stationsFile}")

    stationNames = [detail["stationName"] for detail in stationDetails if detail["stationName"]]
    stationCounts = Counter(stationNames)

    countsFile = os.path.join(OUTPUT_DIR, f"{subjectId}_station_counts.txt")
    with open(countsFile, 'w', encoding='utf-8') as f:
        f.write(f"作品 '{title}' 地标总数: {len(bangumiData)}\n")
        f.write("最近站点统计结果:\n")
        for station, count in stationCounts.most_common():
            f.write(f"{station}: {count} 个地标\n")
    logger.info(f"站点统计结果已保存至: {countsFile}")

    logger.info(f"\n作品 '{title}' 地标总数: {len(bangumiData)}")
    logger.info("最近站点统计结果:")
    for station, count in stationCounts.most_common():
        logger.info(f"{station}: {count} 个地标")