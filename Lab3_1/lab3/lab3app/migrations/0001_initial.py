# Generated by Django 5.1.2 on 2024-10-29 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'branch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=40)),
                ('customer_email', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'customer_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
                ('employee_email', models.CharField(max_length=40, unique=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('position_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'employee_position',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeSalaryHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_change_date', models.DateField()),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'employee_salary_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('material_name', models.CharField(max_length=20, unique=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'material',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeOfWork',
            fields=[
                ('work_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'type_of_work',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderMaterial',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lab3app.customerorder')),
                ('quantity_used', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order_material',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuppliesTo',
            fields=[
                ('supplier', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lab3app.supplier')),
            ],
            options={
                'db_table': 'supplies_to',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuppliesWith',
            fields=[
                ('supplier', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lab3app.supplier')),
            ],
            options={
                'db_table': 'supplies_with',
                'managed': False,
            },
        ),
    ]
