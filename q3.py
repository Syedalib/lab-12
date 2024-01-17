class Employee:
    def __init__(self, employee_id, name, title):
        self.employee_id = employee_id
        self.name = name
        self.title = title
        self.subordinates = []

class OrganizationTree:
    def __init__(self):
        self.root = None
        self.employee_map = {}

    def add_employee(self, employee_id, name, title, supervisor_id=None):
        employee = Employee(employee_id, name, title)
        self.employee_map[employee_id] = employee

        if supervisor_id is None:
            self.root = employee
        else:
            supervisor = self.employee_map.get(supervisor_id)
            if supervisor:
                supervisor.subordinates.append(employee)
            else:
                raise ValueError("Supervisor not found.")

    def find_supervisor(self, employee_id):
        employee = self.employee_map.get(employee_id)
        if employee and employee != self.root:
            return self._find_supervisor(self.root, employee)
        else:
            return None

    def _find_supervisor(self, current_employee, target_employee):
        if target_employee in current_employee.subordinates:
            return current_employee

        for subordinate in current_employee.subordinates:
            result = self._find_supervisor(subordinate, target_employee)
            if result:
                return result

        return None

    def get_subordinates(self, employee_id):
        employee = self.employee_map.get(employee_id)
        if employee:
            return employee.subordinates
        else:
            return []


org_tree = OrganizationTree()


org_tree.add_employee(1, "Syed ali", "CEO")
org_tree.add_employee(2, "Safee", "CTO", supervisor_id=1)
org_tree.add_employee(3, "Sheryar", "Software Engineer", supervisor_id=2)
org_tree.add_employee(4, "Zeshan", "HR Manager", supervisor_id=1)

print("Supervisor of Sheryar:", org_tree.find_supervisor(3).name)
print("Subordinates of Safee:")
for subordinate in org_tree.get_subordinates(2):
    print(subordinate.name)
