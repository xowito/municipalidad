from django.db import models

# Create your models here.
class agenda_semanal(models.Model):
    dia = models.CharField(max_length=25)

    def __str__(self):
        return self.dia
    
class hora(models.Model):
    tipo_visita = [('1','desparacitacion'),
                   ('2','consulta veterinaria'),
                   ('3','eutanasia')]
    
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, null=True)
    tipo_visita = models.CharField(max_length=1, choices=tipo_visita)
    agenda_semanal = models.ForeignKey(agenda_semanal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    