import json
import csv
import os

# 指定目录
directory = r'qianchengwuyou\20250214'

# 初始化一个列表来存储所有JSON数据
all_data = []

# 遍历目录下的所有文件
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        json_path = os.path.join(directory, filename)
        with open(json_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            json_data =json_data['resultbody']['job']['items']
            all_data.extend(json_data)

# 确保有数据可以写入CSV文件
if all_data:
    # 打开CSV文件以写入模式
    with open('out_qc/output_dl_java.csv', 'w+', newline='', encoding='utf-8-sig') as csv_file:
        # 获取JSON数据的键作为CSV文件的列名
        fieldnames = all_data[0].keys()
        
        # 创建DictWriter对象
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # 写入CSV文件的表头
        writer.writeheader()
        
        # 写入JSON数据
        for row in all_data:
            writer.writerow(row)

    print("所有JSON数据已成功写入CSV文件")
else:
    print("目录中没有找到JSON文件或JSON文件为空")