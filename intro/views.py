from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('Hello world!')
