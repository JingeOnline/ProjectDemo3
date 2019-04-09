from django.shortcuts import render, HttpResponse, Http404,redirect
from django.views import View
from App_User_Control import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict

# Create your views here.
class Homepage(View):
    def get(self, request):

        if request.user.is_authenticated:
            search_history=models.SearchHistory.objects.filter(user=self.request.user).values().order_by("-search_time")
            patient_list=models.UserPatient.objects.filter(user=self.request.user).values("patient","patient__name","patient__device")
            # for item in patients:
            #     print (item)

            result_dic={
                "search_history":search_history,
                "patient_list":patient_list
            }

            return render(request, 'homepage.html',{"result_dic":result_dic})
        else:
            return render(request, 'homepage.html')


class Patient(LoginRequiredMixin, View):

    def get(self,request,patient_id):

        patient_infor=models.Patient.objects.get(id=patient_id)
        result_dic=model_to_dict(patient_infor)
        # print(result_dic)

        # return HttpResponse(patient_infor)
        return render(request,'patient.html',{"result_dic":patient_infor})

    def post(self,request,patient_id):
        # device_binding=request.POST.get('patient_device')
        # device_binding+=request.POST.get('patient_name')
        device_binding=request.POST.get('patient_device')
        # print("hello",device_binding)
        currentURL = request.path
        if device_binding:
            record = models.Patient.objects.get(id=patient_id)
            record.device = device_binding
            record.save()
            print('finish')

        return redirect(currentURL)
        # return HttpResponse(device_binding)