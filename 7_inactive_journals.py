import pandas as pd

excel_file_name = 'data/5-analysis.xlsx'

df = pd.read_excel(excel_file_name, sheet_name='Inactive Journals')

# What % are still publishing in 2025? (Are still actively publishing research)
print(df['Year of last published issue on journal website'].value_counts())
print(df['Year of last published issue on journal website'].value_counts(normalize=True))

# What % have been ERIC-indexed up to 2025? (Established as part of the scholarly record by ERIC and will no longer be)
print(df['Year of last publication indexed by ERIC'].value_counts())
print(df['Year of last publication indexed by ERIC'].value_counts(normalize=True))

# What % are still publishing in 2025 AND ERIC-indexed up to 2025?
filtered_df = df[
    (df['Year of last published issue on journal website'] == 2025) & 
    (df['Year of last publication indexed by ERIC'] == 2025)
]

result = filtered_df[['Journal Name', 'issn_l']]

print(result.count())

# What % are still publishing in 2025 AND NOT ERIC-indexed up to 2025?

filtered_df = df[
    (df['Year of last published issue on journal website'] == 2025) & 
    (df['Year of last publication indexed by ERIC'] != 2025)
]

result = filtered_df[['Journal Name', 'issn_l']]

print(result.count())

# For journals indexed in 2025, on average how long had they been indexed by ERIC?

df.loc[df['Year of last publication indexed by ERIC'] == 2025, 'Length of ERIC Indexing'] = 2025 - df['Year of earliest publication indexed by ERIC']

print(df['Length of ERIC Indexing'].describe())

