import os
import webbrowser
import csv
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 取得當前檔案所在資料夾

# ===== 功能 1: 開啟常用網站 =====
def open_websites():
    websites = [
        "https://www.google.com",
        "https://github.com",
        "https://news.ycombinator.com"
    ]
    for site in websites:
        webbrowser.open(site)
    print("✅ 已開啟常用網站")

# ===== 功能 2: 讀取 CSV =====
def read_csv():
    csv_path = os.path.join(BASE_DIR, "day4", "data.csv")
    if not os.path.exists(csv_path):
        print(f"❌ 找不到 CSV 檔案: {csv_path}")
        return
    
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
    print("✅ 已讀取 CSV 檔案")

# ===== 功能 3: 批次檔案改名 (加日期) =====
def rename_files():
    folder_path = os.path.join(BASE_DIR, "day5", "files")
    if not os.path.exists(folder_path):
        print(f"❌ 找不到資料夾: {folder_path}")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            new_filename = f"{today}_{filename}"
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"已將 {filename} 改為 {new_filename}")
    print("✅ 已完成批次檔案改名")

# ===== 顯示完成紀錄 =====
def show_progress():
    print("\n🎉 七天自動化挑戰完成紀錄 🎉")
    days = [
        "Day 1 - Hello World",
        "Day 2 - GitHub 版本控制",
        "Day 3 - 開啟常用網站",
        "Day 4 - 讀取 CSV",
        "Day 5 - 批次檔案改名",
        "Day 6 - README 整理",
        "Day 7 - 多功能自動化工具"
    ]
    for day in days:
        print(f"✅ {day}")
    print("\n🏆 恭喜你完成全部挑戰！")

# ===== 主選單 =====
def main():
    while True:
        print("\n請選擇功能：")
        print("1. 開啟常用網站")
        print("2. 讀取 CSV")
        print("3. 批次檔案改名")
        print("0. 離開")
        
        choice = input("輸入選項: ")
        
        if choice == "1":
            open_websites()
        elif choice == "2":
            read_csv()
        elif choice == "3":
            rename_files()
        elif choice == "0":
            show_progress()
            print("👋 再見！")
            break
        else:
            print("⚠️ 無效選項，請重新輸入")

if __name__ == "__main__":
    main()
