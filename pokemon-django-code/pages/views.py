from django.shortcuts import render
from django.http import HttpResponse
import requests


# home page
def home_view(request, *args, **kwargs):
    context = {
        "title": "Home Page",
    }
    return render(request, 'pages/home_page.html', )


# ------------------------ pokemon --------------------------------
# pokemon - info
def pokemon_info_view(request, *args, **kwargs):
    pokemons = requests.get("https://pokeapi.co/api/v2/pokemon/").json()
    context = {
        "title": "Pokemon - Info",
        "pokemons": pokemons["results"],
    }
    return render(request, 'pages/info/pokemon_info_page.html', context)


# id - pokemon - info
def pokemon_id_info_view(request, pokemon_id_from_url, *args, **kwargs):
    try:
        pokemon = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_from_url}/"
        ).json()

    except Exception as e:
        print(e)

        # to count number of pokemon ids there
        count = requests.get(
            f"https://pokeapi.co/api/v2/pokemon?offset=2000000"
        ).json()["count"]

        return HttpResponse(
            f"""
            <h4>&nbsp;</h4>
            <h4>No pokemon with --> <i>ID ( #{pokemon_id_from_url} ) </i></h4>
            <h4>There are in all --> { count } <-- pokemons</h4>
            <h4>but</h4>
            <h4>Pokemon id can be greater than or less than --> { count } <-- ... Okay</h4>

        """)

    # name of pokemon
    name = pokemon["name"].capitalize()

    # context to go on templete
    context = {

        "pokemon": pokemon,
        "name": name,
        "title": f"{ name } (#{ pokemon_id_from_url }) Pokemon Info",
        "pokemon_id": pokemon_id_from_url,

        # images-tag-more.html extra images is used then uncomment this variable
        "official_artwork_image": pokemon["sprites"]["other"]["official-artwork"]["front_default"],

    }
    return render(request, 'pages/info/pokemon_id_info_page.html', context)


# ------------------------ type --------------------------------
# type ( ex: water, fire, grass, etc ) - pokemon
def type_view(request, *args, **kwargs):
    types = requests.get(
        f"https://pokeapi.co/api/v2/type/"
    ).json()

    # context to go on templete
    context = {
        "title": "Types of Pokemon",
    }
    return HttpResponse("Types of Pokemon---under development")
    return render(request, 'pages/info/??.html', context)


# id - type ( ex: water, fire, grass, etc ) - pokemon
def type_id_view(request, type_id_from_url, *args, **kwargs):
    try:
        pokemon = requests.get(
            f"https://pokeapi.co/api/v2/type/{type_id_from_url}/"
        ).json()
    except Exception as e:
        count = requests.get(
            f"https://pokeapi.co/api/v2/type?limit=1&offset=50"
        ).json()["count"]

        return HttpResponse(
            f"""<h4>No Type with --> <i>ID #{type_id_from_url}</i></h4>
            Try some less <b>ID</b> Type because<br/>
            <h3>There are Type up Till --> <i>ID #{count}</i> only</h3>
        """)

    # context to go on templete
    context = {
        "title": "Type of Pokemon",
    }
    return HttpResponse("type id id id of pokemon")
    return render(request, 'pages/info/??.html', context)
