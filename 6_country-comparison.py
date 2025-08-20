import pandas as pd

excel_file_name = 'data/5-analysis.xlsx'
sheet_name = 'Country Comparison'

df = pd.read_excel(excel_file_name, sheet_name=sheet_name)

df['Absolute Change Count'] = df['count 2025'] - df['count 2024']
df['Percent Change'] = ((df['count 2025'] - df['count 2024']) / df['count 2024'])*100

print(df)