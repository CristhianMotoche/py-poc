from bs4 import BeautifulSoup

import requests

def get_baby_names_by_range(init_year, finish_year):
    results = []

    for year in range(init_year, finish_year):
        result = {}
        result['year'] = year
        result['baby_names'] = get_baby_names_by_year(year)
        results.append(result)

    return results

def get_baby_names_by_year(year):
    payload = {'year': year, 'top': 1000, 'number':'n'}
    r = requests.post("https://www.ssa.gov/cgi-bin/popularnames.cgi", data=payload)
    return parse_html(r.text)

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find_all('table')
    table_babynames = tables[2]
    rows = table_babynames.find_all('tr')
    baby_names = []
    for row in rows[1:-1]:
        baby_names.append(get_data_from_row(row))
    return baby_names

def get_data_from_row(row):
    cells = row.find_all('td')
    return { 'rank': cells[0].text
            , 'boy_name': cells[1].text
            , 'number_of_boys': cells[2].text
            , 'girl_name': cells[3].text
            , 'number_of_girls': cells[4].text
            }

