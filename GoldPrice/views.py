from email import message
from this import d
from django.shortcuts import render
from urllib import response
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from bs4 import BeautifulSoup
import lxml

@api_view(['GET'])
def gold(request):
    gold_rate_in_india_url = 'https://gadgets360.com/finance/gold-rate-in-india'

    source = requests.get(gold_rate_in_india_url)
    soup = BeautifulSoup(source.text, 'lxml')
    it = soup.getText()

    data = []
    table = soup.find('table', {'id': 'city_wise_data'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    dg = {}
    d1 = {}
    d2 = {}

    for i in range(len(data)):
        d1.update({data[i][0]:data[i][1].replace('\u20b9','')})

    for i in range(len(data)):
        d2.update({data[i][0]:data[i][2].replace('\u20b9','')})

    dg = {
        '24k':d1,
        '22k':d2
    }

    return JsonResponse(dg ,safe=False)


@api_view(['GET'])
def silver(request):
    silver_rate_in_india_url = 'https://www.bankbazaar.com/silver-rate-india.html'

    source = requests.get(silver_rate_in_india_url)
    soup = BeautifulSoup(source.text, 'lxml')
    it = soup.getText()

    data = []
    table = soup.find('table', {'class': 'table table-curved tabdetails heightcontroltable'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # print(data)
    ds = {}
    d1 = {}
    d2 = {}

    for i in range(len(data)):
        d1.update({data[i][0]:data[i][1]})

    for i in range(len(data)):
        d2.update({data[i][0]:data[i][2]})

    ds = {
        'Silver (1 gram)':d1,
        'Bar Silver (1 Kg)':d2
    }

    return JsonResponse(ds ,safe=False)



# class all(object):
#     def __init__(self):
#         self.gold = gold()
#         self.silver = silver()

#     def get_all(self):
#         return JsonResponse(self.gold, self.silver, safe=False)


# @api_view(['GET'])
# def all(request):
#     gold = gold(request)
#     silver = silver(request)
#     return JsonResponse(gold, silver, safe=False)




    

    



