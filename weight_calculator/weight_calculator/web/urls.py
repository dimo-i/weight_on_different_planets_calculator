from django.urls import path

from weight_calculator.web.views import calculate, index

urlpatterns = (
    path('', index, name='index'),
    path('weight_on_planet_calculator/', calculate, name='calculator'),
)