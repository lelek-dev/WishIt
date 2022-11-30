from googlesearch import search
from bs4 import BeautifulSoup
import requests
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

def getTypesView(request, search):
    if len(search) > 4:
        urls = searchproduct(search)
        data=[]
        for url in urls:
            item = {}
            item['url'] = url
            item['name'] = gettitle(url)
            data.append(item)
        if len(data) > 0:
            return JsonResponse(data=data, safe=False)    
    return HttpResponseBadRequest
    
@csrf_exempt
def getOffersView(request):
    if request.method == 'POST':
        url = request.POST.get("url", "")
        print(url)
        offers = getoffers(url)
        return JsonResponse(offers, safe=False)
    return HttpResponseBadRequest

def searchproduct(input):
    input = "site:https://www.idealo.de/preisvergleich/OffersOfProduct " + input
    urls = []
    for url in search(input,stop = 3, pause = 0.1):
        urls.append(url)
    return urls

def getsoup(url):
    headers = {
        'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup

def getoffers(url):
    soup = getsoup(url)
    title = soup.title.string.rsplit("ab",1)[0]
    a_tags = soup.findAll('a', {'class': 'productOffers-listItemOfferLogoLink'})
    toreturn = []
    for a_tag in a_tags:
        if len(toreturn) >= 5:
            return toreturn
        result = str(a_tag).split("{")[1].split("}")
        link = result[1]
        result = result[0].replace('\t', '').replace('\n', '').split('"product_price"')
        result = '"product_price"' + result[1]
        if result != None:
            data = json.loads("{"+result+"}")
        link = link.split('href="')[1].split("?")
        link = "https://www.idealo.de"+ link[0]
        if link != None:
            data["link"] = link
        data["title"] = title
        toreturn.append(data)
    return toreturn

def gettitle(url):
    soup = getsoup(url)
    title = soup.title.string.rsplit("ab", 1)[0]
    return title