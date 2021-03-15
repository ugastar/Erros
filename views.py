from django.shortcuts import render
##from patientData.Form import PesquisForm
from patientData.models import *
from core.models import PatientBag

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
dados2 =[]

def buscarDados(request):
    context = {'codpremed': None, 'dadosPaciente': None, 'codetique': None}
    if request.method == "POST":
        codpremed = request.POST['codpremed']
        codetique = request.POST['codetique']
        #dadosPaciente = Atendime.objects.using('Oracle').filter(cd_atendimento=codpremed)
        ##dadosPaciente = Paciente.objects.using('Oracle').filter(cd_paciente=codpremed)
        ##dadosPaciente = Paciente.objects.using('Oracle').select_related('Atendime').get(cd_paciente=codpremed)
        #dadosPaciente = PreMed.objects.using('Oracle').filter(cd_pre_med=codpremed)
        dadosPaciente = PreMed.objects.using('Oracle').select_related('cd_atendimento').filter(cd_pre_med=codpremed)        
        dados2 = dadosPaciente
        #return HttpResponseRedirect(reverse('login') )
        context = {'codpremed': codpremed, 'dadosPaciente': dadosPaciente, 'codetique': codetique }
        return render(request, 'patientData.html', context)
    #return render(request, 'templates/patientData.html', {'dadosPaciente': dadosPaciente})         
    return render(request, 'patientData.html',context)


def cadastrarPaciente(request):
    #context = {'codpacient':None,'pacient':None,'codatendimento':None,'prescicao':None,'etiqueta':None,'usuario':None,'time':None}
    if request.method == "POST":
      
       cd_paciente = dados2.value_list('cd_paciente')      
       context = {'cd_paciente': cd_paciente}
    return render(request, 'patientData.html', cd_paciente )
    
    #PatientBag.objects.create(cd_paciente=dadosPaciente.cd_atendimento.cd_paciente.cd_paciente,
     #                         nm_paciente=dadosPaciente.cd_atendimento.cd_paciente.nm_paciente,
      #                        cd_atendimento=dadosPaciente.cd_atendimento.cd_atendimento,
       #                       cd_pre_med=dadosPaciente.cd_pre_med,
        #                      cd_etiqueta=dadosPaciente.codetique,
         #                     usuario=request.user)
         
     #return render(request, 'patientData.html', context)
                                                            
