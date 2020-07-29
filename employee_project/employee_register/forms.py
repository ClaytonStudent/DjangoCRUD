from django import forms
from .models import Employee
'''
Create Object EmployeeForm
'''
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # selet and rearrange the the fields in Employee
        fields = ('fullname','mobile','emp_code','position')
        # set label for fields
        labels = {
            'fullname':'Full Name',
            'emp_code': 'EMP_CODE'
        }
    # set default name of position to "Select"
    # set field emp_code not required
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='Select'
        self.fields['emp_code'].required = False