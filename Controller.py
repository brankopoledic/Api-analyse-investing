from fastapi import FastAPI
from Api.InvestingTechnical import *
from HtmlToInfoAnalyseCurrency import *
from Enum.EnumIdCurrency import EnumIdCurrency

app = FastAPI()

@app.get("/IndicatorCurrency/{period}&{currencyId}")
def IndicatorCurrency(period, currencyId):
    responseHtml = GetCurrencyFromAnalyseTechnicalHtml(currencyId, period)
    return HtmlToInfoAnalyseCurrency(responseHtml, currencyId, period)

