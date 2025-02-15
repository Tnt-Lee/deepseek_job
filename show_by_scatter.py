import matplotlib.pyplot as plt
import pandas as pd

file_path = r"out_qc\output_dl_java_20250215.csv"  # 替换为你的数据文件路径
# 数据
data = pd.read_csv(file_path)  # 假设数据是 CSV 格式
# 按照 'jobAreaString' 列升序排序
# 创建 DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by='jobAreaString', ascending=True)
df['jobAreaString'].fillna("", inplace=True)  # 或者其他填充值
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者使用 'Microsoft YaHei'，为了防止乱码

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(df['jobAreaString'], df['jobSalaryMax'], color='blue', label='Salary')
plt.title('Salary vs Job')
plt.xlabel('Job')
plt.ylabel('Salary')
plt.grid(True)

# 添加数据标签
for i in range(len(df)):
    # 获取数据点的坐标
    x, y = df['jobAreaString'][i], df['jobSalaryMax'][i]
    plt.text(x, y, df['jobAreaString'][i], fontsize=6, rotation=45, ha='right')
    # 使用 plt.annotate() 添加注释
    plt.annotate(
        df['jobName'][i],  # 标签内容
        (x, y),  # 标签的锚点位置
        textcoords="offset points",  # 指定偏移量的坐标系统
        xytext=(0, 0),  # 偏移量
        ha='right',  # 水平对齐方式
        va='bottom',  # 垂直对齐方式
        fontsize=9,
        rotation=45  # 标签倾斜角度
    )

# 调整 X 轴刻度标签的倾斜角度为向下 45 度
plt.xticks(rotation=-45)
plt.legend()
plt.show()