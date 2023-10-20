import requests
def GetCurrencyFromAnalyseTechnicalHtml(currencyId, period):
    url = "https://br.investing.com/technical/Service/GetStudiesContent"

    payload = f"pairID={currencyId}&period={period}"
    headers = {
        'x-requested-with': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
