from django.contrib import admin
from .models import Course
from django.utils.html import format_html

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    def Thumbmail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50%" />'.format(object.image.url))
    list_display = ('id','Thumbmail','course_title','description')
    list_display_links = ('id','Thumbmail','course_title')

admin.site.register(Course, CourseAdmin)
