from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.button),
    path('output', views.randomizer, name="randomizer" ),
]

# urlpatterns = [

# url(r'^admin/', admin.site.urls),

# url(r'^$', ),

# url(r'^output', ),

# url(r'^external', views.external),

# ]