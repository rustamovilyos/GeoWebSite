import requests
from bs4 import BeautifulSoup

# # URL страницы с информацией о стране
# url = "https://ru.wikipedia.org/wiki/Узбекистан"
#
# # получаем содержимое страницы
# res = requests.get(url)
# soup = BeautifulSoup(res.content, "html.parser")
#
# # находим информацию о столице
# capital = ""
# for th in soup.select("th"):
#     if "Реки" in th.text.lower():
#         capital = th.find_next_sibling("td").text.strip()
#         break
#
# # выводим результат
# if capital:
#     print(f"Столица Франции: {capital}")
# else:
#     print("Информация о столице Франции не найдена")

# import requests
# from bs4 import BeautifulSoup
#
# # URL страницы с информацией о стране
# url = f"https://ru.wikipedia.org/wiki/Беларусь"
#
# # Получаем содержимое страницы
# res = requests.get(url)
# soup = BeautifulSoup(res.content, "html.parser")
#
# # Находим информацию о столице
# capital = ""
# for td in soup.select("td"):
#     if "Территория" in td.text:
#         # print(td.text)
#         # print(td.find("tr"))
#         for tr in soup.select('tr'):
#             if "Всего" in tr.text:
#                 # print(tr.find_next('td').text)
#                 capital = tr.find_next('td').text
#         break
#
# # выводим результат
# if capital:
#     print(f"Территория Узбекистана: {capital}")
# else:
#     print("Информация о территории Узбекистана не найдена")


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_country_continent(country):
#     # URL страницы с информацией о стране
#     url = f"https://ru.wikipedia.org/wiki/{country}"
#
#     # Получаем содержимое страницы
#     res = requests.get(url)
#     soup = BeautifulSoup(res.content, "html.parser")
#
#     # Находим информацию о материке
#     continent = ""
#     for th in soup.select("th"):
#         if "Материк" in th.text:
#             for td in th.parent.select('td'):
#                 if td.text:
#                     continent = td.text.strip()
#                     break
#             break
#
#     # Возвращаем результат
#     if continent:
#         return f"{country} находится на материке {continent}"
#     else:
#         return f"Информация о материке, в котором расположена {country}, не найдена"
#
#
# print(get_country_continent('Австралия'))


from googletrans import Translator


def translate(text):
    translator = Translator()
    translated = translator.translate(text, src='ru', dest='en')
    return translated.text


# Пример использования
text_to_translate = "Узбекистан"
translated_text = translate(text_to_translate)
print(translated_text)
