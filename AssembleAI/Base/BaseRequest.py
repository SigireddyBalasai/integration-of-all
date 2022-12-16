import aiohttp


class Request:
    def __init__(self, url,headers,data=None,json=None):
        self.url = url
        self.data = data
        self.headers = headers
        self.json = json

    async def request_with_data(self):
        async with aiohttp.ClientSession() as session:
            response = await session.post(self.url,headers=self.headers,data=self.data)
            return response

    async def request_without_data(self):
        async with aiohttp.ClientSession() as session:
            response = await session.post(self.url,headers=self.headers,json=self.json)
            return response

    async def request_get(self):
        async with aiohttp.ClientSession() as session:
            response = await session.get(self.url,headers=self.headers)
            return response
