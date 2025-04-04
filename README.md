# SeichiJunrei Eki Finder 圣地巡礼公共交通车站搜索器
这是一个 Python 脚本，根据Bangumi作品ID，通过Anitabi APIs获取对应动画的圣地巡礼地标信息，然后通过Overpass APIs搜索离每个地标直线距离最近的轨道交通（电车/地铁）站点，默认初始搜索半径为1公里，默认最大搜索半径为4公里。计算地标与站点的距离，并统计每个站点的地标数量。

## 功能

1. **获取地标数据**
   - 通过用户输入的Bangumi作品ID，从Anitabi APIs获取该作品的圣地巡礼地标详情。

2. **查找最近站点**
   - 使用 OpenStreetMap的Overpass API，根据地标的经纬度查找附近火车站或地铁站。
   - 逐步扩大搜索范围的策略（1000m->2000m->4000m）。

3. **距离计算**
   - 使用Haversine公式计算地标与站点之间的地理距离（km）。

4. **输出文件**
   - 将每个地标的最近站点信息保存到本地。
   - 统计每个站点关联的地标数量。
   - 日志文件

### 流程

1. 输入Bangumi作品ID。
2. 获取地标数据并保存。
3. 对每个地标查找最近站点，记录结果。
4. 保存详细站点信息和统计结果，同时输出到日志。

## APIs

1. **Anitabi API**
   - **参考**: [Anitabi APIs](https://github.com/anitabi/anitabi.cn-document/blob/main/api.md)
   - **参数**: `haveImage`（可选，`true` 筛选含图片的地标，默认 `false`）【此处疑似未生效】
   - **用途**: 根据Bangumi条目id，查询该动画的巡礼地标信息。Bangumi条目id可从该条目的URL获得。
   - **返回数据**: 地标列表，包含 `id`, `name`, `geo`, `origin`, `originURL` 等字段。
   - **协议**: 遵循 CC BY-NC-SA 4.0（署名、非商业性使用、相同方式共享）。

2. **Overpass API (OpenStreetMap)**
   - **参考**: [Overpass APIs](https://wiki.openstreetmap.org/wiki/Overpass_API)
   - **查询**: 使用 Overpass QL 搜索目标坐标附近的轨道交通(`railway=station`)、(`station=subway`)。
   - **用途**: 根据经纬度和设定半径查找最近的站点。
   - **返回数据**: JSON 格式的站点节点信息。

### API KEYS

无需配置，均为公共APIs

### 输出文件

- **`{subject_id}_locates.json`**: Anitabi APIs返回的地标数据。
- **`{subject_id}_stations.json`**: 地标信息与最近站点信息。
- **`{subject_id}_station_counts.txt`**: 站点统计，用于旅行计划。
- **`station_query.log`**: 日志。

### Tips
- Overpass API和Anitabi API可能会限制请求频率，请适度使用。
- 可通过修改initial_radius参数调整搜索范围。
