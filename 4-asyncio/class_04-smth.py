import asyncio
import random

ANSI_COLORS = {
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
}

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(f"\033[36m Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"\033[91m makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(f"\033[35m ---> Finished: makerandom({idx}) == {i}\033[0m")
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
