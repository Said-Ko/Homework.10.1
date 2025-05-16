from src.decorators import log
import pytest


# Успешный вызов, лог пишется в файл
def test_log_addition_to_file(tmpdir):
    log_file = tmpdir.join("log.txt")

    @log(filename=str(log_file))
    def add(x, y):
        """ Простой декоратор на сложение"""
        return x + y

    result = add(1, 2)
    assert result == 3

    with open(str(log_file), encoding="utf-8") as f:
        content = f.read()

    assert "my_function ok" in content


# Ошибка, лог пишется в файл
def test_log_error_to_file(tmpdir):
    log_file = tmpdir.join("log_error.txt")

    @log(filename=str(log_file))
    def divide(x, y):
        """Обработка ошибки, при делении на 0"""
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

    with open(str(log_file), encoding="utf-8") as f:
        content = f.read()

    assert "my_function error" in content
    assert "Inputs: (5, 0), {}" in content


# Успешный вызов, лог в консоль
def test_log_division_to_console(capsys):
    @log()
    def multiply(a, b):
        """ Простой декоратор умножения"""
        return a * b

    result = multiply(3, 4)
    assert result == 12

    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


# Ошибка, лог в консоль
def test_log_error_to_console(capsys):
    @log()
    def fail_func():
        """Обработка отсутствия логирования"""
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError):
        fail_func()

    captured = capsys.readouterr()
    assert "my_function error" in captured.out
    assert "Inputs: (), {}" in captured.out
