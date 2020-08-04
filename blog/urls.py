from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.button),
    path('output', views.randomizer_en, name="randomizer_en" ),
    path('output', views.randomizer_es, name="randomizer_es" ),
    path('output', views.randomizer_it, name="randomizer_it" ),
]

# urlpatterns = [

# url(r'^admin/', admin.site.urls),

# url(r'^$', ),

# url(r'^output', ),

# url(r'^external', views.external),

# ]