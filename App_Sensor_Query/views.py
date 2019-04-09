from django.shortcuts import render, HttpResponse, redirect, Http404
from django.views import View
from App_Sensor_Query import models
from App_User_Control import models as app_modles
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.urls import reverse
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage


# Create your views here.
class DeviceSearchResult(LoginRequiredMixin, View):

    def get(self, request):
        dev_id = request.GET.get('query_text')
        print(dev_id)
        if dev_id:
            # add the query text to "user search history"
            self.add_history(dev_id)

            result = models.AwareDevice.objects.filter(device_id__contains=dev_id)

            return render(request, 'devices.html', {'result_dic': result})

        else:
            return redirect('homepage')

    # add the query text to "user search history"
    def add_history(self, content):
        app_modles.SearchHistory.objects.create(
            user=self.request.user,
            search_text=content,
            search_time=datetime.datetime.now()
        )


class TablesInDevice(LoginRequiredMixin, View):

    def get(self, request, device_id):

        result_list = []

        if device_id:
            models_list = apps.all_models['App_Sensor_Query']
            exclude_table = ["mqtthistory", "aware_device"]
            for table_name, model_class in models_list.items():
                if table_name not in exclude_table:
                    count = model_class.objects.filter(device_id=device_id).count()
                    # print(type(model_class))
                    temp_dic = {
                        "tab": table_name,
                        "num": count,
                    }
                    result_list.append(temp_dic)

            result_dic = {
                "device_id": device_id,
                "table_list": result_list
            }

            return render(request, 'tables_in_device.html', {'result_dic': result_dic})

        else:
            return Http404


class RecordsInTable(LoginRequiredMixin, View):

    def get(self, request, device_id, table_name, page_num=1):

        print(page_num)
        models_list = apps.all_models['App_Sensor_Query']
        for tableName, modelClass in models_list.items():
            if table_name == tableName:
                result = modelClass.objects.filter(device_id=device_id).values().order_by('field_id')
        paginator = Paginator(result, 10)
        # print(request.path)
        currentURL = reverse('recordsInTable', args=(device_id, table_name))
        # print(currentURL)

        try:
            content = paginator.page(page_num)
        except PageNotAnInteger:
            # if page_num is not a int, return to page=1
            content = paginator.page(1)
        except EmptyPage:
            # if page_num is not in valid range, return to page=lastNum
            content = paginator.page(paginator.num_pages)

        result_dic = {
            "currentURL": currentURL,
            "content": content,
            "device":device_id,
            "table":table_name,
        }

        # return HttpResponse(result_dic)
        return render(request,'paging_results_in_table.html', {'result_dic':result_dic})

