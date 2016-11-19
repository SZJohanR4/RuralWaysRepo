from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse("priemera view")