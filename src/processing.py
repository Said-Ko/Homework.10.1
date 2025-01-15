from typing import Dict, List, Any


def filter_by_state(tested_dict: List[Dict[str, Any]], state_of_dict: str = "EXECUTED") -> str | list[dict[str, Any]]:
    """Функция возвращает список словарей со статусом 'EXECUTED'"""
    if tested_dict is None or not tested_dict: # проверка, является ли словарь пустым или имеет ли значение
        return "отсутствует ключ-значение в словаре"
    else:
        list_of_executed = [] # создаем дополнительный словарь, который будет хранить удовлетворяющие условию словари
        for element_of_list in tested_dict:
            if element_of_list("state") == state_of_dict:
                list_of_executed.append(element_of_list)
    return list_of_executed


def sort_by_date(tested_input: List[Dict], arg_for_sort: bool = True) -> List[Dict]:
    """Функция сортировки списока словарей по возрастанию даты"""
    sort_list = sorted(tested_input, key=lambda x: x.get("date"), reverse=arg_for_sort)
    return sort_list
