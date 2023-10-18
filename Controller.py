import string

from fastapi import FastAPI
from ResponseApi import *
from ConverterHtmlToDto import *

app = FastAPI()

@app.get("/IndicatorCurrency/{period}")
def IndicatorCurrency(period):
    currencyId = 1
    responseHtml = GetResponseHtml(currencyId, period)
    dto = HtmlToDto(responseHtml, currencyId, period)
    return dto