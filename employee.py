import secrets
from Common.Descriptors.string_length_descriptor import StringLengthDescriptor

class Employee:
    FirstName = StringLengthDescriptor(1, 50)
    LastName = StringLengthDescriptor(1, 50)
    NationalCode = StringLengthDescriptor(10, 10)
    Email = StringLengthDescriptor(5, 100)
    UserName = StringLengthDescriptor(3, 50)
    Password = StringLengthDescriptor(3, 50)

    def __init__(self, ID, FirstName, LastName, NationalCode, Email, UserName, Password, EmployeeStatusID, RoleID):
        self.ID = ID
        self.FirstName = str(FirstName or "")
        self.LastName = str(LastName or "")
        self.NationalCode = str(NationalCode or "")
        self.Email = str(Email or "")
        self.UserName = str(UserName or "")
        if not Password or not isinstance(Password, str) or len(Password) < 3:
            Password = secrets.token_urlsafe(12)
        self.Password = Password
        self.EmployeeStatusID = EmployeeStatusID
        self.RoleID = RoleID


    def get_full_name(self):
        return f"{self.FirstName} {self.LastName}"

    @classmethod
    def create_with_dict(cls, dict_data):
        user_name = dict_data.get("UserName") or dict_data.get("Username") or dict_data.get("userName")
        password = str(dict_data.get("Password") or "")
        return cls(
            dict_data.get("ID"),
            dict_data.get("FirstName"),
            dict_data.get("LastName"),
            dict_data.get("NationalCode"),
            dict_data.get("Email"),
            user_name,
            password,
            dict_data.get("EmployeeStatusID"),
            dict_data.get("RoleID"),

        )


