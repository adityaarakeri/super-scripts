import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
        title = "......Its Time to Drink Water......",
        message = "water is essential for life. "
                  "The amount of drinking water required to maintain good health varies, "
                  "and depends on physical activity level, age, health-related issues, "
                  "and environmental conditions.",
        app_icon = "F:\ico.file\glass.ico.ico",
        timeout = 10,
        )
        time.sleep(60*60)