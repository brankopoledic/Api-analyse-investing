import configparser

def GetConfiguration():
    arquivo = configparser.RawConfigParser()
    arquivo.read('config.txt')
    return {
        'ValueToSendInOrder': arquivo.get('BALANCE', 'ValueToSendInOrder'),
        'TimeInMinutesToWaitAfterSendOrder': arquivo.get('TIMER', 'TimeInMinutesToWaitAfterSendOrder'),
        'TimeInMinutesInBroker': arquivo.get('TIMER', 'TimeInMinutesInBroker'),
        'TimeInMinutesToMonitoringCurrency': arquivo.get('TIMER', 'TimeInMinutesToMonitoringCurrency'),
        'URLBaseApiNotificationManager': arquivo.get('URL_BASE', 'URLBaseApiNotificationManager'),
        'URLBaseApiTraderExecute': arquivo.get('URL_BASE', 'URLBaseApiTraderExecute')
    }