class Customer:
    def __init__(self,
                 id,
                 firstname,
                 lastname,
                 phone_number,
                 birth_date,
                 gender):
        self.customer_id = id
        self.first_name = firstname
        self.last_name = lastname
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.gender = gender
    @classmethod
    def create_with_dict(cls,dict_data):
        return cls(
            dict_data.get("CustomerId"),
            dict_data.get("FirstName"),
            dict_data.get("LastName"),
            dict_data.get("PhoneNumber"),
            dict_data.get("BirthDate"),
            dict_data.get("Gender")
        )
