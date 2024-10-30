# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from abc import ABC, abstractmethod


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(unique=True, max_length=40)
    manager = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch'


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


class EmployeePosition(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'employee_position'


class EmployeeSalaryHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    salary_change_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_salary_history'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=40)
    customer_email = models.CharField(max_length=40)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    work = models.ForeignKey('TypeOfWork', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_order'


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(unique=True, max_length=20)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material'


class OrderMaterial(models.Model):
    order = models.OneToOneField(CustomerOrder, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, material_id) found, that is not supported. The first column is selected.
    material = models.ForeignKey(Material, models.DO_NOTHING)
    quantity_used = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_material'
        unique_together = (('order', 'material'),)


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class SuppliesTo(models.Model):
    supplier = models.OneToOneField(Supplier, models.DO_NOTHING, primary_key=True)  # The composite primary key (supplier_id, branch_id) found, that is not supported. The first column is selected.
    branch = models.ForeignKey(Branch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supplies_to'
        unique_together = (('supplier', 'branch'),)


class SuppliesWith(models.Model):
    supplier = models.OneToOneField(Supplier, models.DO_NOTHING, primary_key=True)  # The composite primary key (supplier_id, material_id) found, that is not supported. The first column is selected.
    material = models.ForeignKey(Material, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'supplies_with'
        unique_together = (('supplier', 'material'),)


class TypeOfWork(models.Model):
    work_id = models.AutoField(primary_key=True)  # The composite primary key (work_id, branch_id) found, that is not supported. The first column is selected.
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    work_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'type_of_work'
        unique_together = (('work_id', 'branch'),)


###########################
class IRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class EmployeeRepository(IRepository):
    def get_all(self):
        return Employee.objects.all()

    def get_by_id(self, employee_id):
        try:
            return Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            return None

    def add(self, employee_data):
        employee = Employee(**employee_data)
        employee.save()
        return employee

    def update(self, employee_id, updated_data):
        employee = self.get_by_id(employee_id)
        if employee:
            for field, value in updated_data.items():
                setattr(employee, field, value)
            employee.save()
        return employee

    def delete(self, employee_id):
        employee = self.get_by_id(employee_id)
        if employee:
            employee.delete()


class EmployeePositionRepository(IRepository):
    def get_all(self):
        return EmployeePosition.objects.all()

    def get_by_id(self, position_id):
        try:
            return EmployeePosition.objects.get(pk=position_id)
        except EmployeePosition.DoesNotExist:
            return None

    def add(self, position_data):
        position = EmployeePosition(**position_data)
        position.save()
        return position

    def update(self, position_id, updated_data):
        position = self.get_by_id(position_id)
        if position:
            for field, value in updated_data.items():
                setattr(position, field, value)
            position.save()
        return position

    def delete(self, position_id):
        position = self.get_by_id(position_id)
        if position:
            position.delete()


class EmployeeSalaryHistoryRepository(IRepository):
    def get_all(self):
        return EmployeeSalaryHistory.objects.all()

    def get_by_id(self, history_id):
        try:
            return EmployeeSalaryHistory.objects.get(pk=history_id)
        except EmployeeSalaryHistory.DoesNotExist:
            return None

    def add(self, history_data):
        history = EmployeeSalaryHistory(**history_data)
        history.save()
        return history

    def update(self, history_id, updated_data):
        history = self.get_by_id(history_id)
        if history:
            for field, value in updated_data.items():
                setattr(history, field, value)
            history.save()
        return history

    def delete(self, history_id):
        history = self.get_by_id(history_id)
        if history:
            history.delete()


class BranchRepository(IRepository):
    def get_all(self):
        return Branch.objects.all()

    def get_by_id(self, branch_id):
        try:
            return Branch.objects.get(pk=branch_id)
        except Branch.DoesNotExist:
            return None

    def add(self, branch_data):
        branch = Branch(**branch_data)
        branch.save()
        return branch

    def update(self, branch_id, updated_data):
        branch = self.get_by_id(branch_id)
        if branch:
            for field, value in updated_data.items():
                setattr(branch, field, value)
            branch.save()
        return branch

    def delete(self, branch_id):
        branch = self.get_by_id(branch_id)
        if branch:
            branch.delete()


class CustomerRepository(IRepository):
    def get_all(self):
        return Customer.objects.all()

    def get_by_id(self, customer_id):
        try:
            return Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            return None

    def add(self, customer_data):
        customer = Customer(**customer_data)
        customer.save()
        return customer

    def update(self, customer_id, updated_data):
        customer = self.get_by_id(customer_id)
        if customer:
            for field, value in updated_data.items():
                setattr(customer, field, value)
            customer.save()
        return customer

    def delete(self, customer_id):
        customer = self.get_by_id(customer_id)
        if customer:
            customer.delete()


class CustomerOrderRepository(IRepository):
    def get_all(self):
        return CustomerOrder.objects.all()

    def get_by_id(self, order_id):
        try:
            return CustomerOrder.objects.get(pk=order_id)
        except CustomerOrder.DoesNotExist:
            return None

    def add(self, order_data):
        order = CustomerOrder(**order_data)
        order.save()
        return order

    def update(self, order_id, updated_data):
        order = self.get_by_id(order_id)
        if order:
            for field, value in updated_data.items():
                setattr(order, field, value)
            order.save()
        return order

    def delete(self, order_id):
        order = self.get_by_id(order_id)
        if order:
            order.delete()


class MaterialRepository(IRepository):
    def get_all(self):
        return Material.objects.all()

    def get_by_id(self, material_id):
        try:
            return Material.objects.get(pk=material_id)
        except Material.DoesNotExist:
            return None

    def add(self, material_data):
        material = Material(**material_data)
        material.save()
        return material

    def update(self, material_id, updated_data):
        material = self.get_by_id(material_id)
        if material:
            for field, value in updated_data.items():
                setattr(material, field, value)
            material.save()
        return material

    def delete(self, material_id):
        material = self.get_by_id(material_id)
        if material:
            material.delete()


class OrderMaterialRepository(IRepository):
    def get_all(self):
        return OrderMaterial.objects.all()

    def get_by_id(self, order_id):
        try:
            return OrderMaterial.objects.get(pk=order_id)
        except OrderMaterial.DoesNotExist:
            return None

    def add(self, order_material_data):
        order_material = OrderMaterial(**order_material_data)
        order_material.save()
        return order_material

    def update(self, order_id, updated_data):
        order_material = self.get_by_id(order_id)
        if order_material:
            for field, value in updated_data.items():
                setattr(order_material, field, value)
            order_material.save()
        return order_material

    def delete(self, order_id):
        order_material = self.get_by_id(order_id)
        if order_material:
            order_material.delete()


class SupplierRepository(IRepository):
    def get_all(self):
        return Supplier.objects.all()

    def get_by_id(self, supplier_id):
        try:
            return Supplier.objects.get(pk=supplier_id)
        except Supplier.DoesNotExist:
            return None

    def add(self, supplier_data):
        supplier = Supplier(**supplier_data)
        supplier.save()
        return supplier

    def update(self, supplier_id, updated_data):
        supplier = self.get_by_id(supplier_id)
        if supplier:
            for field, value in updated_data.items():
                setattr(supplier, field, value)
            supplier.save()
        return supplier

    def delete(self, supplier_id):
        supplier = self.get_by_id(supplier_id)
        if supplier:
            supplier.delete()


class SuppliesToRepository(IRepository):
    def get_all(self):
        return SuppliesTo.objects.all()

    def get_by_id(self, supplier_id):
        try:
            return SuppliesTo.objects.get(pk=supplier_id)
        except SuppliesTo.DoesNotExist:
            return None

    def add(self, supplies_to_data):
        supplies_to = SuppliesTo(**supplies_to_data)
        supplies_to.save()
        return supplies_to

    def update(self, supplier_id, updated_data):
        supplies_to = self.get_by_id(supplier_id)
        if supplies_to:
            for field, value in updated_data.items():
                setattr(supplies_to, field, value)
            supplies_to.save()
        return supplies_to

    def delete(self, supplier_id):
        supplies_to = self.get_by_id(supplier_id)
        if supplies_to:
            supplies_to.delete()


class SuppliesWithRepository(IRepository):
    def get_all(self):
        return SuppliesWith.objects.all()

    def get_by_id(self, supplier_id):
        try:
            return SuppliesWith.objects.get(pk=supplier_id)
        except SuppliesWith.DoesNotExist:
            return None

    def add(self, supplies_with_data):
        supplies_with = SuppliesWith(**supplies_with_data)
        supplies_with.save()
        return supplies_with

    def update(self, supplier_id, updated_data):
        supplies_with = self.get_by_id(supplier_id)
        if supplies_with:
            for field, value in updated_data.items():
                setattr(supplies_with, field, value)
            supplies_with.save()
        return supplies_with

    def delete(self, supplier_id):
        supplies_with = self.get_by_id(supplier_id)
        if supplies_with:
            supplies_with.delete()


class TypeOfWorkRepository(IRepository):
    def get_all(self):
        return TypeOfWork.objects.all()

    def get_by_id(self, work_id):
        try:
            return TypeOfWork.objects.get(pk=work_id)
        except TypeOfWork.DoesNotExist:
            return None

    def add(self, type_of_work_data):
        type_of_work = TypeOfWork(**type_of_work_data)
        type_of_work.save()
        return type_of_work

    def update(self, work_id, updated_data):
        type_of_work = self.get_by_id(work_id)
        if type_of_work:
            for field, value in updated_data.items():
                setattr(type_of_work, field, value)
            type_of_work.save()
        return type_of_work

    def delete(self, work_id):
        type_of_work = self.get_by_id(work_id)
        if type_of_work:
            type_of_work.delete()


# class Program:
#     def __init__(self):
#         self.employee_repo = EmployeeRepository()
#         self.position_repo = EmployeePositionRepository()
#         self.salary_history_repo = EmployeeSalaryHistoryRepository()
#         self.branch_repo = BranchRepository()
#         self.customer_repo = CustomerRepository()
#         self.customer_order_repo = CustomerOrderRepository()
#         self.material_repo = MaterialRepository()
#         self.order_material_repo = OrderMaterialRepository()
#         self.supplier_repo = SupplierRepository()
#         self.supplies_to_repo = SuppliesToRepository()
#         self.supplies_with_repo = SuppliesWithRepository()
#         self.type_of_work_repo = TypeOfWorkRepository()
# 
#     def print_options(self):
#         print("----- Options -----")
#         print("EMPLOYEE")
#         print("-- Employee")
#         print("-- Employee position")
#         print("-- Employee salary history")
#         print("BRANCH")
#         print("-- Branch")
#         print("SUPPLIER")
#         print("-- Supplies to")
#         print("-- Supplies with")
#         print("CUSTOMER")
#         print("-- Customer")
#         print("-- Customer order")
#         print("-- TypeOfWork")
#         print("MATERIAL")
#         print("-- Material")
#         print("-- Order material\n")
# 
#     def print_crud_options(self):
#         print("1. Select all")
#         print("2. Select one by ID")
#         print("3. Add")
#         print("4. Update")
#         print("5. Delete")
#         print("6. Exit")
# 
#     def run(self):
#         self.print_options()
#         entity = input("Choose an entity: ").strip().lower()
# 
#         repo = self.select_repository(entity)
# 
#         if repo is None:
#             print("Invalid entity selected.")
#             return
# 
#         self.print_crud_options()
#         action = int(input("Choose an action: "))
# 
#         if action == 1:
#             self.handle_select_all(repo)
#         elif action == 2:
#             self.handle_select_by_id(repo)
#         elif action == 3:
#             self.handle_add(repo)
#         elif action == 4:
#             self.handle_update(repo)
#         elif action == 5:
#             self.handle_delete(repo)
#         elif action == 6:
#             print("Exiting...")
#         else:
#             print("Invalid action selected.")
# 
#     def select_repository(self, entity):
#         repos = {
#             'employee': self.employee_repo,
#             'employee position': self.position_repo,
#             'employee salary history': self.salary_history_repo,
#             'branch': self.branch_repo,
#             'customer': self.customer_repo,
#             'customer order': self.customer_order_repo,
#             'material': self.material_repo,
#             'order material': self.order_material_repo,
#             'supplies to': self.supplies_to_repo,
#             'supplies with': self.supplies_with_repo,
#             'type of work': self.type_of_work_repo
#         }
#         return repos.get(entity)
# 
#     def handle_select_all(self, repo):
#         items = repo.get_all()
#         for item in items:
#             print(item)
# 
#     def handle_select_by_id(self, repo):
#         entity_id = input("Enter ID: ")
#         item = repo.get_by_id(entity_id)
#         if item:
#             print(item)
#         else:
#             print(f"Entity with ID {entity_id} not found.")
# 
#     def handle_add(self, repo):
#         data = {}
#         entity = repo.add(data)
#         print(f"Added: {entity}")
# 
#     def handle_update(self, repo):
#         entity_id = input("Enter ID to update: ")
#         data = {}
#         updated_entity = repo.update(entity_id, data)
#         if updated_entity:
#             print(f"Updated: {updated_entity}")
#         else:
#             print(f"Entity with ID {entity_id} not found.")
# 
#     def handle_delete(self, repo):
#         entity_id = input("Enter ID to delete: ")
#         repo.delete(entity_id)
#         print(f"Deleted entity with ID {entity_id}")