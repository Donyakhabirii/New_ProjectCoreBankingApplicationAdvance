import pymssql
from Common.Repositories.iemployee_repository import IEmployeeRepository
from Common.Entities.employee import Employee


class SQLServerEmployeeRepository(IEmployeeRepository):
    def create_connection(self):
        connection =  pymssql.connect(host="localhost",database="corebankingDB")
        return connection
    def get_by_username_password(self,username:str,password:str):
        with self.create_connection() as connection:
            cursor = connection.cursor(as_dict = True)
            cursor.execute("""
            Select ID
            ,	   FirstName
            ,		LastName
            ,		NationalCode
            ,		Email
            ,		Username AS UserName
            ,		EmployeeStatusID AS EmployeeStatusID
            ,		RoleId
            FROM Employee
            Where Username = %s
            And  Password = %s""",(username,password))
            data = cursor.fetchone()
            if not data:
                return None
            try:
                return Employee.create_with_dict(data)
            except Exception:
                return Employee(
                    data.get("ID"),
                    data.get("FirstName"),
                    data.get("LastName"),
                    data.get("NationalCode"),
                    data.get("Email"),
                    data.get("UserName") or data.get("Username"),
                    data.get("EmployeeStatusID"),
                    data.get("RoleId")
                )

    def get_by_id(self, employee_id: int):
        with self.create_connection() as connection:
            cursor = connection.cursor(as_dict=True)
            cursor.execute("""
                SELECT  ID,
                        FirstName,
                        LastName,
                        NationalCode,
                        Email,
                        Username AS UserName,
                        EmployeeStatusID,
                        RoleId
                FROM    Employee
                WHERE   ID = %s
            """, (employee_id,))
            data = cursor.fetchone()
            if not data:
                return None
            try:
                return Employee.create_with_dict(data)
            except Exception:
                return Employee(
                    dict_data.get("ID"),
                    dict_data.get("FirstName"),
                    dict_data.get("LastName"),
                    dict_data.get("NationalCode"),
                    dict_data.get("Email"),
                    dict_data.get("UserName") or dict_data.get("Username"),
                    dict_data.get("EmployeeStatusID"),
                    dict_data.get("RoleId")
                )

    def update_employee_password(self, employee_id: int, password_hashed: str):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Employee
                SET Password = %s
                WHERE ID = %s
            """, (password_hashed, employee_id))
            connection.commit()

    def update_employee_image_path(self, employee_id: int, image_path: str):
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Employee
                SET ImagePath = %s
                WHERE ID = %s
            """, (image_path, employee_id))
            connection.commit()


