from django.shortcuts import render,redirect
from notes.models import Student

def my_view(request):
    name=""
    role_number=0
    email=""
    date=""
    time=""
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        role_number = data.get('role_number')
        email = data.get("email")
        date = data.get("date")
        time = data.get("time")

        Student.objects.create(name=name,role_number= role_number,
                                email=email,date=date,time=time)
        
    context = {
        "name":name,
        'role_number':role_number,
        'email':email,
        'date':date,
        'time':time
    }
    return render(request,"note_01.html", context)


def students_list(request):
    students = Student.objects.all()
    context = {
        "students":students
    }
    return render(request,"note_02.html",context)


def edit_student(request,id):
    student = Student.objects.get(id=id)
    

    if request.method == "POST":
        data = request.POST
        student_id = id
        student_name = data.get('name')
        student_role_number = data.get('role_number')
        student_email = data.get('email')
        student_date = data.get('date')
        student_time = data.get('time')

        student.name = student_name
        student.role_number = student_role_number
        student.email = student_email
        student.date = student_date
        student.time = student_time

        student.save()
        return redirect('/students_list/')
        context = {
        "students":[student]
            }
        
        return redirect('/my_view/')
     
    context = {"student":[student]}
    return render(request,'note_03.html',context)

def another_view(request):
    return render(request,'note_04.html')

def sematic_tags(request):
    return render(request,'note_05.html')

def html_06(request):
     

    return render(request,'note_06.html')
  