from abc import ABC, abstractmethod


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