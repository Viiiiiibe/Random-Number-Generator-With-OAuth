import asyncio
import random
from channels.generic.websocket import AsyncWebsocketConsumer


class RandomNumberConsumer(AsyncWebsocketConsumer):
    # переменная для хранения текущего случайного числа
    current_number = random.randint(1, 100)

    # переменная для отслеживания статуса генерации чисел
    generation_task = None

    async def connect(self):
        await self.accept()

        # присоединяем пользователя к группе
        await self.channel_layer.group_add("random_number_group", self.channel_name)

        # отправляем текущее число новому подключенному клиенту
        await self.send(text_data=str(self.current_number))

        # запускаем генерацию случайных чисел, если она еще не запущена
        if not RandomNumberConsumer.generation_task:
            RandomNumberConsumer.generation_task = asyncio.create_task(self.generate_random_number())

    async def disconnect(self, close_code):
        # Отключаем пользователя от группы
        await self.channel_layer.group_discard("random_number_group", self.channel_name)

    async def generate_random_number(self):
        while True:
            # генерация нового случайного числа
            RandomNumberConsumer.current_number = random.randint(1, 100)

            # отправляем новое число всем подключенным клиентам
            await self.channel_layer.group_send(
                "random_number_group",
                {
                    "type": "send_number",
                    "number": RandomNumberConsumer.current_number,
                }
            )

            await asyncio.sleep(5)

    async def send_number(self, event):
        # отправляем число клиентам
        await self.send(text_data=str(event["number"]))
