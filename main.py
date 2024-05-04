import tkinter as tk
import requests
import time
def getWeather(canvas):

 city = textField.get()

 api = "https://api.openweathermap.org/data/2.5/weather?q= " + city + " &appid=3426caee0f678fc56d849f7210b8d9ec"
 api2="https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=ac64cca3bd95540319ae03e084683a86"

 json_data = requests.get(api).json()
 json_data2 = requests.get(api2).json()

 condition = json_data['weather'][0]['main']

 temp = int(json_data['main']['temp'] - 273.15)

 min_temp = int(json_data['main']['temp_min'] - 273.15)

 max_temp = int(json_data['main']['temp_max'] - 273.15)

 pressure = json_data['main']['pressure']

 humidity = json_data['main']['humidity']

 wind = json_data['wind']['speed']

 sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] -21600))

 sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] -21600))

 final_info = condition + "\n" + str(temp) + "°C"
 final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
 max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
 humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset +"\n"
 Date_txt_one = (json_data2['list'][4]['dt_txt'])
 weather_temp_one = round(json_data2['list'][4]['main']['temp'] - 273.15)
 weather_description_one = (json_data2['list'][4]['weather'][0]['description'])

 Date_txt_sec = (json_data2['list'][11]['dt_txt'])
 weather_temp_sec = round(json_data2['list'][11]['main']['temp'] - 273.15)
 weather_description_sec = (json_data2['list'][11]['weather'][0]['description'])
 Date_third = (json_data2['list'][19]['dt_txt'])
 temp_third = round(json_data2['list'][19]['main']['temp'] - 273.15)
 weather_description_third = (json_data2['list'][19]['weather'][0]['description'])
 Date_txt_fourth = (json_data2['list'][27]['dt_txt'])
 weather_temp_fourth =round (json_data2['list'][27]['main']['temp'] - 273.15)
 weather_description_fourth = (json_data2['list'][27]['weather'][0]['description'])
 Date_txt_five = (json_data2['list'][35]['dt_txt'])
 weather_temp_five = round(json_data2['list'][35]['main']['temp'] - 273.15)

 weather_description_five = (json_data2['list'][35]['weather'][0]['description'])
 Date_txt_six = (json_data2['list'][39]['dt_txt'])
 weather_temp_six = round(json_data2['list'][39]['main']['temp'] - 273.15)
 weather_description_six = (json_data2['list'][39]['weather'][0]['description'])
 one_info = "\n" + "Date: " + str(Date_txt_one) + ", Temperature: " + str(
 weather_temp_one) + "°C" + ", Description: " + str(weather_description_one)
 sec_info ="\n" + "Date: " + str(Date_txt_sec) + ", Temperature: " + str(weather_temp_sec) + "°C" + ", Description: " + str(weather_description_sec)
 third_info ="\n" + "Date: " + str(Date_third) + ", Temperature: " + str(temp_third) + "°C" + ", Description: " + str(weather_description_third)
 four_info ="\n" + "Date: " + str( Date_txt_fourth) + ", Temperature: " + str(weather_temp_fourth) + "°C" + ", Description: " + str(weather_description_fourth)

 five_info = "\n" + "Date: " + str(Date_txt_five) + ", Temperature: " + str(weather_temp_five) + "°C" + ", Description: " + str(weather_description_five)
 six_info = "\n" + "Date: " + str(Date_txt_six) + ", Temperature: " + str(
 weather_temp_six) + "°C" + ", Description: " + str(weather_description_six)

 label.config(text=final_info)
 label1.config(text=final_data)
 label2.config(text=one_info)
 label3.config(text=sec_info)
 label4.config(text=third_info)
 label5.config(text=four_info)
 label6.config(text=five_info)
 label7.config(text=six_info)

canvas = tk.Tk()

canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 10, "bold")
t = ("poppins", 15, "bold")
g = ("poppins",28, "bold")
canvas['background'] = "pink"
textField = tk.Entry(canvas, justify='center', width=20, font=g )
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)
label0 = tk.Label(canvas, font=g,fg="green",bg="pink")
label0.pack()
label1 = tk.Label(canvas, font=t,fg="black",bg="pink")
label1.pack()
label= tk.Label(canvas,text="6 Day Forecast", font=g,fg="brown",bg="pink")
label.pack()
label2 = tk.Label(canvas, font=f,fg="black",bg="pink")
label2.pack()
label3 = tk.Label(canvas, font=f,fg="black",bg="pink")
label3.pack()

label4 = tk.Label(canvas, font=f,fg="black",bg="pink")
label4.pack()
label5 = tk.Label(canvas,font=f,fg="black",bg="pink")
label5.pack()
label6 = tk.Label(canvas,font=f,fg="black",bg="pink")
label6.pack()
label7 = tk.Label(canvas,font=f,fg="black",bg="pink")
label7.pack()
canvas.mainloop()

