import webbrowser
import time

print("準備開啟你的每日網站...")
time.sleep(2)  # 延遲 2 秒，製造小等待感

# 開啟網站
urls = [
    "https://mail.google.com",
    "https://github.com",
    "https://www.youtube.com"
]

for url in urls:
    webbrowser.open(url)
    time.sleep(1)