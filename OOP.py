import random


class Name:
    def __init__(self, name):
        self.name = name


class ID:
    def __init__(self, id):
        self.id = id

    def get_info(self):
        print(f"ID: {self.id}")


class Employee(Name, ID):
    def __init__(self, id, name, gender, branch_id, is_busy=False):
        Name.__init__(self, name)
        ID.__init__(self, id)
        self.gender = gender
        self.branch_id = branch_id
        self.is_busy = is_busy

    def get_info(self):
        print("About employee:")
        print(f"Name: {self.name}, Branch ID: {self.branch_id}, Is busy: {self.is_busy}")

    def change_status(self, is_busy):
        self.is_busy = is_busy

    @staticmethod
    def employee_added_message():
        print("An employee is added successfully")


class Branch(Name, ID):
    def __init__(self, id, name):
        Name.__init__(self, name)
        ID.__init__(self, id)


class Order(Name, ID):
    def __init__(self, id, name, cost, branch, employees):
        Name.__init__(self, name)
        ID.__init__(self, id)
        self.__cost = cost
        self.branch = branch
        self.employees = employees
        self.completed = False

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def complete_order(self):
        print(f"Completing order {self.name}...")
        for employee in self.employees:
            employee.change_status(False)
        self.completed = True
        print(f"Order {self.name} is completed. Employees are now free.")

    def get_info(self):
        print(f"Order ID: {self.id}, Name: {self.name}, Cost: {self.__cost}")
        print(f"Branch: {self.branch.name}")
        print(f"Employees working on this order:")
        for emp in self.employees:
            emp.get_info()


class System:
    def __init__(self):
        self.employees = [
            Employee(1, "Eric Johnson", "Male", 1),
            Employee(2, "Jack Smith", "Female", 2),
            Employee(3, "Mary Manfrotto", "Female", 3),
            Employee(4, "Anna Taylor", "Female", 1)
        ]
        self.branches = [
            Branch(1, "Branch 1"),
            Branch(2, "Branch 2"),
            Branch(3, "Branch 3")
        ]
        self.orders = []

    def find_available_employees(self, branch_id):
        available_employees = [emp for emp in self.employees if emp.branch_id == branch_id and not emp.is_busy]
        return available_employees

    def create_order(self, order_name, branch_id, cost):
        available_employees = self.find_available_employees(branch_id)
        if available_employees:
            selected_employees = random.sample(available_employees, min(len(available_employees), 2))
            for emp in selected_employees:
                emp.change_status(True)
            order = Order(len(self.orders) + 1, order_name, cost, self.branches[branch_id - 1], selected_employees)
            self.orders.append(order)
            print(f"Order '{order_name}' created successfully.")
            order.get_info()
        else:
            print(f"No available employees in Branch {branch_id}")

    def complete_order(self, order_id):
        order = next((o for o in self.orders if o.id == order_id), None)
        if order and not order.completed:
            order.complete_order()
        else:
            print(f"Order with ID {order_id} not found or already completed.")

    def add_employee(self, name, gender, branch_id):
        new_id = len(self.employees) + 1
        new_employee = Employee(new_id, name, gender, branch_id)
        self.employees.append(new_employee)
        new_employee.employee_added_message()

    def add_branch(self, branch_name):
        new_id = len(self.branches) + 1
        new_branch = Branch(new_id, branch_name)
        self.branches.append(new_branch)
        print(f"Branch '{branch_name}' added successfully.")

    def change_employee_status(self, employee_id, is_busy):
        employee = next((emp for emp in self.employees if emp.id == employee_id), None)
        if employee:
            employee.change_status(is_busy)
            print(f"Employee {employee.name} status changed to {'busy' if is_busy else 'not busy'}.")
        else:
            print(f"Employee with ID {employee_id} not found.")


def admin_interaction(system):
    while True:
        print("What would you like to do?")
        print("1. Add an employee \n2. Add a branch \n3. Change employee's status \n4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter the employee's name: ")
            gender = input("Enter the employee's gender (Male/Female): ")
            branch_id = int(input("Enter the branch ID where the employee will work: "))
            system.add_employee(name, gender, branch_id)
        elif choice == "2":
            branch_name = input("Enter the name of the new branch: ")
            system.add_branch(branch_name)
        elif choice == "3":
            employee_id = int(input("Enter the employee's ID: "))
            status = input("Is the employee busy? (y/n): ")
            is_busy = True if status.lower() == 'y' else False
            system.change_employee_status(employee_id, is_busy)
        elif choice == "4":
            print("Exiting admin panel.")
            break
        else:
            print("Invalid choice. Please try again.")


def customer_interaction(system):
    string = input("Register your name: ")
    if string != "Admin":
        ans = input(f"Hello, {string}! Would you like to make an order? (y/n) ")
        if ans == "n":
            return
        elif ans == "y":
            print("Please specify your order:")
            order_name = input("1. Change window \n2. Paint walls \n3. Replace floor \n4. Place new furniture")
            cost = random.randint(100, 1000)
            branch_mapping = {
                "1": 1,  # Branch 1 for "Change window"
                "2": 2,  # Branch 2 for "Paint walls"
                "3": 1,  # Branch 1 for "Replace floor"
                "4": 2,  # Branch 2 for "Place new furniture"
            }
            branch_id = branch_mapping.get(order_name, 3)
            system.create_order(order_name, branch_id, cost)
    else:
        password = input("Enter password: ")
        if password == "pass123s14D10":
            admin_interaction(system)
        else:
            print("Incorrect password.")


system = System()
customer_interaction(system)
