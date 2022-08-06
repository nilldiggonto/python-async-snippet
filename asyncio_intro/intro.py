import asyncio,time

async def main():
    print(f'I am walking at {time.ctime()}')
    await asyncio.sleep(1.0)
    print(f'I am done walking at {time.ctime()}')

asyncio.run(main())