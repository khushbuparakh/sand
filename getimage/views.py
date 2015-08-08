from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.template import RequestContext, loader
from lxml import html
import requests
import urlparse

def home(request):
    template = loader.get_template('home.html')
    c = {}
    h = {}
    z = []
    if request.POST:
        url = request.POST["url"]
        r = requests.get(url)
        tree = html.fromstring(r.text)
        c = tree.xpath('//img/@src')
        h = tree.xpath('//a/@href')
        for x in c:
            if bool(urlparse.urlparse(x).netloc):
                z.append(x)
            else:
                z.append(str(url) + str(x))

    return render_to_response("home.html", {'h': h, 'z' : z}, context_instance=RequestContext(request))