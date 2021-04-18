from django.contrib import admin
from .models import PortFolio
from django.utils.html import format_html

# Register your models here.
class PortFolioAdmin(admin.ModelAdmin):
    def Thumbmail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50%" />'.format(object.image.url))
    list_display = ('id','Thumbmail','project_name','category')
    list_display_links = ('id','Thumbmail','project_name')

admin.site.register(PortFolio, PortFolioAdmin)