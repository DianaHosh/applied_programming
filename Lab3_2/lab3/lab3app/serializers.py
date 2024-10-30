from rest_framework import serializers
from .models import (Employee, Material, Supplier, Branch, EmployeePosition, EmployeeSalaryHistory,
Customer, CustomerOrder, OrderMaterial, TypeOfWork)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'


class EmployeePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePosition
        fields = '__all__'


class EmployeeSalaryHistorySerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = EmployeeSalaryHistory
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    work = serializers.StringRelatedField()

    class Meta:
        model = CustomerOrder
        fields = '__all__'


class OrderMaterialSerializer(serializers.ModelSerializer):
    order = CustomerOrderSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = OrderMaterial
        fields = '__all__'


class TypeOfWorkSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = TypeOfWork
        fields = '__all__'
