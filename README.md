# 🐾 Pokemon Telegram Bot

Этот проект реализует Telegram-бота, который позволяет пользователям создавать и взаимодействовать с покемонами через чат. Бот поддерживает команды для создания покемона, атаки, кормления и получения информации о покемоне.

## 📜 Описание

**Pokemon Telegram Bot** позволяет пользователям:
- Создавать своего покемона с уникальными характеристиками (здоровье, атака, защита).
- Кормить покемона, чтобы увеличивать его здоровье.
- Вступать в сражения с покемонами других пользователей.
- Получать информацию о характеристиках своего покемона.

Каждый покемон генерируется случайным образом с помощью API [PokeAPI](https://pokeapi.co/), и пользователь может увидеть изображение своего покемона прямо в чате.

## 🚀 Команды

- `/go` — Создать покемона. Если у вас уже есть покемон, команда не сработает.
- `/info` — Показать информацию о вашем покемоне: имя, здоровье, сила атаки, защита.
- `/attack` — Атаковать покемона другого пользователя. Чтобы атаковать, нужно ответить на сообщение противника.
- `/feed` — Покормить своего покемона, чтобы увеличить его здоровье.

## 📸 Скриншоты

![Пример создания покемона](https://user-images.githubusercontent.com/https://mail.google.com/mail/u/0?ui=2&ik=d2ee687e22&attid=0.1&permmsgid=msg-a:r9071406158793685592&th=193791de3f6dbb5c&view=fimg&fur=ip&permmsgid=msg-a:r9071406158793685592&sz=s0-l75-ft&attbid=ANGjdJ92PbaFnUCNRHdhyXNiMqhHvAF0JnR2KnGvQgbQK8AsDbQTzYvju9vvV5huuiQGz94W6L_m0Nc8jhMJW78LdEVc1isVCjQMXrI0YJkzthAbd_x854tEVovPkk0&disp=emb&realattid=ii_m4326q1n0&zw)
![Пример сражения](https://user-images.githubusercontent.com/https://mail.google.com/mail/u/0?ui=2&ik=d2ee687e22&attid=0.1&permmsgid=msg-a:r-3868200950399654729&th=1937921d967a33ca&view=fimg&fur=ip&permmsgid=msg-a:r-3868200950399654729&sz=s0-l75-ft&attbid=ANGjdJ8kcxqQnrYeVihCBLNb_AsoeN-eZFbwcRBdkJck1enbJ9tBboLl3agXqvMGUyu7ymcWi-7MRxNEAQEAOgcp0g8-GljGQYCyRB-OoULK_T4bc_cf-9i_smNUeCQ&disp=emb&realattid=ii_m432cd8e0&zw)

## 🛠️ Установка и запуск

1. Клонируйте репозиторий:
   Введите это в терминал:
   git clone https://github.com/your-username/pokemon-telegram-bot.git


2. Установите токен вашего Telegram-бота в файле config.py:
    token = "YOUR_TELEGRAM_BOT_TOKEN"


3. Запустите бота:
    В терминале введите:
        python main.py



🦾 Основные технологии
Python
pyTelegramBotAPI для взаимодействия с Telegram API
PokeAPI для получения данных о покемонах


✨ Возможности
Поддержка различных типов покемонов (обычный, магический, боец), с уникальными способностями и взаимодействиями.
Взаимодействие между пользователями через сражения и обмен информацией.
Получение изображения покемона прямо в чат.
