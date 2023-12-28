### HakuDev Discord Бот и API

Этот репозиторий содержит код для Discord бота и API, разработанного Tokishu и Антоном.
Получить DiscordID пользователя вы можете сделав авторизацию на вашем сайте через Discord Oauth2.

---

#### Функционал:

- API на основе FastAPI для получения информации о пользователях.

---

#### Установка:

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/Tok1shu/DiscordUserAPI.git
   cd DiscordUserAPI
   ```

2. Установить зависимости:

   ```bash
   pip install asyncio discord discord.py fastapi aiohttp uvicorn
   ```

3. Настроить конфигурацию:

   Отредактируйте контент в файле с именем `settings.py`:

   ```python
   settings = {
       'discordToken': 'ВАШ_ТОКЕН_ДИСКОРДА',
       'hakuServerId': 'ИДЕНТИФИКАТОР_ВАШЕГО_СЕРВЕРА'
   }
   ```

   Замените `ВАШ_ТОКЕН_ДИСКОРДА` на токен вашего Discord бота, а `ИДЕНТИФИКАТОР_ВАШЕГО_СЕРВЕРА` на идентификатор вашего Discord сервера.

---

#### Использование:

1. Запустите бота и API:

   ```bash
   python bot.py
   ```

2. Наслаждаться.

---

#### Конечные точки API:

- **GET /api/getUser/{user_id}**

  Получение информации о пользователе Discord.

  - **Параметры:**
    - `user_id` (Path): Идентификатор пользователя Discord.

  - **Пример:**
    ```http
    GET /api/getUser/1234567890
    ```
  - **Ответ:**
    ```json
    {
    "avatar": "https://cdn.discordapp.com/avatars/761175017588916224/1de233297fdabbabfee73c6808ef12d9.png?size=1024",
    "nickname": "Tok1shu",
    "roles": [
        "@everyone",
        "new role"
    ],
    "discord_id": "761175017588916224",
    "banner": "https://cdn.discordapp.com/banners/761175017588916224/5a0958976d4a7f63794525ba3fab2244.png?size=512"
}
    ```
---

#### Важное замечание:

Убедитесь, что вашему Discord боту предоставлены необходимые разрешения, и он добавлен на ваш сервер Discord.
Также замените айпи и порт в файле `tok.py` если есть такая необходимость!

---

#### Участники:

- [Токишу](https://github.com/Tok1shu)
- Discord антона: @anton2281337

---

#### Лицензия:

Этот проект лицензирован по лицензии MIT - см. файл [LICENSE](LICENSE) для получения подробной информации.
