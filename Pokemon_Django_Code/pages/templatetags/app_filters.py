from django import template
register = template.Library()


# {{ pokemon.height | convert_from_decimeter_to_feet_inches }}
# perform conversion
# decimeter -> feet inches
@register.filter(name='convert_from_decimeter_to_feet_inches')
def convert_from_decimeter_to_feet_inches(decimeter_value):
    inch = 0.3937 * decimeter_value * 10
    feet = 0.0328 * decimeter_value * 10
    return str(f'{feet:.2f}\' {inch:.2f}\" ')


# url_value content value likethis
# https://pokeapi.co/api/v2/pokemon/123/
# getting the end --> id <-- vaule of pokemon in templeate
@register.filter(name='get_pokemon_id_from_url_ending')
def get_pokemon_id_from_url_ending(url_value):
    return url_value.split("/")[-2]
