import requests
from bs4 import BeautifulSoup

'''获取网站标题'''
url = 'https://cn.bing.com/'  # bing

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 编码格式，根据实际情况选择 utf-8 或者 gbk
response.encoding = 'utf-8'
# 确保请求成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'lxml')

    # 查找<title>标签
    title_tag = soup.find('title')

    # 打印标题文本
    if title_tag:
        print(title_tag.get_text())
    else:
        print("未找到<title>标签")
else:
    print("请求失败，状态码：", response.status_code)
