from rest_framework import generics
from rest_framework import viewsets

from .serializers import PersonaSerializer
from apps.servicios.models import Persona

class PersonaViewSet(viewsets.ModelViewset):
    queryset = Persona.objects.all()
    serializer_class =PersonaSerializer

#https://www.youtube.com/watch?v=RQGmkG8Xb6w&t=320s
