import asyncio
import random

async def producer(queue,id):
    for i in range(3):
        item = f"item : id - {id}"
        await queue.put(item)
        print(f"Producer Produced -> {item}")
        await asyncio.sleep(random.uniform(0.1,0.5))

async def consumer(queue):
    while True:
        item = await queue.get()
        if item == None:
            break
        else:
            queue.task_done()



async def main():
    q = asyncio.Queue()
    producers = [ asyncio.create_task(producer(q,i)) for i in range(3)]
    consumer_task = asyncio.create_task(consumer(q))
    await asyncio.gather(*producers)
    await q.join()
    await q.put(None)
    await consumer_task

asyncio.run(main())