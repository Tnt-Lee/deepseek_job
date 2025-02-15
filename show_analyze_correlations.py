import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_correlations(file_path):
    # 读取数据
    data = pd.read_csv(file_path)  # 假设数据是 CSV 格式

    # 筛选浮点数列
    float_columns = data.select_dtypes(include=['float64', 'int64']).columns
    float_data = data[float_columns]
    # 计算相关系数矩阵
    correlation_matrix = float_data.corr()

    # 打印相关系数矩阵
    print("相关系数矩阵：")
    print(correlation_matrix)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者使用 'Microsoft YaHei'，为了防止乱码
    # 绘制热力图
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("字段相关性热力图")
    plt.show()

# 使用示例
file_path = r"out_qc\output_dl_java.csv"  # 替换为你的数据文件路径
analyze_correlations(file_path)