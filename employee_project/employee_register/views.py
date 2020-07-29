from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    '''
    List all Employee stored in DB
    '''
    context = {'employee_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request, id=0):
    '''
    View for employee form
    Deal with all requests to employee form.
    Including GET and POST
    '''
    # when method is GET
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request,"employee_register/employee_form.html",{'form':form})
    
    # When method is POST/PUT
    else:
        # creat new form
        if id == 0:
            form = EmployeeForm(request.POST)
        # update an existing form
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid:
            form.save()
        return redirect('/employee/list')

def employee_delete(request,id=0):
    '''
    View for delete
    '''
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list') 
