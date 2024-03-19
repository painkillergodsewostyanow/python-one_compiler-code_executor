import asyncio

from code_executor import CodeExecutor

code_executor = CodeExecutor(
    "token:str",
    'lang_id:str'
)


async def execute(code_task):
    return await code_executor.async_execute(code_task[0], code_task[1] if len(code_task) == 2 else None)


async def main(code_tasks: list[tuple[str, str or None]]):
    tasks = [execute(code_task) for code_task in code_tasks]
    results = await asyncio.gather(*tasks)
    for res in results:
        print(res)


asyncio.run(main([
    ('import time\ntime.sleep(4)\nprint(1)', None),
    ('import time\ntime.sleep(3)\nprint(2)', None),
    ('import time\ntime.sleep(4)\nprint(3)', None),
    ('import time\ntime.sleep(2)\nprint(4)', None)
]))
