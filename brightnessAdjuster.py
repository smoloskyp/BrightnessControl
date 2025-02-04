import screen_brightness_control as sbc
import keyboard
import numpy
import time
import cv2
import wmi

class BrightnessCalculator:
    def __init__(self, minimal_brightness=40):
        self.minimalBrightness = minimal_brightness

    def calculate_brightness(self, frame) -> int:
        average_brightness = int(frame.mean())
        brightness_percent = round((average_brightness * (100 - self.minimalBrightness) / 255) + self.minimalBrightness)
        return brightness_percent


class DisplayBrightnessController:
    def __init__(self, num_displays):
        self.amountOfDisplays = num_displays

    def set_brightness(self, brightness: int):
        for display in range(self.amountOfDisplays):
            try:
                sbc.set_brightness(brightness, display=display)
                print(f"adjusted: (monitor:{display}, brightness:{brightness}%)")
            except Exception as e:
                print(f"Error: {e}")


class Camera:
    def take_a_frame(self) -> numpy.ndarray | None:
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        if not camera.isOpened():
            print("Error: Could not open camera.")
            return None
        
        frame = camera.read()[1]

        if camera.isOpened():
            camera.release()
        return frame
    
    def get_CameraList(self):
        ...



class BrightnessController:
    def __init__(self, calculator: BrightnessCalculator, controller: DisplayBrightnessController, camera: Camera):
        self.calculator = calculator
        self.controller = controller
        self.camera = camera

    def adjust_brightness(self):
        frame = self.camera.take_a_frame()
        brightness = self.calculator.calculate_brightness(frame)
        self.controller.set_brightness(brightness)


class HotkeyListener:
    def __init__(self, brightness_controller: BrightnessController, hotkey: str = 'F9'):
        self.brightness_controller = brightness_controller
        self.hotkey = hotkey

    def listen_for_hotkey(self):
        while True:
            if keyboard.is_pressed(self.hotkey):
                print(f"Adjusting brightness...")
                self.brightness_controller.adjust_brightness()
                time.sleep(1)


if __name__ == "__main__":
    calculator = BrightnessCalculator()
    controller = DisplayBrightnessController(num_displays=len(wmi.WMI(namespace="wmi").WmiMonitorBasicDisplayParams()))
    camera = Camera()

    brightness_adjuster = BrightnessController(calculator, controller, camera)
    hotkey_listener = HotkeyListener(brightness_controller=brightness_adjuster, hotkey='F9')

    import threading
    hotkey_thread = threading.Thread(target=hotkey_listener.listen_for_hotkey)
    hotkey_thread.daemon = True
    hotkey_thread.start()

    # цикл для утримання основного потіку програми робочим
    while True: 
        time.sleep(1)