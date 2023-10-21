from Api.InvestingTechnical import *
from Api.SendOrder import SendOrder
from Configuration import GetConfiguration
from Enum.EnumOperationType import EnumOperationType
from HtmlToInfoAnalyseCurrency import *
from Enum.EnumIdCurrency import EnumIdCurrency
from Enum.EnumStatusIndicatorCurrency import EnumStatusIndicatorCurrency
from Enum.EnumPeriod import EnumPeriod
import time
import datetime

def MonitorSellOrBuyCurrecy(currencyId: EnumIdCurrency):
    configuration = GetConfiguration()
    valueToSendInOrder = configuration["ValueToSendInOrder"]
    indicatorToBuy = EnumStatusIndicatorCurrency.COMPRA_FORTE
    indicatorToSell = EnumStatusIndicatorCurrency.VENDA_FORTE
    timerBuyOrSell =  int(configuration["TimeToWaitAfterSendOrder"])
    executeLoop = True

    while(executeLoop):
        indicatorMinute01 = GetIndicatorCurrency(currencyId, EnumPeriod.MINUTO_01)
        indicatorMinute05 = GetIndicatorCurrency(currencyId, EnumPeriod.MINUTO_05)
        indicatorMinute15 = GetIndicatorCurrency(currencyId, EnumPeriod.MINUTO_15)

        buyInMinute01 = indicatorMinute01.Status == indicatorToBuy.value
        buyInMinute05 = indicatorMinute05.Status == indicatorToBuy.value
        buyInMinute15 = indicatorMinute15.Status == indicatorToBuy.value

        sellInMinute01 = indicatorMinute01.Status == indicatorToSell.value
        sellInMinute05 = indicatorMinute05.Status == indicatorToSell.value
        sellInMinute15 = indicatorMinute15.Status == indicatorToSell.value

        buy = True
        sell = sellInMinute01 and sellInMinute05 and sellInMinute15

        if buy:
            executeLoop = False
            BuyOrSellCurrency(indicatorMinute01.CurrencyName, indicatorToBuy, valueToSendInOrder)
            TimmingController(timerBuyOrSell)
            executeLoop = True

        if sell:
            executeLoop = False
            BuyOrSellCurrency(indicatorMinute01.CurrencyName, indicatorToSell, valueToSendInOrder)
            TimmingController(timerBuyOrSell)
            executeLoop = True

        print(f"CurrencyName: {indicatorMinute01.CurrencyName} | 01min: {indicatorMinute01.Status}-{indicatorMinute01.UpdateTime} | 05min: {indicatorMinute05.Status}-{indicatorMinute05.UpdateTime} | 15min: {indicatorMinute15.Status}-{indicatorMinute15.UpdateTime} ")

def GetIndicatorCurrency(currencyId : EnumIdCurrency, period):
    responseHtml = GetCurrencyFromAnalyseTechnicalHtml(currencyId, period)
    dto = HtmlToInfoAnalyseCurrency(responseHtml, currencyId, period)
    return dto

def TimmingController(timer_in_seconds : int):
    print(f"Monitoring Paused and Timing Start, Wait to {timer_in_seconds}")
    for i in range(timer_in_seconds, 0, -1):
        print(f"Timing to restart: {i} seconds")
        time.sleep(1)
    print("Monitoring Continue and Timing Stop")

def BuyOrSellCurrency(currencyName, buyOrSell, ValueToSendInOrder):
    print("Try to send order to IqOption . . .")
    currencyName = currencyName.replace("/","")

    if buyOrSell.VENDA_FORTE == buyOrSell:
        SendOrder(currencyName, EnumOperationType.Down, ValueToSendInOrder)
    if buyOrSell.COMPRA_FORTE == buyOrSell:
        SendOrder(currencyName, EnumOperationType.Up, ValueToSendInOrder)

print("Start Monitoring Status Currency . . .")
MonitorSellOrBuyCurrecy(EnumIdCurrency.EUR_USD)