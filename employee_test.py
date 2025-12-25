from Common.DTOs.response import Response
from Common.Entities.employee import Employee
from DataAccess.Repositories.SQLServer.sql_server_employee_repository import SQLServer
from BusinessLogic.employee_business_logic import EmployeeBusinessLogic
from unittest import TestCase


class EmployeeTest(TestCase):
    def test_success_login(self):
        repository = SQLServerEmployeeRepository("localhost","localhost")
        employee_business = EmployeeBusinessLogic(repository)
        response = employee_business.login("Donyakhabiri","newpass")
        self.assertIs(response,Response)
        self.assertEqual(response.success,True)
        self.assertIs(response.data,Employee)
    def test_failed_login(self):
        repository= SQLServerEmployeeRepository("localhost","localhost")
        employee_business = EmployeeBusinessLogic(repository)
        response = employee_business.login("Donyakhabiri", "newpass")
        self.assertIs(response,Response)
        self.assertEqual(response.success,False)
