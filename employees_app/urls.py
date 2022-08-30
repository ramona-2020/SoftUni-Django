from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home, department_details, list_department, go_to_home

# Project URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('go-to-home/', go_to_home, name='go to home'),
    path('inner/order_by/filers/one/two', go_to_home, name='custom url'),

    # Include URL configuration from employees_app
    path('departments/', include('employees_app.employees.urls'))
]
