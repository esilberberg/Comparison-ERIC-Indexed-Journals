import pandas as pd

excel_file_name = 'data/1-journals-2024-2025-ERIC-indexing-policy.xlsx'
sheet_2025 = '2025-06'
sheet_2024 = '2024-11'

df_2024 = pd.read_excel(excel_file_name, sheet_name=sheet_2024)
df_2025 = pd.read_excel(excel_file_name, sheet_name=sheet_2025)

def create_master_journal_list(df_2024, df_2025):
    """
    Creates a master list of unique journals, prioritizing Indexing Status from df_2025,
    and indicating presence/absence of journals in original journal list by year.
    """

    # 1. Get all unique journal names
    all_journals = pd.concat([df_2024['Journal Name 2024'], df_2025['Journal Name 2025']]).unique()
    master_df = pd.DataFrame({'Journal Name': all_journals})

    # 2. Merge df_2025's Indexing Status (supersedes df_2024)
    # Perform a left merge with df_2025 to get its Indexing Status
    master_df = pd.merge(master_df, df_2025[['Journal Name 2025', 'Indexing Status 2025']],
                         left_on='Journal Name', right_on='Journal Name 2025', how='left')

    # Rename the merged 'Indexing Status 2025' column
    master_df.rename(columns={'Indexing Status 2025': 'Indexing Status_2025'}, inplace=True)
    # Drop the redundant 'Journal Name 2025' column that resulted from the merge
    master_df.drop(columns=['Journal Name 2025'], inplace=True)


    # 3. Left Merge df_2024's Indexing Status
    master_df = pd.merge(master_df, df_2024[['Journal Name 2024', 'Indexing Status 2024']],
                         left_on='Journal Name', right_on='Journal Name 2024', how='left')

    # Rename the merged 'Indexing Status 2024' column
    master_df.rename(columns={'Indexing Status 2024': 'Indexing Status_2024'}, inplace=True)
    # Drop the redundant 'Journal Name 2024' column that resulted from the merge
    master_df.drop(columns=['Journal Name 2024'], inplace=True)

    # Combine 'Indexing Status_2025' and 'Indexing Status_2024'.
    # Use fillna to prioritize _2025 status.
    # If _2025 status is NaN (journal not in 2025), it will use _2024 status.
    master_df['Indexing Status'] = master_df['Indexing Status_2025'].fillna(master_df['Indexing Status_2024'])

    # Drop the temporary status columns
    master_df.drop(columns=['Indexing Status_2025', 'Indexing Status_2024'], inplace=True)

    # 4. Add 'Not_on_2024' column
    # Create a set of journal names from df_2024 for efficient lookup
    journals_2024_set = set(df_2024['Journal Name 2024'])
    master_df['Not_on_2024'] = master_df['Journal Name'].apply(
        lambda x: 'X' if x not in journals_2024_set else ''
    )

    # 5. Add 'Not_on_2025' column
    # Create a set of journal names from df_2025 for efficient lookup
    journals_2025_set = set(df_2025['Journal Name 2025'])
    master_df['Not_on_2025'] = master_df['Journal Name'].apply(
        lambda x: 'X' if x not in journals_2025_set else ''
    )

    # Reorder columns for better readability (optional)
    master_df = master_df[['Journal Name', 'Indexing Status', 'Not_on_2024', 'Not_on_2025']]

    return master_df

# Call the function to create the master list
df_master = create_master_journal_list(df_2024, df_2025)

# If a journal is not on 2025 list, then indexing status is unknown
df_master.loc[df_master['Not_on_2025'] == 'X', 'Indexing Status'] = 'unknown'

output_excel_file = "master-journal-list.xlsx"

df_master.to_excel(output_excel_file, index=False)