import sqlite3
from Common.Repositories.iemployee_repository import IEmployeeRepository
from Common.Entities.employee import Employee

class SQLiteEmployeeRepository(IEmployeeRepository):
    def get_by_username_password(self,username:str,password:str):
        with sqlite3.connect("CoreBankingDB,db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
        Select ID
            , FirstName
            , LastName
            , NationalCode
            , Email
            , Username
            , EmployeeStatusID
            , RoleId
        From Employee
        Where Username = '{username}'
        AND Password = '{password}' """)
        data = cursor.fetchone()
        if data is None:
            return None
        employee = Employee(*data)
        return employee
