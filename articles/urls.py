from django.urls import path

from .views import *

urlpatterns = [
    path('', homeview, name='home'),
    path('about/', aboutview, name='about'),
    path('news/', newsview, name='news'),
    path('<int:pk>/', detailview, name='detail'),
    path('hodimlar/', hodim_view, name='hodim'),
    path('price/', price_about, name='prcie'),
]
