import pandas as pd

excel_file = 'của-Sơn-máy-5.xlsx'
# Đọc file Excel vào DataFrame
df = pd.read_excel(excel_file, usecols=[1,2], skiprows=4, header= None)

txt_file = 'Trim video\\cut segment time.txt'
# Ghi dữ liệu vào file txt
with open(txt_file, 'w') as file:
    for index, row in df.iterrows():
        for col in df.columns:
            value = row[col]
            file.write(str(value) + '\n')
