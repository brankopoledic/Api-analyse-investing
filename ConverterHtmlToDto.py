import requests
from bs4 import BeautifulSoup

def HtmlToDto(html_content, currencyId, period):
    soup = BeautifulSoup(html_content, 'html.parser')

    data = {}
    data['currencyId'] = currencyId
    data['period'] = period
    data['currencyName'] = soup.find('a', {'id': 'quoteLink'}).text.strip()
    data['lastValue'] = soup.find('div', {'id': 'lastValue1'}).text.strip()
    data['updateTime'] = soup.find('div', {'id': 'updateTime'}).text.strip()
    data['status'] = soup.find('div', {'class': 'summary'}).text.strip().replace('Resumo:','')
    data['pivotPoints'] = []
    table = soup.find('table', {'id': 'curr_table'})
    table_rows = table.find_all('tr')
    for row in table_rows:
        col = row.find_all('td')
        if len(col) > 1:
            col_name = col[0].text.strip()
            if col_name == "Fibonacci":
                table_dto = {
                    "Nome": col_name,
                    "S3": col[1].text.strip(),
                    "S2": col[2].text.strip(),
                    "S1": col[3].text.strip(),
                    "PontosPivo": col[4].text.strip(),
                    "R1": col[5].text.strip(),
                    "R2": col[6].text.strip(),
                    "R3": col[7].text.strip()
                }

                data['pivotPoints'].append(table_dto)

    return data