import csv
import requests
from bs4 import BeautifulSoup

books = [] # 儲存所有書的資料

for i in range(1, 10):
    url = 'https://www.sanmin.com.tw/search/index?ct=k&k=AI%e4%ba%ba%e5%b7%a5%e6%99%ba%e6%85%a7&ls=sd&fu=0&vs=list&pi=' + str(i)
    # 來對 url發送一個 GET請求，回應的內容是一個字串
    html = requests.get(url).text
    # 創建一個 BeautifulSoup物件，可以更好操作 html的結構
    soup = BeautifulSoup(html, 'html.parser')
    
    products = soup.find_all('div', 'Info') # 抓取一本書籍資料（書名、作者、價格）
    
    for product in products: # 處理資料
        name = product.find('h3', 'Title').a 
        # 抓取書籍資料（書名）
        author = product.find('div', 'Author').find('span', class_='text-green').a
        # 抓取一本書籍資料（作者）
        price = product.find('span', 'Price')
        # 抓取一本書籍資料（價格）
        if name is not None and author is not None and price is not None: 
            # 判斷是否有抓取到資料
            book=[] # 儲存單一本書的資料
            name_element = "書名：" + name.text + " "  # 抓取書名資料轉為text
            author_element = "作者：" + author.text + " " # 抓取作者資料轉為text
            price_element = "價格：" + price.text + "元" # 抓取價格資料轉為text
            price_value = int(price.text) # 提取價格的數值部分並轉換為int
            book.append(name_element ) # 本書資料加入串列
            book.append(author_element)
            book.append(price_element)
            books.append((book, price_value))  # 將價格數值與書籍資料一起存儲

# 按價格進行排序
sorted_books = sorted(books, key=lambda x: x[1]) # 利用串列的價格資料(x[1])排序
for item in sorted_books:
    print(item[0], "\n") # 分行印出資料
    
# 檔案建立或讀取地址
directory = "/Users/anguschen/Desktop/PythonCrawler/"
text_file_path = directory + "books.txt"
csv_file_path = directory + "books.csv"

"""
textfile = open(text_file_path,'w') # 新建檔案若存在則清空並寫入資料
textfile.write("學號：B1043003，姓名：陳麒安"+"\n")
for item in sorted_books: # 寫入資料
    textfile.write(item[0][0] + "\n") # 依序寫入書名、作者、價格
    textfile.write(item[0][1] + "\n")
    textfile.write(item[0][2] + "\n")
    textfile.write("\n")
textfile.close() # 關閉檔案
print("TXT file writing completed")

with open(csv_file_path, "w", encoding='utf-8') as csvfile:
    # 打開名為 "books.csv" 的 CSV 檔案，並使用 UTF-8 編碼寫入
    csv_writer = csv.writer(csvfile)
    # 寫入CSV文件的標題行
    csv_writer.writerow(["書名", "作者", "價格"])
    # 寫入書籍資訊
    for book in sorted_books:
        csv_writer.writerow(book[0])     
print("CSV file writing completed")
"""