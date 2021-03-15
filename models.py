from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class tab_sol(models.Model):
    startdate = models.DateTimeField(auto_now_add=False, auto_now=False, null=False)   
    endate    = models.DateTimeField(auto_now_add=False, auto_now=False, null=False)
    jus       = models.CharField(max_length=500)
    created   = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    
class PatientBag(models.Model):
    cd_paciente    = models.IntegerField()
    nm_paciente    = models.CharField(max_length=200)    
    cd_atendimento = models.IntegerField()
    cd_pre_med     = models.IntegerField()
    cd_etiqueta    = models.IntegerField(unique=True,blank=False,null=False)    
    created        = models.DateTimeField(auto_now_add=False, auto_now=True, blank=False)
    usuario        = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nm_paciente



   
