import asyncio
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")
        
async def count_async():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    
def main():
    for _ in range(3):
        count()

async def main_async():
    await asyncio.gather(count_async(), count_async(), count_async())
    

if __name__ == "__main__":
    print('------- Synchronous run ---------')
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    print('------ aSynchronous run ---------')
    s = time.perf_counter()
    asyncio.run(main_async())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
