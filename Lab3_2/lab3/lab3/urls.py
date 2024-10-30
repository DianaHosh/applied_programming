"""lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from lab3app import views
from django.conf import settings
from lab3app.views import (EmployeeList, EmployeeDetail, EmployeeCreate,
                           MaterialList, MaterialDetail, MaterialCreate,
                           SupplierList, SupplierDetail, SupplierCreate,
                           BranchList, BranchDetail, BranchCreate,
                           EmployeePositionList, EmployeePositionDetail, EmployeePositionCreate,
                           EmployeeSalaryHistoryList, EmployeeSalaryHistoryDetail, EmployeeSalaryHistoryCreate,
                           CustomerList, CustomerDetail, CustomerCreate,
                           CustomerOrderList, CustomerOrderDetail, CustomerOrderCreate,
                           OrderMaterialList, OrderMaterialDetail, OrderMaterialCreate,
                           TypeOfWorkList, TypeOfWorkDetail, TypeOfWorkCreate)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', views.getData),
    path('api/drf-auth/', include('rest_framework.urls')),

    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreate.as_view(), name='employee-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),

    path('materials/', MaterialList.as_view(), name='material-list'),
    path('materials/create/', MaterialCreate.as_view(), name='material-create'),
    path('materials/<int:pk>/', MaterialDetail.as_view(), name='material-detail'),

    path('suppliers/', SupplierList.as_view(), name='supplier-list'),
    path('suppliers/create/', SupplierCreate.as_view(), name='supplier-create'),
    path('suppliers/<int:pk>/', SupplierDetail.as_view(), name='supplier-detail'),

    path('branches/', BranchList.as_view(), name='branch-list'),
    path('branches/create/', BranchCreate.as_view(), name='branch-create'),
    path('branches/<int:pk>/', BranchDetail.as_view(), name='branch-detail'),

    path('positions/', EmployeePositionList.as_view(), name='position-list'),
    path('positions/create/', EmployeePositionCreate.as_view(), name='position-create'),
    path('positions/<int:pk>/', EmployeePositionDetail.as_view(), name='position-detail'),

    path('salary_histories/', EmployeeSalaryHistoryList.as_view(), name='salary-history-list'),
    path('salary_histories/create/', EmployeeSalaryHistoryCreate.as_view(), name='salary-history-create'),
    path('salary_histories/<int:pk>/', EmployeeSalaryHistoryDetail.as_view(), name='salary-history-detail'),

    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/create/', CustomerCreate.as_view(), name='customer-create'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),

    path('orders/', CustomerOrderList.as_view(), name='order-list'),
    path('orders/create/', CustomerOrderCreate.as_view(), name='order-create'),
    path('orders/<int:pk>/', CustomerOrderDetail.as_view(), name='order-detail'),

    path('order_materials/', OrderMaterialList.as_view(), name='order-material-list'),
    path('order_materials/create/', OrderMaterialCreate.as_view(), name='order-material-create'),
    path('order_materials/<int:pk>/', OrderMaterialDetail.as_view(), name='order-material-detail'),

    path('works/', TypeOfWorkList.as_view(), name='work-list'),
    path('works/create/', TypeOfWorkCreate.as_view(), name='work-create'),
    path('works/<int:pk>/', TypeOfWorkDetail.as_view(), name='work-detail'),
]