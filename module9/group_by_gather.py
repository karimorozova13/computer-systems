import asyncio

async def task_one():
    await asyncio.sleep(1)
    return "результат task_one"

async def task_two():
    await asyncio.sleep(2)
    return "результат task_two"

async def main():
    results = await asyncio.gather(task_one(), task_two())
    print(results)  

if __name__ == '__main__':
    asyncio.run(main())
