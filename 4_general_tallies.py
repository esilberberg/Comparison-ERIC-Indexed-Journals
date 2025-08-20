import pandas as pd


excel_file_name = 'data/4-journals-with-openalex-data.xlsx'

df = pd.read_excel(excel_file_name)

# Journal counts per category
df.count()
all_in_2024 = df[df['Not_on_2024'] != 'X']
all_in_2025 = df[df['Not_on_2025'] != 'X']
unique_in_2024 = df[df['Not_on_2025'] == 'X']
unique_in_2025 = df[df['Not_on_2024'] == 'X']
inactive_indexing = df[df['Indexing Status'] == 'Inactive']
active_indexing_2025 = all_in_2025[all_in_2025['Indexing Status'] == 'Active']


categories = {
    'all': df,
    'All in 2024': all_in_2024,
    'All in 2025': all_in_2025,
    'Active indexing 2025': active_indexing_2025,
    'Inactive indexing': inactive_indexing,
    'Unique 2024': unique_in_2024,
    'Unique 2025': unique_in_2025  
}

# OA Comparison
for name, value in categories.items():
    print(f"Variable Name: {name}---------------")
    print(value['is_oa'].count())
    print(value['is_oa'].value_counts())
    print(value['is_oa'].value_counts(normalize=True))

# DOAJ Comparison
for name, value in categories.items():
    print(f"Variable Name: {name}---------------")
    print(value['is_in_doaj'].count())
    print(value['is_in_doaj'].value_counts())
    print(value['is_in_doaj'].value_counts(normalize=True))

# Country Comparison
for name, value in categories.items():
    print(f"Variable Name: {name}---------------")
    print(value['country'].count())
    print(value['country'].value_counts())
    print(value['country'].value_counts(normalize=True))