from wildlife.models import Critter
from rest_framework import viewsets
from .serializers import CritterSerializer
from .models import Critter


class FishViewSet(viewsets.ModelViewSet):

    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    serializer_class = CritterSerializer

    queryset = Critter.objects.filter(critter_type=Critter.FISH)


class BugsViewSet(viewsets.ModelViewSet):

    serializer_class = CritterSerializer

    queryset = Critter.objects.filter(critter_type=Critter.BUG)


class SeaViewSet(viewsets.ModelViewSet):

    serializer_class = CritterSerializer

    queryset = Critter.objects.filter(critter_type=Critter.SEA)
