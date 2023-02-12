from itertools import cycle
from datetime import date
from model_bakery.recipe import Recipe, seq, foreign_key, related
from common.baker_recipes import custom_place, custom_disabled
from .models import Tutorial, PremiumTutorial, Language


lvl_options = ["S", "T"]
date_range = (date(2023, 1, 1), date(2024, 2, 2))

custom_language = Recipe(Language, name=seq("polish"))
custom_tutorial = Recipe(
    Tutorial,
    name=seq("course"),
    date=date_range,
    price=50,
    description=seq("Lorem ipsum"),
    scope=seq("Lorem ipsum"),
    lvl=cycle(lvl_options),
    essential=seq("Lorem ipsum"),
    learning_form=seq("Lorem ipsum"),
    homework=True,
    status=True,
    place=related(custom_place),
    support_disabled=related(custom_disabled),
    language=related(custom_language),
)
custom_premium_tutorial = Recipe(
    PremiumTutorial, status=True, tutorial=foreign_key(custom_tutorial)
)
