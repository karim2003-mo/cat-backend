from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import *
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from bs4 import BeautifulSoup
import time
import random
# Create your views here.
def test(request):
    return HttpResponse("Hello World")
@api_view(['GET'])
def product(request):
    p= WhatsUsers.objects.all()
    print(p[0].image.path)
    data=ProductSerializer(p,many=True).data
    return Response({'data':data})
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    ]
def vote(request):
    for i in range(200):
        try:
            for i in range(10):

                # Step 1: Get the page where the form is located
                session = requests.Session()
                url1 = "https://www.radionrjfm.com/vote/5"
                response = session.get(url1)

                # Step 2: Parse the page to extract the token
                soup = BeautifulSoup(response.text, "html.parser")
                csrf_token = soup.find("input", {"name": "_token"})["value"]
                print(f"Extracted CSRF Token: {csrf_token}")
                url="https://www.radionrjfm.com/pvote"
                res=session.get('https://www.radionrjfm.com/pvote')

                xtoken=res.cookies.get_dict()['XSRF-TOKEN']
                web_session=res.cookies.get_dict()['webground_session']
                headers = {
                    "authority": "www.radionrjfm.com",
                    "method": "POST",
                    "path": "/pvote",
                    "scheme": "https",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-encoding": "gzip, deflate, br, zstd",
                    "accept-language": "en-US,en;q=0.9",
                    "cache-control": "max-age=0",
                    "content-type": "application/x-www-form-urlencoded",
                    "cookie": f"XSRF-TOKEN={xtoken}; webground_session={web_session}",
                    "origin": "https://www.radionrjfm.com",
                    "referer": "https://www.radionrjfm.com/vote/5",
                    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": random.choice(USER_AGENTS),
                    "X-XSRF-TOKEN": xtoken  # Including XSRF token in headers
                }
                payload = {
            "gidvnrj": "5",
                "sex": "1",
                "age": "3",
                "_token": csrf_token,  # Use the extracted token
                "answers[450]": "1"
                        }
                res2=session.post(url,headers=headers,data=payload)
                print(res2.text)
        except :
            time.sleep(3)
        time.sleep(20)
    return JsonResponse({'status':'done'})
    # O9B2MGLWFErMmu0xj0k3E95zQe4LKm15bXfx7rI0