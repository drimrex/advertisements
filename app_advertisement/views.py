from django.http import HttpResponse
from django.shortcuts import render

def index(reqest):
    return render(reqest,'index.html')
# Create your views here.

def top_sellers(reqest):
    return render(reqest,'top-sellers.html')