from  typing import List,Dict

def filter_by_state (tested_input: List[Dict], state_of_dict: str = 'EXECUTED') -> List[Dict]:
    """ Функция возвращает список словаре со статусом 'EXECUTED' """
    list_of_executed = []
    for element_of_list in tested_input:
        if element_of_list['state'] == state_of_dict:
            list_of_executed.append(element_of_list)
    return list_of_executed
    

def sort_by_date (tested_input: List[Dict], arg_for_sort: bool = True) -> List[Dict]:
    """ Функция сортировки списока словаре по возрастанию даты """
    sort_list = sorted(tested_input, key=lambda x: x.get('date'), reverse=arg_for_sort)
    return sort_list



