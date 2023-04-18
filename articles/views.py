import re
from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import DetailView

from .models import *


def homeview(request):
    carusel_models = HomeCaruselModel.objects.all()
    future_model = FutureModels.objects.all()
    sub_models = SubMenuModels.objects.all()
    mainsite_models = MainSiteModels.objects.all()
    news_model = Newsmodel.objects.order_by('-date')
    paginator = Paginator(news_model, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'carusel_models': carusel_models,
        'future_model': future_model,
        'sub_models': sub_models,
        'mainsite_models': mainsite_models,
        'news_model': news_model,
        'page_obj': page_obj,

    }
    return render(request, 'home.html', context)


def aboutview(request):
    about_model = About.objects.all()
    about_maydon = AboutMaydon.objects.all()
    context = {
        'about_model': about_model,
        'about_maydon': about_maydon
    }
    return render(request, 'about.html', context)


def newsview(request):
    news_model = Newsmodel.objects.order_by('-date')
    news_price = NewsPrise.objects.all()
    paginator = Paginator(news_model, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tarjima = _("helo world")

    context = {
        'news_model': news_model,
        'news_price': news_price,
        'page_obj': page_obj,
        'tarjima': tarjima
    }
    return render(request, 'news.html', context)


def detailview(request, pk):
    news = Newsmodel.objects.get(id=pk)
    context = {
        'news': news
    }
    return render(request, 'detail.html', context)


def hodim_view(request):
    hodim_model = XodimModel.objects.all()
    context = {
        'hodim_model': hodim_model,
    }
    return render(request, 'team.html', context)


def price_about(request):
    context = {}
    return render(request, 'price.html')


def xujjat(request):
    xujjat = XujjatModel.objects.all()
    xujjatDetail = XujjatDetailModel.objects.all()

    context = {
        'xujjat': xujjat,
        'xujjatDetail': xujjatDetail
    }

    return render(request, 'price.html', context)