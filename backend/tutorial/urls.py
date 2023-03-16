from rest_framework import routers
from .views import LanguageViewSet, TutorialViewSet


router = routers.DefaultRouter()
router.register("language", LanguageViewSet)
router.register("", TutorialViewSet)
