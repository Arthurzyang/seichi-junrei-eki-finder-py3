import requests
import json
import os
from src.logging_config import configureLogging

logger = configureLogging()
OUTPUT_DIR = "../Outputs"

def fetchNearestStations(targetLat, targetLon, radius):
    query = f'[out:json][timeout:60];(node["railway"="station"](around:{radius},{targetLat},{targetLon});node["station"="subway"](around:{radius},{targetLat},{targetLon}););out body;>;out skel qt;'
    url = "https://overpass-api.de/api/interpreter"

    try:
        response = requests.post(
            url,
            data=query.encode('utf-8'),
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"API 请求失败 (半径 {radius}m): {e}")
        return None

def fetchAnitabiLandmarks(subjectId):
    url = f"https://api.anitabi.cn/bangumi/{subjectId}/points/detail"
    params = {"haveImage": "false"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        filename = os.path.join(OUTPUT_DIR, f"{subjectId}_locates.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"地标信息已保存至: {filename}")
        return data
    except requests.RequestException as e:
        logger.error(f"获取地标数据失败: {e}")
        return None