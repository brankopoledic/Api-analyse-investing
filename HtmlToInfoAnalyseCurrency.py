import requests
from bs4 import BeautifulSoup
from Entities.InfoAnalyseCurrency import *
from Entities.PointPivot import *
from ExceptionGeneric import ExceptionGeneric


def HtmlToInfoAnalyseCurrency(html_content, currencyId, period):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        infoAnalyseCurrency = InfoAnalyseCurrency()
        infoAnalyseCurrency.CurrencyName = soup.find('a', {'id': 'quoteLink'}).text.strip()
        infoAnalyseCurrency.CurrencyId = currencyId
        infoAnalyseCurrency.Period = period
        infoAnalyseCurrency.LastValue = soup.find('div', {'id': 'lastValue1'}).text.strip()
        infoAnalyseCurrency.UpdateTime = soup.find('div', {'id': 'updateTime'}).text.strip()
        infoAnalyseCurrency.Status = soup.find('div', {'class': 'summary'}).text.strip().replace('Resumo:', '')
        listPointPivot = []

        table = soup.find('table', {'id': 'curr_table'})
        table_rows = table.find_all('tr')
        for row in table_rows:
           col = row.find_all('td')
           if len(col) > 1:
               col_name = col[0].text.strip()
               if col_name == "Fibonacci":
                   pointPivot = PointPivot()
                   pointPivot.Name = col_name
                   pointPivot.S3 = col[1].text.strip()
                   pointPivot.S2 = col[2].text.strip()
                   pointPivot.S1 = col[3].text.strip()
                   pointPivot.PointsPivot = col[4].text.strip()
                   pointPivot.R1 = col[5].text.strip()
                   pointPivot.R2 = col[6].text.strip()
                   pointPivot.R3 = col[7].text.strip()
                   listPointPivot.append(pointPivot)

        infoAnalyseCurrency.ListPivotPoints = listPointPivot

        return infoAnalyseCurrency
    except Exception as error:
        print("ERROR DETECTED IN HtmlToInfoAnalyseCurrency")
        infoAnalyseCurrency = InfoAnalyseCurrency()
        infoAnalyseCurrency.Status = "ERROR"
        return infoAnalyseCurrency