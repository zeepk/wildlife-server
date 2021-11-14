from rest_framework.permissions import IsAuthenticated
from wildlife.models import Critter
from rest_framework import viewsets
from .serializers import CritterSerializer
from .models import Critter, Caught


class CaughtViewSet(viewsets.ModelViewSet):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = CritterSerializer

    def get_queryset(self):
        return Caught.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

    # def perform_update(self, serializer):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object_or_none()
    #     serializer = self.get_serializer(
    #         instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)


class FishViewSet(viewsets.ModelViewSet):

    serializer_class = CritterSerializer

    queryset = Critter.objects.filter(critter_type=Critter.FISH)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class BugsViewSet(viewsets.ModelViewSet):

    serializer_class = CritterSerializer

    queryset = Critter.objects.filter(critter_type=Critter.BUG)


class SeaViewSet(viewsets.ModelViewSet):

    serializer_class = CritterSerializer

    queryset = Critter.objects.filter(critter_type=Critter.SEA)
