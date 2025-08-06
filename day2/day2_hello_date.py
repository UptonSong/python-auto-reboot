from datetime import date

print("Hello Automation!")
today = date.today()
roc_year = today.year - 1911
roc_date_str = f"{roc_year:03d}/{today.month:02d}/{today.day:02d}"

print(roc_date_str)  # 114/08/06