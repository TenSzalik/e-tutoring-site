from django.contrib import admin
from common.models import Place, Disabled, BaseComment, BaseStar

admin_classes = [Place, Disabled, BaseComment, BaseStar]

admin.site.register(admin_classes)
