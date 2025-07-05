import asyncio

class AsyncResourceManager:
    async def __aenter__(self):
        print("Entering the async context")
        # 模拟异步初始化操作
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the async context")
        # 模拟异步清理操作
        await asyncio.sleep(1)
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False

async def main():
    async with AsyncResourceManager() as manager:
        print("Inside the async context")

asyncio.run(main())
