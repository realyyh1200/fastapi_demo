import re
from datetime import datetime
import requests
from settings import API_KEY


WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


class GetWeatherClientAdapter:
    def get_location(self, question: str) -> str | None:
        match = re.search(r'(?:今天|现在|这儿|这里|那|那里)[，。？\s]*(.+?)[？。！\s]*$', question)
        if match:
            return match.group(1).strip()
        cities = re.findall(r'[\u4e00-\u9fa5]{2,}|[a-zA-Z]+', question)
        for city in cities:
            if len(city) > 1:
                return city
        return None

    def get_weather(self, city_name: str) -> str:
        params = {
            'q': city_name,
            'appid': API_KEY,
            'lang': 'zh_cn',
            'units': 'metric'
        }
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        city = data['name']
        country = data['sys']['country']
        return (
            f"📍 {city}, {country}\n"
            f"🌤 天气：{desc}\n"
            f"🌡 温度：{temp}°C\n"
            f"💧 湿度：{humidity}%\n"
            f"📅 {datetime.now().strftime('%Y年%m月%d日 %H:%M')}"
        )

    @staticmethod
    def err_stream():
        msg = "🤖 抱歉，我没听清你想查哪个城市的天气？请说清楚哦～"
        for char in msg:
            yield char.encode("utf-8")