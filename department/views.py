from django.shortcuts import render
from .models import department, department_message, department_images


def programsView(request):
    departments = department.objects.all()
    context = {'departments': departments}
    return render(request, 'admissions/programs.html', context)


def departmentView(request, dept_name, dept_id):
    deptmsg = department_message.objects.get(id=dept_id)
    deptimgs = department_images.objects.all()
    context = {
        'deptmsg': deptmsg,
        'deptimgs': deptimgs
    }

    return render(request, 'department.html', context)


def academicDepartmentView(request):
    departments = department.objects.all()
    context = {
        'depts': departments,
    }

    return render(request, 'academic.html', context)


def nonAcademicDepartmentView(request):
    departments = department.objects.all()
    context = {
        'depts': departments,

    }

    return render(request, 'non-academic.html', context)
