from fastapi import FastAPI
from Api.InvestingTechnical import *
from HtmlToInfoAnalyseCurrency import *
from Enum.EnumIdCurrency import EnumIdCurrency

app = FastAPI()

@app.get("/IndicatorCurrency/{period}")
def IndicatorCurrency(period):
    currencyId = EnumIdCurrency.EUR_USD
    responseHtml = GetCurrencyFromAnalyseTechnicalHtml(currencyId, period)
    return HtmlToInfoAnalyseCurrency(responseHtml, currencyId, period)

