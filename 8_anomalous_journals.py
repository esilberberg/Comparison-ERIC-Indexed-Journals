import pandas as pd

excel_file_name = 'data/5-analysis.xlsx'

sheet_names = ['Not on 2024', 'Not on 2025']

for sheet in sheet_names:
    print('--------------' + sheet + '--------------')
    df = pd.read_excel(excel_file_name, sheet_name=sheet)

# What % are still publishing in 2025? (Are still actively publishing research)
    print(df['Year of last published issue on journal website'].value_counts())
    print(df['Year of last published issue on journal website'].value_counts(normalize=True))

# What % have been ERIC-indexed up to 2025? (Established as part of the scholarly record by ERIC and will no longer be)
    print(df['Year of last publication indexed by ERIC'].value_counts())
    print(df['Year of last publication indexed by ERIC'].value_counts(normalize=True))

# 'Year of earliest publication indexed by ERIC'
    print(df['Year of earliest publication indexed by ERIC'].value_counts())
    print(df['Year of earliest publication indexed by ERIC'].value_counts(normalize=True))