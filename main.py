from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim  
from tkinter import ttk,messagebox
# noinspection PyUnresolvedReferences
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests
import pytz

root = Tk()
root.title("weather App")
root.geometry("900x500+300+200")   #set the size of the window screen
root.resizable(False,False)

#getweather function

def getWeather():
    
    try:
        city=textfield.get()
        
        '''geolocator = Nominatim(user_agent="geoapiExercises")
        
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        '''
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=28d00a96f0a71f650ed38d49d98e5b79"
        json_data = requests.get(api).json()
        
        
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror("Weather App","Enter Correct city name!!")
        
        
#SEARCH BOX
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)                        #search image location

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

sc=ttk.Combobox(root,text="list_name",values=list_name,font=("time new roman",30,"bold"))
sc.place(x=500,y=20,width=150)    

#textfield
textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")         #font of textfield
textfield.place(x=50,y=40)                      #location of searchfield
textfield.focus()                                #for showing cursor in text field


#search_icon   #button
search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)             #@@@@@@@@@@@@@@@@@@@@@@@@@@22222
myimage_icon.place(x=400,y=34)


#LOGO
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#TIME
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)




#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="#1ab5ef")   #fg='white',bg='#1ab5ef'
label1.place(x=120,y=400)


label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="#1ab5ef")   
label2.place(x=250,y=400)


label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="#1ab5ef")   
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="#1ab5ef")   
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()







#PS I:\PythonProject\WeatherAPI> & C:/Users/ISHIKA/AppData/Local/Programs/Python/Python310/python.exe i:/PythonProject/WeatherAPI/main.py
#Exception in Tkinter callback
#Traceback (most recent call last):
  #File "C:\Users\ISHIKA\AppData\Local\Programs\Python\Python310\lib\site-packages\geopy\geocoders\base.py", line 368, in _call_geocoder
   # result = self.adapter.get_json(url, timeout=timeout, headers=req_headers)
  #File "C:\Users\ISHIKA\AppData\Local\Programs\Python\Python310\lib\site-packages\geopy\adapters.py", line 472, in get_json
   # resp = self._request(url, timeout=timeout, headers=headers)
  #File "C:\Users\ISHIKA\AppData\Local\Programs\Python\Python310\lib\site-packages\geopy\adapters.py", line 500, in _request
 #   raise AdapterHTTPError(
#geopy.adapters.AdapterHTTPError: Non-successful status code 403

#The above exception was the direct cause of the following exception:
#
#Traceback (most recent call last):
  #File "C:\Users\ISHIKA\AppData\Local\Programs\Python\Python310\lib\tkinter\__init__.py", line 1921, in __call__
 #   return self.func(*args)
 #   return self._call_geocoder(url, callback, timeout=timeout)
 # File "C:\Users\ISHIKA\AppData\Local\Programs\Python\Python310\lib\site-packages\geopy\geocoders\base.py", line 388, in _call_geocoder
  #  res = self._adapter_error_handler(error)
 # File "C:\Users\ISHIKA\AppData\Local\Programs\Python\Python310\lib\site-packages\geopy\geocoders\base.py", line 411, in _adapter_error_handler
 #   raise exc_cls(str(error)) from error
#geopy.exc.GeocoderInsufficientPrivileges: Non-successful status code 403 '''