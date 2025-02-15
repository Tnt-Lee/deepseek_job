import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# 数据
data = pd.read_csv(r'out_qc\output_qg_java_20250215.csv')  # 假设数据是 CSV 格式
# 按照 'jobAreaString' 列升序排序
# 创建 DataFrame
df = pd.DataFrame(data)
# 删除包含NaN值的行
df = df.dropna(subset=["lon", "lat", "jobSalaryMax"])
# 指定解压后的文件路径
file_path = r"ne_10m_admin_0_countries_chn\ne_10m_admin_0_countries_chn.shp"

# 加载数据
china_map = gpd.read_file(file_path)
# 加载中国地图数据
# china_map = china_map[china_map["iso_a3"] == "CHN"]  # 仅保留中国部分

# 绘制地图
fig, ax = plt.subplots(figsize=(10, 8))
china_map.plot(ax=ax, color="lightblue", edgecolor="black")

# 添加工作地点的热力图
plt.scatter(df["lon"], df["lat"], c=df["jobSalaryMax"], cmap="Reds", s=50, alpha=0.6)
plt.colorbar(label="Max Salary")

# 设置地图范围
ax.set_xlim([70, 140])  # 经度范围
ax.set_ylim([15, 55])   # 纬度范围

# 添加标题
plt.title("Job Salary Heatmap in China")
plt.show()