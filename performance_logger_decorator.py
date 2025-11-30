from functools import wraps
from datetime import datetime
from pymssql import connect
from time import time

def performance_logger(main_function):
    @wraps(main_function)
    def wrapper(*args, **kwargs):
        function_name = main_function.__name__
        call_datetime = datetime.now()
        start_time = time()

        user_call = None
        try:
            for arg in args:

                if hasattr(arg, "current_user") and getattr(arg, "current_user") is not None:
                    current_user = getattr(arg, "current_user")
                    if hasattr(current_user, "UserName"):
                        user_call = current_user.UserName
                    else:
                        user_call = f"{getattr(current_user, 'FirstName', '')} {getattr(current_user, 'LastName', '')}"
                    break

                if hasattr(arg, "view_manager"):
                    vm = getattr(arg, "view_manager")
                    if hasattr(vm, "current_user") and getattr(vm, "current_user") is not None:
                        cu = getattr(vm, "current_user")
                        if hasattr(cu, "UserName"):
                            user_call = cu.UserName
                        else:
                            user_call = f"{getattr(cu, 'FirstName', '')} {getattr(cu, 'LastName', '')}"
                        break
        except Exception:
            user_call = None

        result = main_function(*args, **kwargs)
        stop_time = time()
        execution_time = stop_time - start_time

        try:
            with connect(host="localhost", database="corebankingDB") as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO PerformanceLogger(FunctionName, CallDateTime, ExecutionTime, UserCall)
                    VALUES (%s, %s, %s, %s)
                """, (function_name, call_datetime, execution_time, user_call))
                connection.commit()
        except Exception as e:
            print("Logging failed:", e)

        return result

    return wrapper
