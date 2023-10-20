import configparser

def GetConfiguration():
    arquivo = configparser.RawConfigParser()
    arquivo.read('config.txt')
    return {
        'ValueToSendInOrder': arquivo.get('BALANCE', 'ValueToSendInOrder'),
        'TimeToWaitAfterSendOrder': arquivo.get('TIMER', 'TimeToWaitAfterSendOrder')
    }