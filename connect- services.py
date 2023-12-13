import asyncio
from bleak import BleakScanner, BleakClient
import sys

uuid_first_name = "00002a8a-0000-1000-8000-00805f9b34fb"
uuid_last_name = "00002a90-0000-1000-8000-00805f9b34fb"
uuid_gender = "00002a8c-0000-1000-8000-00805f9b34fb"

async def get_services(mac):
    async with BleakClient(mac) as client:
        print(f"Connected to {client}")

        # svcs = await client.get_services()

        # print("Services:", svcs)

        # for service in svcs:
        #     print(f"Service: {service}")

        #     print("\nCharacteristics:")

        #     for char in service.characteristics:
        #         print(f"{char}")

        #         print("\nProperties:")
        #         print(f"{char.properties}")
        
        await client.write_gatt_char(uuid_first_name, bytearray("Kelompok 8 Tekber", "utf-8"))
        await client.write_gatt_char(uuid_last_name, bytearray("Sistem Informasi", "utf-8"))
        
        first_name = await client.read_gatt_char(uuid_first_name)
        print(f"First Name: {first_name.decode('utf-8')}")
        last_name = await client.read_gatt_char(uuid_last_name)
        print(f"Last Name: {last_name.decode('utf-8')}")
        gender = await client.read_gatt_char(uuid_gender)
        print(f"Gender: {gender.decode('utf-8')}")
            
        await client.disconnect()

try:
    asyncio.run(get_services("55B078C4-83E0-4FE0-9EA1-FF90C5C889D5"))

except KeyboardInterrupt:
    print("Keyboard Interrupted")
    sys.exit(0)
