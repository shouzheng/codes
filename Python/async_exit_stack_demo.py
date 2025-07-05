import asyncio
from contextlib import AsyncExitStack

class SomeAsyncResource:
    async def __aenter__(self):
        print("Entering SomeAsyncResource")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting SomeAsyncResource")
        await asyncio.sleep(1)

async def main():
    async with AsyncExitStack() as stack:
        # 动态添加异步上下文管理器
        resource = await stack.enter_async_context(SomeAsyncResource())
        print("Using the resource")
        print(type(resource))

asyncio.run(main())
