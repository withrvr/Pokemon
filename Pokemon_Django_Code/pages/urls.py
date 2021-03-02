from django.conf.urls import url
from django.urls import path
from .views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # home page
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),

    # info of pokemons and individual by id
    path(
        'info/pokemon/',
        pokemon_info_view,
        name='pokemon_info'
    ),

    path(
        'info/pokemon/<str:pokemon_id_from_url>/',
        pokemon_id_info_view,
        name='type_id_info'
    ),

    # path(
    #     'info/pokemon/<str:pokemon_name_from_url>/',
    #     pokemon_name_info_view,
    #     name='type_name_info'
    # ),

    # type of pokemon ( catagories ) like water, fire, grass, etc
    path(
        'info/type/',
        type_view,
        name='type'
    ),
    path(
        'info/type/<int:type_id_from_url>/',
        type_id_view,
        name='type_id_info'
    ),

]

urlpatterns += staticfiles_urlpatterns()
