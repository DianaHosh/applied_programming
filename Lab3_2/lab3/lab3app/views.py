from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view  # для @api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from .models import *
from django.http import Http404
from .serializers import (
    MaterialSerializer,
    SupplierSerializer,
    BranchSerializer,
    EmployeeSerializer,
    EmployeePositionSerializer,
    EmployeeSalaryHistorySerializer,
    CustomerSerializer,
    CustomerOrderSerializer,
    OrderMaterialSerializer,
    TypeOfWorkSerializer,
)

def index(request):
    return HttpResponse("Hello, world. You're at the lab3 index.")


@api_view(['GET'])
def getData(request):
    array = {
        'link1':'cool',
        'link2':'nice',
        'link3':'wow',
    }
    return Response(array)


class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeeDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return Employee.objects.get(employee_id=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#########################################


class MaterialList(APIView):
    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data)


class MaterialDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return Material.objects.get(material_id=pk)
        except Material.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        material = self.get_object(pk)
        serializer = MaterialSerializer(material)
        return Response(serializer.data)

    def put(self, request, pk):
        material = self.get_object(pk)
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        material = self.get_object(pk)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MaterialCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##################


class SupplierList(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)


class SupplierDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return Supplier.objects.get(supplier_id=pk)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def put(self, request, pk):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        supplier = self.get_object(pk)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SupplierCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

####################


class BranchList(APIView):
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)


class BranchDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return Branch.objects.get(branch_id=pk)
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        branch = self.get_object(pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    def put(self, request, pk):
        branch = self.get_object(pk)
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        branch = self.get_object(pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BranchCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##########################


class EmployeePositionList(APIView):
    def get(self, request):
        positions = EmployeePosition.objects.all()
        serializer = EmployeePositionSerializer(positions, many=True)
        return Response(serializer.data)


class EmployeePositionDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return EmployeePosition.objects.get(position_id=pk)
        except EmployeePosition.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        position = self.get_object(pk)
        serializer = EmployeePositionSerializer(position)
        return Response(serializer.data)

    def put(self, request, pk):
        position = self.get_object(pk)
        serializer = EmployeePositionSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        position = self.get_object(pk)
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeePositionCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = EmployeePositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#################


class EmployeeSalaryHistoryList(APIView):
    def get(self, request):
        histories = EmployeeSalaryHistory.objects.all()
        serializer = EmployeeSalaryHistorySerializer(histories, many=True)
        return Response(serializer.data)
    

class EmployeeSalaryHistoryDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return EmployeeSalaryHistory.objects.get(history_id=pk)
        except EmployeeSalaryHistory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        history = self.get_object(pk)
        serializer = EmployeeSalaryHistorySerializer(history)
        return Response(serializer.data)

    def put(self, request, pk):
        history = self.get_object(pk)
        serializer = EmployeeSalaryHistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        history = self.get_object(pk)
        history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeSalaryHistoryCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = EmployeeSalaryHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##################


class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class CustomerDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return Customer.objects.get(customer_id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#####################


class CustomerOrderList(APIView):
    def get(self, request):
        orders = CustomerOrder.objects.all()
        serializer = CustomerOrderSerializer(orders, many=True)
        return Response(serializer.data)


class CustomerOrderDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return CustomerOrder.objects.get(order_id=pk)
        except CustomerOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = CustomerOrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = CustomerOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerOrderCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = CustomerOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################

class OrderMaterialList(APIView):
    def get(self, request):
        order_materials = OrderMaterial.objects.all()
        serializer = OrderMaterialSerializer(order_materials, many=True)
        return Response(serializer.data)


class OrderMaterialDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return OrderMaterial.objects.get(order_id=pk)
        except OrderMaterial.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order_material = self.get_object(pk)
        serializer = OrderMaterialSerializer(order_material)
        return Response(serializer.data)

    def put(self, request, pk):
        order_material = self.get_object(pk)
        serializer = OrderMaterialSerializer(order_material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order_material = self.get_object(pk)
        order_material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderMaterialCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = OrderMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######################

class TypeOfWorkList(APIView):
    def get(self, request):
        works = TypeOfWork.objects.all()
        serializer = TypeOfWorkSerializer(works, many=True)
        return Response(serializer.data)


class TypeOfWorkDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_object(self, pk):
        try:
            return TypeOfWork.objects.get(work_id=pk)
        except TypeOfWork.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        work = self.get_object(pk)
        serializer = TypeOfWorkSerializer(work)
        return Response(serializer.data)

    def put(self, request, pk):
        work = self.get_object(pk)
        serializer = TypeOfWorkSerializer(work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        work = self.get_object(pk)
        work.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TypeOfWorkCreate(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        serializer = TypeOfWorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#############
