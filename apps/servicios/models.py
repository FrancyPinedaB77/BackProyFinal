from django.db import models

class Persona(models.Model):
    cedula_id = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()

    def __unicode__(self):
        #return (self.cedula_id, self.nombre, self.edad)
        return u'{0}-{1}'.format(self.cedula_id, self.nombre, self.edad)

