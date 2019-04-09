"""ProjectDemo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from App_User_Control import views as user_view
from App_Sensor_Query import views as sensor_view
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', user_view.Homepage.as_view(), name='homepage'),
    path('patient/<int:patient_id>',user_view.Patient.as_view(),name='patient'),
    # path('logout/', user_view.Homepage.as_view(), name='logout'),
    # path('profile/', user_view.Homepage.as_view(), name='edit_profile'),
    # path('login/', user_view.Login.as_view(),name='login'),
    # path('register/', user_view.Register.as_view(),name='register'),
    # path('reset_password/',user_view.ResetPassword.as_view(),name='reset_password'),
    path('devices/',sensor_view.DeviceSearchResult.as_view(),name='devices'),
    path('devices/<device_id>/', sensor_view.TablesInDevice.as_view(), name='tablesInDevice'),
    path('devices/<device_id>/<table_name>/',sensor_view.RecordsInTable.as_view(),name='recordsInTable'),
    path('devices/<device_id>/<table_name>/<int:page_num>/',sensor_view.RecordsInTable.as_view(),name="recordsInTable_pageNum"),
    #Django user account urls
    path('accounts/', include('django.contrib.auth.urls')),
    #set the root URL to /homepage/
    path('', RedirectView.as_view(url='/homepage/')),
]
