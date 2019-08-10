from django.contrib import admin
from first_app.models import AppRecords,Webpage,Topic

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AppRecords)
