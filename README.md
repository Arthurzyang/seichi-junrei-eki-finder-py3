# SeichiJunrei Eki Finder 圣地巡礼公共交通车站搜索器 

# English

This is a Python script that retrieves landmark information for anime pilgrimage sites based on the Bangumi work ID through the Anitabi APIs. It then uses the Overpass APIs to search for the nearest railway (tram/subway) station to each landmark, with a default initial search radius of 1 kilometer and a maximum search radius of 4 kilometers. It calculates the distance between the landmark and the station and counts the number of landmarks associated with each station.

This is a Python script that uses the Bangumi work ID to retrieve pilgrimage landmark information from the Anitabi API, then uses the Overpass API to search for the nearest rail transportation (tram/subway) stations to each landmark within a default initial search radius of 1 km and a maximum search radius of 4 km. The script calculates the distance between landmarks and stations and counts the number of landmarks associated with each station.

## Features

1. **Get Landmark Data**
   - Fetch the pilgrimage landmark details for a work using the Bangumi work ID from the Anitabi API.

2. **Find Nearest Stations**
   - Use the Overpass API from OpenStreetMap to search for nearby train or subway stations based on the landmark's latitude and longitude.
   - The search radius is expanded gradually (1000m -> 2000m -> 4000m).

3. **Distance Calculation**
   - Use the Haversine formula to calculate the geographical distance (km) between the landmarks and stations.

4. **Output Files**
   - Save the nearest station information for each landmark locally.
   - Count the number of landmarks associated with each station.
   - Log files

### Process

1. Enter the Bangumi work ID.
2. Fetch and save the landmark data.
3. Search for the nearest stations for each landmark and record the results.
4. Save detailed station information and statistics, and output to a log.

## APIs

1. **Anitabi API**
   - **Reference**: [Anitabi APIs](https://github.com/anitabi/anitabi.cn-document/blob/main/api.md)
   - **Parameters**: `haveImage` (optional, `true` filters landmarks with images, default is `false`)【This might not be effective】
   - **Purpose**: Query pilgrimage landmark information for a specific anime based on its Bangumi entry ID. The Bangumi entry ID can be obtained from the entry's URL.
   - **Response Data**: Landmark list containing fields like `id`, `name`, `geo`, `origin`, `originURL`, etc.
   - **License**: CC BY-NC-SA 4.0 (Attribution, Non-Commercial Use, ShareAlike).

2. **Overpass API (OpenStreetMap)**
   - **Reference**: [Overpass APIs](https://wiki.openstreetmap.org/wiki/Overpass_API)
   - **Query**: Use Overpass QL to search for nearby rail transport stations (`railway=station`) or subway stations (`station=subway`) at the target coordinates.
   - **Purpose**: Find the nearest stations based on latitude, longitude, and radius.
   - **Response Data**: JSON format station node information.

### API KEYS

No configuration required, both are public APIs.

### Output Files

- **`{subject_id}_locates.json`**: Landmark data returned by the Anitabi API.
- **`{subject_id}_stations.json`**: Landmark data with the nearest station information.
- **`{subject_id}_station_counts.txt`**: Station statistics for travel planning.
- **`station_query.log`**: Log file.

### Tips
- The Overpass API and Anitabi API may impose request rate limits, please use them moderately.
- You can adjust the search range by modifying the `initial_radius` parameter.

# Chinese 中文

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

# Japanese 日本語

これは、Bangumi作品IDを使用してAnitabi APIから聖地巡礼のランドマーク情報を取得し、その後Overpass APIを使用して各ランドマークから最も近い鉄道（電車/地下鉄）駅を検索するPythonスクリプトです。デフォルトの初期検索範囲は1km、最大検索範囲は4kmです。スクリプトは、ランドマークと駅の間の距離を計算し、各駅に関連するランドマークの数をカウントします。

## 機能

1. **ランドマークデータの取得**
   - Bangumi作品IDを使用してAnitabi APIから聖地巡礼のランドマーク詳細を取得します。

2. **最寄り駅の検索**
   - OpenStreetMapのOverpass APIを使用して、ランドマークの緯度と経度を元に、最寄りの鉄道駅や地下鉄駅を検索します。
   - 検索範囲は順次拡大します（1000m -> 2000m -> 4000m）。

3. **距離計算**
   - Haversine公式を使用して、ランドマークと駅との地理的距離（km）を計算します。

4. **出力ファイル**
   - 各ランドマークの最寄り駅情報をローカルに保存します。
   - 各駅に関連するランドマークの数をカウントします。
   - ログファイル

### 流れ

1. Bangumi作品IDを入力します。
2. ランドマークデータを取得し、保存します。
3. 各ランドマークの最寄り駅を検索し、結果を記録します。
4. 詳細な駅情報と統計結果を保存し、ログとして出力します。

## API

1. **Anitabi API**
   - **参考**: [Anitabi APIs](https://github.com/anitabi/anitabi.cn-document/blob/main/api.md)
   - **パラメータ**: `haveImage`（オプション、`true`で画像付きのランドマークをフィルタリング、デフォルトは`false`）【このパラメータは未対応の可能性があります】
   - **用途**: BangumiエントリIDを使用して、特定のアニメの聖地巡礼のランドマーク情報を取得します。BangumiエントリIDは、エントリのURLから取得できます。
   - **レスポンスデータ**: `id`、`name`、`geo`、`origin`、`originURL`などを含むランドマークのリスト。
   - **ライセンス**: CC BY-NC-SA 4.0（帰属、非商業利用、同じ方法で共有）

2. **Overpass API（OpenStreetMap）**
   - **参考**: [Overpass APIs](https://wiki.openstreetmap.org/wiki/Overpass_API)
   - **クエリ**: Overpass QLを使用して、目標座標の周辺にある鉄道駅（`railway=station`）や地下鉄駅（`station=subway`）を検索します。
   - **用途**: 緯度と経度、および設定した半径を基に最寄りの駅を検索します。
   - **レスポンスデータ**: JSON形式の駅ノード情報。

### API KEYS

設定不要、どちらも公開APIです。

### 出力ファイル

- **`{subject_id}_locates.json`**: Anitabi APIから返されたランドマークデータ。
- **`{subject_id}_stations.json`**: ランドマーク情報と最寄り駅情報。
- **`{subject_id}_station_counts.txt`**: 旅行計画用の駅統計。
- **`station_query.log`**: ログファイル。

### ヒント
- Overpass APIとAnitabi APIはリクエスト頻度を制限する可能性があるため、適切に使用してください。
- `initial_radius`パラメータを変更することで検索範囲を調整できます。
