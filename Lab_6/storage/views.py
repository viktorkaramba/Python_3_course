from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Goods
from .forms import UserForm


# Create your views here.
def show(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            goods = Goods.objects.filter(id_se=form.cleaned_data['id_se'])
            print(form.cleaned_data['id_se'])
            context = {
                'goods': goods,
                'form': form,
                'error': error,
            }
            return render(request, 'index.html', context)
        else:
            error = 'Forms was incorrect'
    else:
        form = UserForm()
        goods = None
        context = {
            'goods': goods,
            'form': form,
            'error': error,
        }
        return render(request, 'index.html', context)
