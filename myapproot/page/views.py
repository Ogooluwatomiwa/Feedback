from django.shortcuts import render, redirect
from .forms import PageForm
from .models import Page
#from django.http import HttpResponse
# Create your views here.


def page(request):
    form = PageForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'base.html', context)
