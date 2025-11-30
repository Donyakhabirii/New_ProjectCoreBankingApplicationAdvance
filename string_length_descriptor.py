class StringLengthDescriptor:
    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length
        self.private_name = None

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.private_name[1:]} must be a string, got {type(value).__name__}")
        if not (self.min_length <= len(value) <= self.max_length):
            raise ValueError(
                f"{self.private_name[1:]} must be between {self.min_length} and {self.max_length} characters long"
            )
        setattr(instance, self.private_name, value)

