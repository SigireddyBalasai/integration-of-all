import aiofiles
import aiohttp
from AssembleAI.Base.Exceptions import Invalid_Api_token
from AssembleAI.Base.BaseRequest import Request


async def _upload_file(filepath: str):
    async with aiofiles.open(filepath, "rb") as file:
        while True:
            data = await file.read(5242880)
            if not data:
                break
            yield data


class Requests:
    def __init__(self, authorization: str):
        self.headers = {"authorization": authorization}

    async def upload_file(self, filepath):
        data = _upload_file(filepath)
        request = Request(url='https://api.assemblyai.com/v2/upload', data=data, headers=self.headers)
        ok = await request.request_with_data()
        response = await ok.json()
        print(response)
        if ok.status == 401:
            raise Invalid_Api_token
        else:
            return response['upload_url']

    async def get_transcription(self, url):
        request = Request(url="https://api.assemblyai.com/v2/transcript", json={"audio_url": url}, headers=self.headers)
        ok = await request.request_without_data()
        response = await ok.json()

        print(response)
        return response['id']

    async def get_result(self, id):
        request = Request(url=f"https://api.assemblyai.com/v2/transcript/{id}", headers=self.headers)
        ok = await request.request_get()
        response = await ok.json()
        print(response)
