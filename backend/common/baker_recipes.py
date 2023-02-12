from model_bakery.recipe import Recipe, seq
from .models import Place, Disabled


custom_place = Recipe(Place, name=seq("place"))
custom_disabled = Recipe(Disabled, name=seq("disabled"))
