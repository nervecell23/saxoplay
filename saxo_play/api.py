import httpx
import asyncio
import json
import os


token = os.environ['ACCESS_TOKEN']

class SaxoApi:
    def __init__(self, access_token):
        self.access_token = access_token
        self.client = httpx.AsyncClient()
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }

    async def get_positions(self, skip=0, top=100):
        positions_url = 'https://gateway.saxobank.com/sim/openapi/port/v1/positions/me/'
        params = {'skip': skip, 'top': top}
        response = await self.client.get(positions_url, headers=self.headers, params=params)
        return response.json()

    async def close(self):
        await self.client.aclose()



async def main():
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    redirect_uri = 'YOUR_REDIRECT_URI'
    auth_url = 'https://gateway.saxobank.com/sim/openapi/connect/token'
    positions_url = 'https://gateway.saxobank.com/sim/openapi/port/v1/positions/me/'

    payload = {
        'grant_type': 'password',
        'username': 'YOUR_USERNAME',
        'password': 'YOUR_PASSWORD',
        'scope': 'read'
    }

    async with httpx.AsyncClient() as client:
        # response = await client.post(auth_url, data=payload, auth=(client_id, client_secret))
        # access_token = response.json()['access_token']

        access_token = token
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }

        params = {'skip': 0, 'top': 100}
        response = await client.get(positions_url, headers=headers, params=params)

        print(json.dumps(response.json(), indent=4))


if __name__ == '__main__':
    asyncio.run(main())