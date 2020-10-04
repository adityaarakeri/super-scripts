# External libraries
import psutil
from plyer import notification 
from threading import Timer


def batteryStatus():
    Timer(60.0, batteryStatus).start()  # the function refreshes every 60 seconds
    # battery details
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    
    # checking the battery status
    plugged = "Plugged In" if plugged else "Not Plugged In"
    if 'Not' in plugged and (percent < 40):
        percent = str(percent)
        output = ''.join([percent,'% | ', plugged])
        print(output)
        print(f"Please plug in your charger. Battery life is only {percent}%")
        notification.notify( 
            title="Battery Percentage", 
            message=output, 
            timeout=10,
        ) 
    elif 'Plugged' in plugged and (percent == 100):
        percent = str(percent)
        output = ''.join([percent,'% | ', plugged])
        print(output)
        print("Please unplug the charger. Your battery is fully charged")
        notification.notify( 
            title="Battery Percentage", 
            message=output, 
            timeout=10,
        ) 
    else:
        pass

# batteryStatus()
