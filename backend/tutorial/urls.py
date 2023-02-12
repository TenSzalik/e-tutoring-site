from rest_framework import routers
from .views import TutorialViewSet


router = routers.DefaultRouter()
router.register("", TutorialViewSet)
