import asyncio
from aiofile import AIOFile, LineReader
from aiopath import AsyncPath
from aioshutil import copyfile

async def main():
    async with AIOFile("hello.txt", 'r') as afp:
        async for line in LineReader(afp):
            print(line)


async def aio_path():
    apath = AsyncPath("hello.txt")
    print(await apath.exists())
    print(await apath.is_file())
    print(await apath.is_dir())
    
    if await apath.exists():
        new_path = AsyncPath('logs')
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(apath, new_path / apath)

if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(aio_path())
    

