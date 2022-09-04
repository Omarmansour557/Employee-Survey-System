from dataclasses import fields
from django.contrib import admin
from .models import Employee
from django import forms
# Register your models here.

class EmployeeForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(queryset=Employee.objects.all())    


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        
        if self.instance:
            self.fields['employees'].initial = self.instance.employees.all()
            self.fields['employees'].required = False
 
    def save(self, *args, **kwargs):
        # FIXME: 'commit' argument is not handled
        # TODO: Wrap reassignments into transaction
        # NOTE: Previously assigned Foos are silently reset

        instance = super(EmployeeForm, self).save(commit=False)
        
        if instance.id != None:
            # set parent = None for the previous employees
            self.fields['employees'].initial.update(parent = None)
            
            # set parent = current instance for the newly chosen employees
            self.cleaned_data['employees'].update(parent=instance)
            
        instance.save()
        
        return instance


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    readonly_fields = ['id']

