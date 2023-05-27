import pandas as pd

# Read file Excel and some options
excel_file = ''
df = pd.read_excel(excel_file, usecols=lambda column: column != 2, header= None,  skiprows=[1])
# usecols=lambda column: column != n mmeans ignoring the nth column
# header = none means don't ignore the first row
# skiprows = [n] means skipping nth row
# write values to the file txt
txt_file = ''
with open(txt_file, 'w') as file:
    for row in df.itertuples(index=False):
        for value in row:
            file.write(str(value) + '\n')

print("Recorded value from Excel file to text file")
