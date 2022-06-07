import aiohttp


class Bot:
    def __init__(self, token: str, prefix: str, application_id: int):
        self.token = token
        self.prefix = prefix
        self.app_id = application_id

    async def run():
        async with aiohttp.ClientSession().get('https://discord.com/api/v10/users/@me', headers={'Authorization': f"Bot {Bot.token}"}) as session:
            return await session.json()

    async def token():
        return Bot.token
