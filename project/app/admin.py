from django.contrib import admin
from .models import Student1Model
# Register your models here.

            # >>>>>>> method <<<<<<<<<
# admin.site.register(Student1Model)


            # >>>>>>> method <<<<<<<<<
# @admin.register(Student1Model)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id','stu1_name','stu1_email','stu1_mobile','stu1_city']


            # >>>>>>> method <<<<<<<<<
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stu1_name','stu1_email','stu1_mobile','stu1_city']
admin.site.register(Student1Model,StudentAdmin)