import os
from datetime import datetime

# 取得今天日期字串
today = datetime.now().strftime("%Y-%m-%d")

folder_path = 'files'  # 資料夾路徑

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg'):
        old_path = os.path.join(folder_path, filename)
        new_filename = filename.replace('.jpg', '_new.jpg')
                # 新檔名：日期 + "_" + 原檔名
        new_filename_date = f"{today}_{new_filename}"
        new_path = os.path.join(folder_path, new_filename_date)
        os.rename(old_path, new_path)
        print(f"已將 {filename} 改為 {new_filename_date}")