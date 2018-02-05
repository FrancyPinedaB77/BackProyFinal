from rest_framework import serializers
from apps.servicios.models import Persona

class PersonaSerializer(serializer.HyperlinkedModelSerializer):
    class Meta:
        model : Persona
        fields:('cedula_id', 'nombre','edad')