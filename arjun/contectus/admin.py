from django.contrib import admin
from contectus.models import Contectus
class ContectusAdmin(admin.ModelAdmin):
    list_display = ('name','email','massage')
admin.site.register(Contectus,ContectusAdmin)
# Register your models here.
