from django.urls import path

from employees_app.employees.views import department_details, home, list_department, not_found, go_to_home

# App urls
urlpatterns = [
    path('<int:id>/', department_details, name='department details'),  # localhost:8000/departments/1  -> department_details
    path('', list_department, name='list departments'),       # localhost:8000/departments    -> list_department
    path('not-found/', not_found),
    path('go-to-home/', go_to_home),
    # path('departments/create', create_department),
    # path('departments/update', update_department),
    # path('departments/delete', delete_department),
]