def check_admin(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role == "админ":
                return func(*args, **kwargs)
            else:
                print("Доступ запрещён")
        return wrapper
    return decorator


@check_admin("админ")
def secret_function():
    print("Секретная функция выполнена!")


@check_admin("арзы")
def another_function():
    print("Эта функция тоже выполнена!")


secret_function()
another_function()
