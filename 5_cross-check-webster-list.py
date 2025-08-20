import pandas as pd

excel_file = 'data/4-journals-with-openalex-data.xlsx'
webster_file = 'data/Webster-journals.xlsx'

df = pd.read_excel(excel_file)
webster_df = pd.read_excel(webster_file)

target_journals = df[df['issn_l'].isin(webster_df['issn_l'])]
print(target_journals)