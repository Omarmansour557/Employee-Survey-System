from dataclasses import fields
from django.contrib import admin
from .models import Employee
from django import forms
# Register your models here.

class EmployeeForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(queryset=Employee.objects.all())    


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['employees'].required = False

        if self.instance.id:
            self.fields['employees'].initial = self.instance.children

 
    def save(self, commit=True):
        # NOTE: Previously assigned Parents are silently reset

        instance = super(EmployeeForm, self).save(commit=False)
        if commit:
            if instance.id:
                # set parent = None for the previous employees
                self.fields['employees'].initial.update(parent = None)
                
                # set parent = current instance for the newly chosen employees
                self.cleaned_data['employees'].update(parent=instance)
            
            super(EmployeeForm, self).save()
        else:
            return instance


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    readonly_fields = ['id']
    list_display = ['id', 'name']

