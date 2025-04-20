from typing import Callable, Any, Optional


def log(filename: str = "") -> Callable:
    """ Декоратор логов"""

    def decorator(func: Callable) -> Callable:
        # @decorator(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = 'my_function ok\n'
                log2(message, filename)
                return result
            except Exception:
                message = f"my_function error. Inputs: {args}, {kwargs}\n"
                log2(message, filename)
                raise

        return wrapper

    return decorator


def log2(message: str, filename: Optional[str]):
    """ Определение записи логов"""
    if filename:
        with open(filename, "a", encoding='utf-8') as f:
            f.write(message)
    else:
        print(message, end=' ')
