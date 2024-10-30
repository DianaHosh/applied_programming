from django.contrib import admin

# Register your models here.
from .models import Branch, Employee, EmployeePosition, EmployeeSalaryHistory, Customer, CustomerOrder, Material, OrderMaterial, Supplier, TypeOfWork
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(EmployeePosition)
admin.site.register(EmployeeSalaryHistory)
admin.site.register(Customer)
admin.site.register(CustomerOrder)
admin.site.register(Material)
admin.site.register(OrderMaterial)
admin.site.register(Supplier)
# admin.site.register(SuppliesTo)
# admin.site.register(SuppliesWith)
admin.site.register(TypeOfWork)
