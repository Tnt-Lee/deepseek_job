import folium
from folium.plugins import HeatMap
import pandas as pd

# 示例数据
data = pd.read_csv(r'out_qc\output_qg_java_20250215.csv')  # 假设数据是 CSV 格式
# 按照 'jobAreaString' 列升序排序
# 创建 DataFrame
df = pd.DataFrame(data)
# 删除包含NaN值的行
df = df.dropna(subset=["lon", "lat", "jobSalaryMax"])
# 提取经纬度信息
df["lon"] = df["lon"].astype(float)
df["lat"] = df["lat"].astype(float)
# 创建一个地图对象，初始位置为大连市，缩放级别为6
map_center = [38.9133, 121.6124]  # 大连市的经纬度
mymap = folium.Map(location=map_center, zoom_start=6)

# 准备热力图数据：提取经纬度和权重（可以使用薪资范围作为权重）
heat_data = df[["lat", "lon", "jobSalaryMax"]].values.tolist()

# 添加热力图层
HeatMap(heat_data, radius=10).add_to(mymap)

# 保存为HTML文件
mymap.save("heatmap.html")