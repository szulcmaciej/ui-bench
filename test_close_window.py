import base64
from io import BytesIO
from typing import List, Optional
from dotenv import load_dotenv
import pyautogui
import time
import os
from openai import OpenAI
import instructor
import pydantic

load_dotenv()



class MoveMouseAction(pydantic.BaseModel):
    """Moves the mouse cursor to a point on the screen, relative to its current position.
The x and y parameters detail where the mouse event happens. If None, the current mouse position is used. If a float value, it is rounded down. If outside the boundaries of the screen, the event happens at edge of the screen.
Args:
  x (int, float, None, tuple, optional): How far left (for negative values) or
    right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
  y (int, float, None, optional): How far up (for negative values) or
    down (for positive values) to move the cursor. 0 by default."""
    name: str = "move_mouse"
    x: int
    y: int

class LeftClickAction(pydantic.BaseModel):
    """Click on the current position"""
    name: str = "left_click"
    
class TypeAction(pydantic.BaseModel):
    """Type text using keyboard"""
    name: str = "type"
    text: str


class ChosenAction(pydantic.BaseModel):
    """ Action to perform, only one of the subfields should be set """
    mouse_move_action: Optional[MoveMouseAction] = None
    left_click_action: Optional[LeftClickAction] = None
    type_action: Optional[TypeAction] = None


def generate_new_line(base64_image, prompt: str):
    return [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                },
            ],
        },
    ]

def make_action(action: ChosenAction):
    if action.mouse_move_action:
        print(f"Moving mouse by {action.mouse_move_action.x}, {action.mouse_move_action.y}")
        pyautogui.moveRel(action.mouse_move_action.x, action.mouse_move_action.y)
    elif action.left_click_action:
        print(f"Clicking")
        # pyautogui.click()
    elif action.type_action:
        print(f"Typing {action.type_action.text}")
        # pyautogui.typewrite(action.type_action.text)
    else:
        raise ValueError("No action specified")

def act(prompt: str):
    client = instructor.patch(OpenAI())
    screenshot = pyautogui.screenshot()
    buffered = BytesIO()
    screenshot.save(buffered, format="JPEG")
    screenshot_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        response_model=ChosenAction,
        messages=generate_new_line(screenshot_base64, prompt),
        max_tokens=300,
    )
    return response
    

def test_close_terminal_window():
    # GIVEN
    # pyautogui.FAILSAFE = True
    # pyautogui.PAUSE = 1
    #assert pyautogui.locateOnScreen("gnome-terminal")
    # os.system("gnome-terminal")
    time.sleep(1)

    prompt = f"I want to open the firefox window. What should I do? Current mouse position: {pyautogui.position()}, Current screen size: {pyautogui.size()}"
    print(prompt)
    action = act(prompt)
    print(action)

    make_action(action)
    
    #time.sleep(5)
    # WHEN
    # pyautogui.click(x=100, y=100)
    # time.sleep(1)
    # THEN


if __name__ == "__main__":
    test_close_terminal_window()