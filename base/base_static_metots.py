from selenium.webdriver.remote.webelement import WebElement


class StaticMetods:
    """Методы преобразования веб элементов"""

    @staticmethod
    def upper_list(list_text: list) -> list:
        """Преобразовывает в верхний регситр весь текст в списке"""
        res = [i.upper() for i in list_text]
        return list(res)

    @staticmethod
    # Где elements_list_text => элемент который нужно преобразовать
    def text_list_to_string(elements_list_text: list) -> str:
        """Переобразовывает список в одну строку"""
        str_text: list = elements_list_text
        return "".join(str_text)

    @staticmethod
    def list_text_to_list_int(list_text: list[str]) -> list[int]:
        """Преобразовывает список строк в список цифр удаляя все пробелы"""
        result = [int(''.join(item.split())) for item in list_text]
        return result

    @staticmethod
    def get_text_from_webelement(element: WebElement) -> str:
        """Получаем строку(текст в виде строки) из веб элемента"""
        return element.text

    @staticmethod
    def get_text_from_webelements(elements: list[WebElement]) -> list[str]:
        """Получаем список строк(текст в списке) из множества одинаковых веб элементов"""
        return [text_elements.text for text_elements in elements]

    @staticmethod
    def one_int_to_many_ints(one_int: int) -> list[int]:
        """Преобразуем одно число в список чисел"""
        result = []
        while one_int > 0:
            result.append(one_int % 10)
            one_int //= 10
        result.reverse()
        return result
