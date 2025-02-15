import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设数据已经保存为CSV文件
# data = pd.read_csv(r"out_qc\output_dl_java_20250215.csv")
data = pd.read_csv(r"out_qc\output_dl_java.csv")

# 数据预处理
# 1. 提取薪资范围的平均值
def extract_salary(salary_str):
    try:
        lower, upper = map(float, salary_str.split("-"))
        return (lower + upper) / 2
    except:
        return None

data["Average Salary"] = (data["jobSalaryMax"]+data["jobSalaryMin"])/2

# 2. 简化工作地点
data["Job Area Simplified"] = data["jobAreaString"]

# 3. 创建热力图需要的交叉表
# 例如：按工作地点和公司类型统计平均薪资
heatmap_data = pd.pivot_table(data, values="Average Salary", index="Job Area Simplified", columns="companyTypeString", aggfunc="mean")
plt.rcParams['font.sans-serif'] = ['SimHei'] # 或者使用 'Microsoft YaHei'，为了防止乱码

# 生成热力图
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Average Salary by Job Area and Company Type")
plt.xlabel("Company Type")
plt.ylabel("Job Area")
plt.show()