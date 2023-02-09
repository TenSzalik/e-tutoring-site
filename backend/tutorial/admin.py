from django.contrib import admin
from tutorial.models import Tutorial, PremiumTutorial, Language

admin_classes = [Tutorial, PremiumTutorial, Language]

admin.site.register(admin_classes)
