from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests


# home page
def social_media_view(request, social_media_from_url, *args, **kwargs):
    # redirect to home page if any path not find
    # this one is for home page .... main page
    redirect_url = ''

    check_if_this_sm = ["youtube", "yt", "twitter",
                        "facebook", "instagram", "fb", "insta"
                        ]
    if social_media_from_url in check_if_this_sm:
        redirect_url = f"https://tapmybio.com/withrvr"

    return redirect(redirect_url)

# home page


def home_view(request, *args, **kwargs):
    context = {
        "title": "Home Page",
    }
    return render(request, 'pages/home_page.html', context)


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
    # add comman content here
    context = {
        "pokemon_id": pokemon_id_from_url,
    }

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

        context = {
            **context,

            "count": count,
            "title": f"No Pokemon with - ID (#{pokemon_id_from_url})",
        }

        return render(request, 'pages/info/no_pokemon_with_id.html', context)

    # name of pokemon
    name = pokemon["name"].capitalize()

    # context to go on templete
    context = {
        **context,

        "pokemon": pokemon,
        "name": name,
        "title": f"{ name } (#{ pokemon_id_from_url }) - Pokemon Info",
        "pokemon_id": pokemon_id_from_url,

        # foo-images-tag-more.html .... for more
        # official_artwork_image .... this work for all images of pokemon ....
        "official_artwork_image": pokemon["sprites"]["other"]["official-artwork"]["front_default"],

    }
    return render(request, 'pages/info/pokemon_id_info_page.html', context)


# name - pokemon - info
def pokemon_name_info_view(request, pokemon_name_from_url, *args, **kwargs):
    return redirect('https://www.google.com/')


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
