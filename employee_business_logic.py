from hashlib import md5
from Common.DTOs.response import Response
from Common.Repositories.iemployee_repository import IEmployeeRepository

class EmployeeBusinessLogic:
    def __init__(self, employee_repository: IEmployeeRepository):
        self.employee_repository = employee_repository
        self._current_user = None
    @property
    def current_user(self):
        return self._current_user
    @current_user.setter
    def current_user(self, employee):
        self._current_user = employee
    def login(self, username: str, password: str):
        if len(username) < 3 or len(password) < 6:
            return Response(False, "Invalid username or password format", None)
        password_hashed = md5(password.encode()).hexdigest()
        employee = self.employee_repository.get_by_username_password(username, password_hashed)
        if employee is None:
            return Response(False, "Invalid username or password", None)
        self.current_user = employee
        return Response(True, f"Welcome {employee.get_full_name()}", employee)

    def get_employee_by_id(self, employee_id: int):
        employee = self.employee_repository.get_by_id(employee_id)
        if employee:
            return Response(True, "Employee found", employee)
        return Response(False, "Employee not found", None)

    def update_employee_password(self, employee_id: int, new_password_plain: str):
        if not new_password_plain or len(new_password_plain) < 6:
            return Response(False, "Password must be at least 6 characters long", None)

        try:
            password_hashed = md5(new_password_plain.encode()).hexdigest()
            self.employee_repository.update_employee_password(employee_id, password_hashed)
            return Response(True, "Password updated successfully", None)
        except Exception as e:
            return Response(False, f"Failed to update password: {str(e)}", None)

    def update_employee_image(self, employee_id: int, image_path: str):
        try:
            self.employee_repository.update_employee_image_path(employee_id, image_path)
            return Response(True, "Image uploaded", image_path)
        except Exception as e:
            return Response(False, f"Failed to update image: {str(e)}", None)


