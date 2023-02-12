from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateApiView(mixins.CreateModelMixin, GenericViewSet):
    """
    Only POST method
    """

    pass


class ListApiView(mixins.ListModelMixin, GenericViewSet):
    """
    Only GET method
    """

    pass


class RetrieveApiView(mixins.RetrieveModelMixin, GenericViewSet):
    """
    Only GET with id method
    """

    pass


class DestroyApiView(mixins.DestroyModelMixin, GenericViewSet):
    """
    Only DELETE method
    """

    pass


class UpdateApiView(mixins.UpdateModelMixin, GenericViewSet):
    """
    PUT & PATCH methods
    """

    pass
