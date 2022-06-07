import discordio
from discordio.interactions import registrator

bot = discordio.Bot(token='OTgzNzQ2OTk1MzU1Mjg3NTYz.G505P1.0a0ipROke1QHUCtRZXcL6dzzdHgs7YXjTgJoqM', prefix='!', application_id=983746995355287563)

registrator.slash_command(name='test')

bot.run()
