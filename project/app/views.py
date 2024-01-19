from django.shortcuts import render
from .models import Student1Model
# Create your views here.

def home(req):
    stu_data = Student1Model.objects.all()
    # stu_data = Student1Model.students.all()
    data = {
        'student':stu_data
    }
    return render(req,'home.html',data)