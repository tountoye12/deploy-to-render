from django.test import TestCase

from .models import Employee, EmployeeGroup

# Create your tests here.


class TestModels(TestCase):

    def test_employee(self):
        emp_groudId = EmployeeGroup.objects.create(name="QA")
        employee = Employee.objects.create(name="Test", company="IT",
                                       email="email@gmail.com",
                                       title="SDE",
                                       mobile="8939484",
                                       photo="eoeojd",
                                       employee_groudId = emp_groudId
                                       )
    
        self.assertEquals(str(employee), "Test")

        self.assertTrue(isinstance(employee, Employee))