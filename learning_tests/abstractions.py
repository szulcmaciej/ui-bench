from typing import List


class Input:
    pass

class Action:
    pass

class MoveMouseAction(Action):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def describe(self):
        return f"Move mouse to {self.x}, {self.y}"

class ClickAction(Action):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def describe(self):
        return f"Click at {self.x}, {self.y}"


class TextInput(Action):
    def __init__(self, text: str) -> None:
        self.text = text

    def describe(self):
        return f"Type {self.text}"


class KeyboardInput(Action):
    def __init__(self, key: str) -> None:
        self.key = key


class ModelTestCase:
    input: Input
    available_actions: List[Action]

    def run(self, model):
        pass

class ImageInput:
    image: bytes
    description: str
    def __init__(self, image: bytes, description: str) -> None:
        self.image = image
        self.description = description
        


class WebUIInteractionTestCase(ModelTestCase):
    def __init__(self, input: Input) -> None:
        super().__init__()
        self.input = ImageInput()
        self.available_actions = []

    def run(self):
        pass