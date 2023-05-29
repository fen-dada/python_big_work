
import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
import matplotlib.pyplot as plt

# 创建一个空字典，用于存储爬取的数据
gdp_data = {}

# 定义一个函数，用于爬取一个国家的GDP数据
def get_gdp_data(country_code):
    # 发送HTTP请求，获取网页源代码
    url = f"https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations={country_code}"
    response = requests.get(url)
    html = response.text

    # 解析HTML文档，提取GDP数据
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="table") # 找到包含GDP数据的表 格
    print(type(table))
    rows = table.find_all("tr") # 找到所有的表格行
    for row in rows[1:]: # 跳过表头行，遍历每一行数据
        cells = row.find_all("td") # 找到每一行中的单元格
        year = cells[0].text.strip() # 提取年份
        gdp = cells[1].text.strip() # 提取GDP值
        if year == "2022": # 如果是预测值，跳过
            continue
        if gdp == "..": # 如果没有数据，用0代替
            gdp = 0
        else:
            gdp = float(gdp.replace(",", "")) # 去掉逗号，转换为浮点数
        gdp_data.setdefault(country_code, {})[year] = gdp # 将年份和GDP值添加到字典中

# 调用函数，分别爬取中国和美国的GDP数据
get_gdp_data("CN") # 中国的国家代码为CN
get_gdp_data("US") # 美国的国家代码为US

# 创建并写入csv文件，将爬取的数据保存起来
with open("gdp.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Year", "China", "USA"]) # 写入表头
    for year in range(2000, 2022): # 遍历每一年
        china_gdp = gdp_data["CN"].get(str(year), 0) # 获取中国的GDP值，如果没有则用0代替
        usa_gdp = gdp_data["US"].get(str(year), 0) # 获取美国的GDP值，如果没有则用0代替
        writer.writerow([year, china_gdp, usa_gdp]) # 写入一行数据

# 读取csv文件，并绘制两个国家的GDP折线图
df = pd.read_csv("gdp.csv") # 使用pandas读取csv文件，返回一个DataFrame对象
plt.plot(df["Year"], df["China"], c="red", label="China") # 绘制中国的GDP折线图，用红色表示，并添加图例标签
plt.plot(df["Year"], df["USA"], c="blue", label="USA") # 绘制美国的GDP折线图，用蓝色表示，并添加图例标签