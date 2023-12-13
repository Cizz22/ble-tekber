from bleak import BleakScanner
import asyncio

async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
        
asyncio.run(run()) 