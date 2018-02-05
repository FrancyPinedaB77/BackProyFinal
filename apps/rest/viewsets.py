from rest_framework import generics
from rest_framework import viewsets

from .serializers import PersonaSerializers
from apps.servicios.models import Persona


class PersonaViewSet (viewsets.ModelViewset):
    queryset = Persona.objects.all()
    serializer_class =