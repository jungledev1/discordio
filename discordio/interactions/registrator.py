import aiohttp
from bot import Bot

async def slash_command(name: str, description: str = None):
    if description is None:
        description = 'Not provided'

    data = {
        'name': name,
        'description': description
    }

    headers = {
        'Authorization': f"Bot {Bot.token}"
    }

    async with aiohttp.ClientSession().post(url=f'https://discord.com/api/v10/applications/{Bot.app_id}/commands', headers=headers, data=data) as s:
        if s.status == 200:
            print(f"Command {name} registered")
        else:
            print(f"Error in register command {name}")


