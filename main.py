from ast import If
import eel
import random

update_rate = 1 # eel.sleep time in seconds

print("Starting")
eel.init('Pages')


eel.start('main.html', block=False, mode="default")     # Don't block on this callupdate_controller_temp()

print("Started")


def update_charge():
    current_charge = 100
    while True:
        if current_charge >= 1:
            eel.update_value("chargeValue", f"{current_charge}%")
            eel.sleep(update_rate)                  # Use eel.sleep(), not time.sleep()
            current_charge -= 1
        else:
            current_charge = 100
        
def update_rpm():
    current_rpm = 1200
    while True:
        delta = random.randint(-10,10)
        current_rpm += delta
        eel.update_value("rpmValue", current_rpm)
        eel.sleep(update_rate)

def update_cell_temp():
    while True:
        cellTemp = random.randint(30,60)
        eel.update_value("cellTempValue",f"{cellTemp}%")
        eel.sleep(update_rate)

def update_controller_temp():
    while True:
        cellTemp = random.randint(30,60)
        eel.update_value("controllerTempValue",f"{cellTemp}%")
        eel.sleep(update_rate)

def update_speed():
    current_speed = 1200
    while True:
        delta = random.randint(-10,10)
        current_speed += delta
        eel.update_value("speedValue", f"{current_speed}MPH")
        eel.sleep(update_rate)

def update_current():
    while True:
        currentDraw = random.randint(30,60)
        eel.update_value("currentValue",f"{currentDraw}A")
        eel.sleep(update_rate)  

eel.spawn(update_charge)
eel.spawn(update_rpm)
eel.spawn(update_cell_temp)
eel.spawn(update_speed)
eel.spawn(update_current)


if __name__ == "__main__":
    update_controller_temp()
