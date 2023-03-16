from django.contrib import admin
from tutorial.models import Tutorial, PremiumTutorial, Language, CommentTutorial

admin_classes = [Tutorial, PremiumTutorial, Language, CommentTutorial]

admin.site.register(admin_classes)
