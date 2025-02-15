import requests

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json'

params = {
    'scene': 1,
    'query': 'python',
    'city': '101040100',
    'page': 1,
    'pageSize': 30
}

response = requests.get(url, params=params)
data = response.json()

for job in data['zpData']['jobList']:
    print(f"职位: {job['jobName']}, 薪资: {job['salary']}, 公司: {job['brandName']}")