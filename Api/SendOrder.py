import requests
from Enum.EnumOperationType import EnumOperationType


def SendOrder(CurrencyName, OperationType : EnumOperationType, Value):
    url = f"http://127.0.0.1:8000/SendOrder{CurrencyName}&{OperationType}&{Value}"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=None)

    if(response.status_code == 200):
        print(f"Order type ({OperationType}) send to IqOption.")
    else:
        print(f"Error to send order to IqOption.")
