import tkinter as tk
import requests
from PIL import Image
from PIL import ImageTk

app = tk.Tk()
app.wait_visibility(app)
app.wm_attributes("-alpha",1)

HEIGHT = 500
WIDTH = 600

def format_response(weather_json):
    try:
        city = weather_json['name']
        longi=weather_json['coord']['lon']
        lati=weather_json['coord']['lat']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        pressure=weather_json['main']['humidity']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s\nHumidity(percent):%s\nLatitude(°):%s\nLongitude(°):%s' % (city, conditions, temp,pressure,longi,lati)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str


def get_weather(city):
    weather_key = '737660a621cfe13892b75c9707da8c6c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': '737660a621cfe13892b75c9707da8c6c', 'q': city, 'units':'imperial'}
    response = requests.get(url, params=params)
    #print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img
def f9():
    exit()

C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
background_image= tk.PhotoImage(file='img/123new.png')
background_label = tk.Label(app, image=background_image,bg="black")
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

one =tk. Label(background_label, text="WEATHER APPLICATION", fg="black",font=60)
one.pack()
two = tk.Label(background_label, text="ENTER CITY NAME IN TEXT BOX AND PRESS GET WEATHER", bg="green", fg="white",font=60)
two.pack()


frame = tk.Frame(app,  bg='lightblue', bd=2)
frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.07, anchor='n')

textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.70, relheight=1)

submit = tk.Button(frame, text='Get Weather', font=60, command=lambda: get_weather(textbox.get()))
submit.place(relx=0.7, relheight=1, relwidth=0.3)
button9 = tk.Button(app, text="EXIT", fg="red", command=f9)
button9.place(x=0,y=0)


lower_frame = tk.Frame(app, bg='#42c2f4', bd=0)
lower_frame.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.3, anchor='n')

#backg= tk.PhotoImage(file='./landscape.png')
#bgl = tk.Label(lower_frame, image=backg)
#bgl.place(x=0, y=0, relwidth=1, relheight=1)


bg_color = 'lightgreen'
results = tk.Label(lower_frame, bg=bg_color,anchor='center', justify='left', bd=4,fg="blue")
results.config(font=40)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results,bg=bg_color,bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


app.mainloop()
