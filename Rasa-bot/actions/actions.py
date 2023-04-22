from typing import Any, Text, Dict, List, Union

from googletrans import Translator
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import wikipediaapi
from rasa_sdk.events import SlotSet
from bs4 import BeautifulSoup
import requests

wiki = wikipediaapi.Wikipedia('ru')


class ActionGetCapital(Action):
    def name(self) -> Text:
        return "action_get_capital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Название страны
        country_name = tracker.get_slot('country')
        # URL страницы с информацией о стране
        url = f"https://ru.wikipedia.org/wiki/{country_name}"

        # Получаем содержимое страницы
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")

        # Находим информацию о столице
        capital = ""
        for th in soup.select("th"):
            if "столица" in th.text.lower():
                capital = th.find_next_sibling("td").text.strip()
                break

        # Отправляем ответ пользователю
        if capital:
            dispatcher.utter_message(f"Столица {country_name}: {capital}")
        else:
            dispatcher.utter_message(f"Информация о столице {country_name} не найдена")

        return []


class ActionGetPopulation(Action):

    def name(self) -> Text:
        return "action_get_population"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot('country')
        if country:
            wiki = wikipediaapi.Wikipedia('ru')
            page = wiki.page(country)
            if page.exists():
                if "население" in page.text.lower():
                    start = page.text.lower().index("население")
                    end = page.text.lower().index("человек")
                    population = page.text[start:end]
                    dispatcher.utter_message(text=population)
                else:
                    dispatcher.utter_message(text="Информация о населении не найдена.")
            else:
                dispatcher.utter_message(text="Страница не найдена.")
        else:
            dispatcher.utter_message(text="Страна не найдена.")

        return [SlotSet('country', country)]


class ActionGetArea(Action):

    def name(self) -> Text:
        return "action_get_area"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot('country')  # получаем название страны из последнего сообщения пользователя
        url = f"https://ru.wikipedia.org/wiki/{country}"  # формируем URL для соответствующей страницы Википедии

        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")

        area = ""
        for td in soup.select("td"):
            if "Территория" in td.text:
                for tr in soup.select('tr'):
                    if "Всего" in tr.text:
                        area = tr.find_next('td').text
                break

        if area:
            response = f"Территория {country}: {area}"
        else:
            response = f"Информация о территории {country} не найдена"

        dispatcher.utter_message(text=response)  # отправляем сообщение пользователю

        return []


def translate_en2ru(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ru')
    return translated.text


def translate_ru2en(text):
    translator = Translator()
    translated = translator.translate(text, src='ru', dest='en')
    return translated.text


class ActionGetContinent(Action):

    def name(self) -> Text:
        return "action_get_continent"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # country = tracker.latest_message['entities'][0]['value']
        country = tracker.get_slot('country')
        # замените на свой API-ключ и ссылку
        api_key = "https://restcountries.com"
        url = f"https://restcountries.com/v3.1/name/{translate_ru2en(country)}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            continent = data[0]["continents"][0]
            dispatcher.utter_message(
                f"{country} находится на континенте {translate_en2ru(continent)}.")
        else:
            dispatcher.utter_message(f"Извините, не могу найти информацию о стране {country}.")

        return []
