from fastapi import FastAPI
from Api.InvestingTechnical import *
from HtmlToInfoAnalyseCurrency import *
from Enum.EnumIdCurrency import EnumIdCurrency
from Monitor import MonitorSellOrBuyCurrecy

app = FastAPI()

@app.get("/IndicatorCurrency/{period}&{currencyId}")
def IndicatorCurrency(period, currencyId):
    responseHtml = GetCurrencyFromAnalyseTechnicalHtml(currencyId, period)
    return HtmlToInfoAnalyseCurrency(responseHtml, currencyId, period)

@app.get("/StartMonitor/{currencyId}")
def IndicatorCurrency(currencyId):
    #MonitorSellOrBuyCurrecy(currencyId)
    return f"Monitoring currency id:{currencyId} started . . ."

