import asyncio

# ИМИТАЦИЯ АСИНХРОННОГО СОЕДИНЕНИЯ С НЕКОЙ ПЕРИФЕРИЕЙ
async def get_conn(host, port):
    class Conn:
        async def put_data(self):
            print('Отправка данных...')
            await asyncio.sleep(2)
            print('Данные отправлены.')

        async def get_data(self):
            print('Получение данных...')
            await asyncio.sleep(2)
            print('Данные получены.')

        async def close(self):
            print('Завершение соединения...')
            await asyncio.sleep(2)
            print('Соединение завершено.')
            
    print('Устанавливаем соединение...')
    await asyncio.sleep(2)
    print('Соединение установлено.')
    return Conn()

class Connection:
    # ЭТОТ КОНСТРУКТОР БУДЕТ ВЫПОЛНЕН В БЛОКЕ with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # ЭТОТ МЕТОД БУДЕТ ВЫПОЛНЕН ПРИ ВХОДЕ В with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # ЭТОТ МЕТОД БУДЕТ ВЫПОЛНЕН ПРИ ВЫХОДЕ ИЗ with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()

async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())
        # ОДНОВРЕМЕННО ОТПРАВКА И ПОЛУЧЕНИЕ ДАННЫХ ВЫПОЛНЕНЫ КОНКУРЕНТНО
        await send_task
        await receive_task

asyncio.run(main())