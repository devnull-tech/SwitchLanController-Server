import json
import vgamepad
import asyncio
from websockets.asyncio.server import serve

gamepad = vgamepad.VX360Gamepad()
left_analog = {
    "x": 0.0,
    "y": 0.0
}
right_analog = {
    "x": 0.0,
    "y": 0.0
}

def gamepad_input(remote_input: dict):
    button = None
    match remote_input.get("action"):
        case "b":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
        case "a":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B
        case "x":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y
        case "y":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X
        case "du":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
        case "dd":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
        case "dl":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
        case "dr":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
        case "l":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
        case "r":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
        case "l3":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
        case "r3":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
        case "start":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START
        case "select":
            button = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK
    if button is not None:
        if remote_input.get("is_pressed"):
            gamepad.press_button(button=button)
        else:
            gamepad.release_button(button=button)
    elif remote_input.get("action") == "zl":
        value = 255 if remote_input.get("is_pressed") else 0
        gamepad.left_trigger(value)
    elif remote_input.get("action") == "zr":
        value = 255 if remote_input.get("is_pressed") else 0
        gamepad.right_trigger(value)
    elif remote_input.get("action")[0:4] == "axis":
        if remote_input.get("action") == "axis0":
            left_analog["x"] = remote_input.get("analog_value")
        elif remote_input.get("action") == "axis1":
            left_analog["y"] = remote_input.get("analog_value") * -1
        elif remote_input.get("action") == "axis2":
            right_analog["x"] = remote_input.get("analog_value")
        elif remote_input.get("action") == "axis3":
            right_analog["y"] = remote_input.get("analog_value") * -1
        gamepad.left_joystick_float(x_value_float=left_analog["x"], y_value_float=left_analog["y"])
        gamepad.right_joystick_float(x_value_float=right_analog["x"], y_value_float=right_analog["y"])
    gamepad.update()


async def echo(websocket):
    async for message in websocket:
        remote_input = json.loads(message.decode())
        gamepad_input(remote_input)
        #await websocket.send("Recived")

async def main():
    async with serve(echo, "0.0.0.0", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
