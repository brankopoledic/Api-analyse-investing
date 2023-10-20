from Api.InvestingTechnical import *
from HtmlToInfoAnalyseCurrency import *
from Enum.EnumIdCurrency import EnumIdCurrency
from Enum.EnumStatusIndicatorCurrency import EnumStatusIndicatorCurrency
from Enum.EnumPeriod import EnumPeriod
import time
import datetime

def MonitorSellOrBuyCurrecy(currencyId):
    indicatorToBuy = EnumStatusIndicatorCurrency.COMPRA_FORTE
    indicatorToSell = EnumStatusIndicatorCurrency.VENDA_FORTE
    timerBuyOrSell = 41
    executeLoop = True

    while(executeLoop):
        indicatorMinute01 = GetIndicatorCurrency(currencyId, EnumPeriod.MINUTO_01)
        indicatorMinute05 = GetIndicatorCurrency(currencyId, EnumPeriod.MINUTO_05)
        indicatorMinute15 = GetIndicatorCurrency(currencyId, EnumPeriod.MINUTO_15)

        buyInMinute01 = indicatorMinute01.Status == indicatorToBuy
        buyInMinute05 = indicatorMinute05.Status == indicatorToBuy
        buyInMinute15 = indicatorMinute15.Status == indicatorToBuy

        sellInMinute01 = indicatorMinute01.Status == indicatorToSell
        sellInMinute05 = indicatorMinute05.Status == indicatorToSell
        sellInMinute15 = indicatorMinute15.Status == indicatorToSell


        buy = buyInMinute01 and buyInMinute05 and buyInMinute15
        sell = sellInMinute01 and sellInMinute05 and sellInMinute15

        if buy:
            BuyOrSellCurrency(indicatorToBuy)
            #executeLoop = False
            TimmingController(timerBuyOrSell)
            #executeLoop = True

        if sell:
            BuyOrSellCurrency(indicatorToSell)
            #executeLoop = False
            TimmingController(timerBuyOrSell)
            executeLoop = True

        print(f"01min: {indicatorMinute01.Status}-{indicatorMinute01.UpdateTime} | 05min: {indicatorMinute05.Status}-{indicatorMinute05.UpdateTime} | 15min: {indicatorMinute15.Status}-{indicatorMinute15.UpdateTime} ")

def GetIndicatorCurrency(currencyId, period):
    responseHtml = GetCurrencyFromAnalyseTechnicalHtml(currencyId, period)
    dto = HtmlToInfoAnalyseCurrency(responseHtml, currencyId, period)
    return dto

def TimmingController(timer_in_seconds):
    print(f"Monitoring Paused and Timing Start, Wait to {timer_in_seconds}")
    for i in range(timer_in_seconds, 0, -1):
        print(f"Timing to restart: {i} seconds")
        time.sleep(1)
    print("Monitoring Continue and Timing Stop")

def BuyOrSellCurrency(BuyOrSell : EnumStatusIndicatorCurrency):
    print(BuyOrSell)

print("Start Monitoring Status Currency . . .")
MonitorSellOrBuyCurrecy(EnumIdCurrency.EUR_USD)