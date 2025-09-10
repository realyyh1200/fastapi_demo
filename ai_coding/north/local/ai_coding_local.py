from typing import Generator

from ...south.client_adapter.get_location_client_adapter import GetWeatherClientAdapter


class AiCodingLocalService:
    def __init__(self):
        self.get_weather_local_client = GetWeatherClientAdapter()

    def get_weather(self, question: str) -> Generator[bytes, None, None]:
        question = question.strip()
        if not question:
            return None
        location = self.get_weather_local_client.get_location(question)
        if not location:
            return GetWeatherClientAdapter.err_stream()
        weather_info = self.get_weather_local_client.get_weather(location)
        for i, char in enumerate(weather_info):
            yield char.encode("utf-8")
