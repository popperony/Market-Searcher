import requests


def GESearch(query: str):
    url = 'https://www.googleapis.com/customsearch/v1'
    API_KEY = 'AIzaSyDO8Be4yBVOht6rjpDCNZ17XP3RP5NwvM4'
    se_ID = '0eed1a6041c25ae17'
    payload = {'key': API_KEY, 'cx': se_ID, 'q': query}
    response = requests.get(url, params=payload)
    result = []
    for i in range(3):
        result.append(response.json()['items'][i]['pagemap']['cse_image'][0]['src'])
    return result
