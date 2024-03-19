import json
import requests
import aiohttp

from dataclasses import dataclass


@dataclass
class CodeExecuteResult:
    status: str
    language: str
    stdin: str
    output: str or bool
    errors: str or bool
    execute_time: int


class CodeExecutor:

    def __init__(self, token: str, language: str):
        self.__token = token
        self.__language = language

    def execute(self, code, input_data=None) -> CodeExecuteResult:
        url = "https://onecompiler-apis.p.rapidapi.com/api/v1/run"

        payload = {
            "language": self.__language,
            "stdin": input_data,
            "files": [
                {
                    "name": "index.py",
                    "content": code
                }
            ]
        }

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.__token,
            "X-RapidAPI-Host": "onecompiler-apis.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        return CodeExecuteResult(
            data['status'], self.__language, data['stdin'], data['stdout'], data['exception'],
            data['executionTime']
        )

    @staticmethod
    async def __async_post(url, data, headers) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data, headers=headers) as response:
                return await response.json()

    async def async_execute(self, code, input_data=None):
        url = "https://onecompiler-apis.p.rapidapi.com/api/v1/run"

        payload = {
            "language": self.__language,
            "stdin": input_data,
            "files": [
                {
                    "name": "index.py",
                    "content": code
                }
            ]
        }

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.__token,
            "X-RapidAPI-Host": "onecompiler-apis.p.rapidapi.com"
        }

        response_data = await self.__async_post(url, data=json.dumps(payload), headers=headers)

        return CodeExecuteResult(
            response_data['status'], self.__language, response_data['stdin'],
            response_data['stdout'], response_data['exception'], response_data['executionTime']
        )
