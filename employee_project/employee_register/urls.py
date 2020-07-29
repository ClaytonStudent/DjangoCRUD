from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),  # POST request: insert form
    path('list/', views.employee_list, name ='employee_list'), # GET request: show list
    path('<int:id>/',views.employee_form,name='employee_update'), # UPDATE request
    path('delete/<int:id>/',views.employee_delete,name='employee_delete') # DELETE request
]