from django.contrib import admin
from App_User_Control.models import Patient,SearchHistory,UserPatient

# Register your models here.
#把表格类注册到admin页面中
# admin.site.register(Users)
# admin.site.register(Patients)
admin.site.register(Patient)
admin.site.register(SearchHistory)
admin.site.register(UserPatient)