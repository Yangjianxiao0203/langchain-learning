import asyncio
import time
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAI

async def async_generate(llm):
    resp = await llm.ainvoke(["Hello, how are you?"])
    print(resp)

async def generate_concurrently():
    llm = OpenAI(temperature=0.9)
    tasks = [async_generate(llm) for _ in range(10)]
    await asyncio.gather(*tasks)  # 使用asyncio.gather等待所有异步任务完成

# 定义一个串行（同步）方式生成文本的函数
def generate_serially():
    llm = OpenAI(temperature=0.9)  # 创建OpenAI对象，并设置temperature参数为0.9
    for _ in range(10):  # 循环10次
        resp = llm.generate(["Hello, how are you?"])  # 调用generate方法生成文本
        print(resp.generations[0][0].text)  # 打印生成的文本


async def main():
    # 记录当前时间点
    s = time.perf_counter()
    # 使用异步方式并发执行生成文本的任务
    await generate_concurrently()
    # 计算并发执行所花费的时间
    elapsed = time.perf_counter() - s
    print("\033[1m" + f"Concurrent executed in {elapsed:0.2f} seconds." + "\033[0m")

asyncio.run(main())