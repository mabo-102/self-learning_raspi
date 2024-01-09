from time import sleep
import os

import pygame

os.environ["SDL_VIDEODRIVER"] = "dummy"

def main():
    pygame.init()
    try:
        joys = pygame.joystick.Joystick(0)
        joys.init()
        print(f"Joystick Name: {joys.get_name()}")
        print(f"Number of Buttons: {joys.get_numbuttons()}")
    except pygame.error:
        print("Joystick not found.")

    while True:
        events = pygame.event.get()
        for event in events:
            print(f"VARS: {vars(event)}")
            print(f"EventType: {event.type}")
            print(f"EventName: {pygame.event.event_name(event.type)}")
            if hasattr(event, 'joy'):
                print(f"Joy# {event.joy}")
            if hasattr(event, 'instance_id'):
                print(f"Instance Id# {event.instance_id}")
            if hasattr(event, 'button'):
                print(f"Button # {event.button}")
            if hasattr(event, 'value'):
                print(f"Value: {event.value}")
        sleep(0.5)

if __name__ == "__main__":
    main()
