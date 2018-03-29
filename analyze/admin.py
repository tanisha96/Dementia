from django.contrib import admin

# Register your models here.
from .models import data1,data2,undata2,Patient,Myuser
admin.site.register(data1)
admin.site.register(data2)
admin.site.register(undata2)
admin.site.register(Patient)
admin.site.register(Myuser)



