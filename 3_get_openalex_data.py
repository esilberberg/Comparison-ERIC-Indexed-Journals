import pandas as pd
import requests

excel_file_name = 'data/3-journals-and-issn.xlsx'

df = pd.read_excel(excel_file_name)

def get_openalex_data(issn):
    """Fetches select journal metadata from OpenAlex API via the ISSN-L."""
    if issn is None or issn == "":
        print('No ISSN-L')
        # Returns None values to avoid error when assigning later to Dataframe
        return (None,) * 10 
    
    base_url = 'https://api.openalex.org/sources/issn:'
    api_endpoint = base_url + str(issn)
    response = requests.get(api_endpoint)

    if response.status_code != 200:
        print(f"Error retrieving data! (ISSN: {issn}) (Status Code: {response.status_code})")
        return (None,) * 10  # Returns None values to avoid error when assigning later to Dataframe

    data = response.json()

    homepage = data.get('homepage_url')
    is_oa = data.get('is_oa')
    is_in_doaj = data.get('is_in_doaj')
    country = data.get('country_code')

    print(issn)
    print(homepage, country, is_oa, is_in_doaj)
    return homepage, country, is_oa, is_in_doaj



new_columns = ['homepage', 'country', 'is_oa', 'is_in_doaj']


df[new_columns] = df['issn_l'].apply(
    lambda x: pd.Series(get_openalex_data(x), index=new_columns)
)

output_excel_file = "journals-with-openalex-data.xlsx"

df.to_excel(output_excel_file, index=False)