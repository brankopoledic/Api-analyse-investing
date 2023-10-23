import requests

from Configuration import GetConfiguration
from Enum.EnumTypeMessage import EnumTypeMessage

def SendMessageToTelegram(typeMessage : EnumTypeMessage, message):
    try:
        configuration = GetConfiguration()
        urlBaseNotificationManager = configuration["URLBaseApiNotificationManager"]

        url = f"{urlBaseNotificationManager}/SendMessageToTelegram/{typeMessage}&{message}"

        response = requests.get(url)

        if (response.status_code == 200):
            print(f'Message send to telegram with sucess')
            return
        else:
            print(f'Error to send messagem to telegram: : {response.status_code}')
            return
    except Exception as e:
        print("Error to send message to telegram: ", e)