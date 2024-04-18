import asyncio
from aiofile import async_open

async def main():
    async with async_open("hello.txt", 'w+') as afp:
        await afp.write("Hello ")
        await afp.write("world\n")
        await afp.write("Hello from - async world!")

async def read():
    async with async_open("hello.txt", 'r') as afp:
        print(await afp.read())

async def async_read():
    async with async_open("hello.txt", 'r') as afp:
        async for line in afp:
            print(line)

if __name__ == '__main__':
    asyncio.run(read())
    asyncio.run(async_read())
    
