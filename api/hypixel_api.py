import requests
import json

from typing import Dict

from .utils import get_hypixel_api_key


class MinecraftStatsFetcher:
    HYPIXEL_API_KEY = get_hypixel_api_key()
    HYPIXEL_PATH = 'https://api.hypixel.net/v2/player'
    MOJANG_PROFILE_URL = 'https://api.mojang.com/users/profiles/minecraft'

    def __init__(self) -> None:
        if not MinecraftStatsFetcher.HYPIXEL_API_KEY:
            raise ValueError(
                'Hypixel API key not found. Please set it in the .env file.')

    def get_uuid(self, username: str) -> str:
        response = requests.get(
            f'{MinecraftStatsFetcher.MOJANG_PROFILE_URL}/{username}')

        if response.status_code == 200:
            return response.json()['id']
        raise Exception(f"Failed to get UUID for username: {username}")

    def __get_player_hypixel_url_creds(self, uuid: str) -> str:
        return f'{MinecraftStatsFetcher.HYPIXEL_PATH}?key={MinecraftStatsFetcher.HYPIXEL_API_KEY}&uuid={uuid}'

    def get_skywars_data(self, uuid: str):
        url = self.__get_player_hypixel_url_creds(uuid)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                return data['player']['stats'].get('SkyWars', {})
            raise Exception("Failed to fetch SkyWars data from Hypixel API.")
        raise Exception("Failed to fetch data from Hypixel API.")

    def print_last_game_stats(self, skywars_data: Dict) -> None:
        print(f"Last game stats:\n {json.dumps(skywars_data, indent=4)}")
