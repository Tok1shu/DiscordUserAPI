################################
###      HakuDev bot&api     ###
###                          ###
###     By Tokishu&Anton     ###
###     Discord&Telegram:    ###
###         @tokishu         ###
################################


import asyncio
from settings import settings
import discord
from discord.ext import commands
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import Path

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

from fastapi import Depends

@app.get("/api/getUser/{user_id}")
async def get_user_route(user_id: str = Path(..., title="Discord User ID")):
    user_data = await get_user(user_id)
    print(user_data)
    if not user_data:
        return {"error": "User not found"}
    return user_data

async def get_user(user_id: str, rate_limit: Depends = Depends()):
    try:
        user = await bot.fetch_user(user_id)
        guild_id = settings['hakuServerId']
        guild = await bot.fetch_guild(guild_id)
        if guild:
            member = await guild.fetch_member(user.id)
            if member:
                avatar = user.avatar
                nickname = member.display_name
                banner = user.banner.url if user.banner else user.accent_color
                roles = [role.name for role in member.roles]
                banner = banner if banner is not None else user.accent_color

                return {
                    "avatar": str(avatar.url) if avatar else None,
                    "nickname": str(nickname),
                    "roles": roles,
                    "discord_id": user_id,
                    "banner": str(banner) if banner else None
                }



    except discord.NotFound:
        return None

@bot.event
async def on_ready():
    print(f'[{bot.user}] Успешная авторизация')

async def start_bot():
    await bot.start(settings['discordToken'])

async def start_api():
    import uvicorn
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_api())
    loop.run_until_complete(start_bot())
