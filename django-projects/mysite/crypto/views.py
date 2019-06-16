from django.shortcuts import render
import requests
import json

def home(request):

    # grab crypto price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    # grab crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"api": api, "price": price})

def prices(request):
    if request.method == "POST":
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD,JPY")
        crypto = json.loads(crypto_request.content)

        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        return render(request, 'prices.html', {'notfound': "NOT FOUND"})
