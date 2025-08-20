import pandas as pd
import requests

excel_file = 'data/2-master-journal-list.xlsx'

def get_issn(journal_name):
    """Fetches a journal's ISSN-L from the OpenAlex API."""
    
    base_url = 'https://api.openalex.org/sources?search='
    api_endpoint = base_url + journal_name
    response = requests.get(api_endpoint)
    response_json = response.json()
    data = response_json.get('results')

    if data:
        data = data[0]
        issn_l = data.get('issn_l')
        return issn_l
    else:
        return None 

df = pd.read_excel(excel_file)
df['issn_l'] = df['Journal Title'].apply(get_issn)

output_excel_file = '3-journals-and-issn.xlsx'
df.to_excel(output_excel_file, index=False)