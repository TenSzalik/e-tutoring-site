from rest_framework.viewsets import ModelViewSet
from backend.viewsets import ReadApiView
from .models import Tutorial, Language
from .serializers import TutorialReadSerializer, TutorialCreateUpdateSerializer, LanguageSerializer


class LanguageViewSet(ReadApiView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class TutorialViewSet(ModelViewSet):
    queryset = Tutorial.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TutorialReadSerializer
        return TutorialCreateUpdateSerializer

    def perform_create(self, serializer):
        data = {"created_by": self.request.user}
        return serializer.save(**data)

    def perform_update(self, serializer):
        created_by = {"created_by": self.request.user}
        data = dict(created_by)
        return serializer.save(**data)
