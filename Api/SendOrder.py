import requests

from Configuration import GetConfiguration
from Enum.EnumOperationType import EnumOperationType


def SendOrder(CurrencyName, OperationType : EnumOperationType, Value, DurationInMinutes):
    configuration = GetConfiguration()
    urlBaseApiTraderExecute = configuration["URLBaseApiTraderExecute"]

    url = f"{urlBaseApiTraderExecute}/SendOrder{CurrencyName}&{OperationType}&{Value}&{DurationInMinutes}"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=None)

    if(response.status_code == 200):
        print(f"Order type ({OperationType}) send to IqOption.")
    else:
        print(f"Error to send order to IqOption.")
