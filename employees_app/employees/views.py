import random

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from employees_app.employees.models import Department, Employee

"""
A Function is Django view if:
- accept request as first param:
- returns HttpResponse
"""


# Create your views here.
def home(request):
    html = f"{request.method}: This is home"
    if request.method == 'POST':
        return HttpResponse(
            html,
            status=201,
            content_type='text/plain',
            headers={
                'x-doncho-header': 'Django'
            }
        )
    else:
        print(reverse_lazy("index"))
        print(reverse_lazy("go to home"))
        print(reverse_lazy("list departments"))
        print(reverse_lazy("custom url"))
        print(reverse_lazy("department details", kwargs={
            'id': 5
        }))

        context = {
            "number": random.randint(0, 1024),
            "numbers": [random.randint(0, 1024) for _ in range(15)],
        }
        return render(request, 'index.html', content_type='text/html', context=context)


def not_found(request):
    return HttpResponseNotFound(request)


def go_to_home(request):
    return redirect('department details', id=516)


def department_details(request, id: int):
    return HttpResponse(f"This is department {id} details")


def list_department(request):
    # Create and insert record
    # department = Department(
    #     name=F'Department {random.randint(0, 1024)}'
    # )
    # department.save()
    #Department.objects.create(name=F'Department_created_ {random.randint(0, 1024)}')

    # Update department record
    # department = Department.objects.filter(name='Tv app').first()
    # department.name = 'Tv app 2'
    # department.save()

    context = {
        'departments': Department.objects.prefetch_related('employee_set').all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)

