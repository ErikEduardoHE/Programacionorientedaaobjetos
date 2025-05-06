import asyncio
from time import sleep

async def tarea(nombre):
    print(f"{nombre} inicia")
    await asyncio.sleep(2)
    print(f"{nombre} termino")
async def main():
    await asyncio.gather(
tarea("tarea_1"),
tarea("tarea_2")
)
asyncio.run(main())