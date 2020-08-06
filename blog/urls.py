from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.button),
    path('output_en', views.randomizer_en, name="randomizer_en" ),
    path('output_es', views.randomizer_es, name="randomizer_es" ),
    path('output_it', views.randomizer_it, name="randomizer_it" ),
]