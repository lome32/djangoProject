from django.shortcuts import render
from django.http import HttpResponse
import datetime 
import logging 

 

logger = logging.getLogger(__name__) 

 

def welcome_page(request): 
    logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+ ' hours!') 
    return HttpResponse("<h1>Welcome to web application development course 2023 (URFU/RTF) :)</h1>") 