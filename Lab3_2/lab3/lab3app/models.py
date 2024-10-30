from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from abc import ABC, abstractmethod


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(unique=True, max_length=20)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'material'

    def __str__(self):
        return self.material_name


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=40, blank=True, null=True)
    materials = models.ManyToManyField(Material, related_name='materials')

    class Meta:
        managed = True
        db_table = 'supplier'

    def __str__(self):
        return self.supplier_name


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(unique=True, max_length=40)
    suppliers = models.ManyToManyField(Supplier, related_name='branches')

    class Meta:
        managed = False
        db_table = 'branch'

    def __str__(self):
        return self.branch_name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    employee_email = models.CharField(unique=True, max_length=40)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey('EmployeePosition', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class EmployeePosition(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'employee_position'

    def __str__(self):
        return self.position_name

class EmployeeSalaryHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    salary_change_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_salary_history'
        unique_together = ('employee', 'salary_change_date')

    def __str__(self):
        return f'{self.employee.first_name} - {self.salary_change_date}'

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=40)
    customer_email = models.CharField(max_length=40)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.customer_name

class CustomerOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    work = models.ForeignKey('TypeOfWork', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_order'
        unique_together = (('customer', 'order_date'),)

    def __str__(self):
        return f'{self.customer.customer_name} - {self.order_date}'


class OrderMaterial(models.Model):
    order = models.OneToOneField(CustomerOrder, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, material_id) found, that is not supported. The first column is selected.
    material = models.ForeignKey(Material, models.DO_NOTHING)
    quantity_used = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_material'
        unique_together = (('order', 'material'),)

    def __str__(self):
        return self.material.material_name


class TypeOfWork(models.Model):
    work_id = models.AutoField(primary_key=True)  # The composite primary key (work_id, branch_id) found, that is not supported. The first column is selected.
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    work_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'type_of_work'
        unique_together = (('work_type', 'branch'),)

    def __str__(self):
        return f'{self.work_type} - {self.branch}'
