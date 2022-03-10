from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Create your views here.

def meu_html(request):
    return render(request, 'juquinha/index.html')
    #return render(request, 'ajuda/index.html')