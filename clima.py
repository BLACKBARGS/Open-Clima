import os
from tkinter import Tk, Text, messagebox, StringVar, font
from tkinter import ttk
import requests

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

def get_weather(city_name):
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(complete_url)
    return response.json()

def format_weather_data(weather_data):
    try:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temperature = int(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        formatted_data = (
            f"Cidade: {city}, {country}\n"
            f"Temperatura: {temperature}°C\n"
            f"Umidade: {humidity}%\n"
            f"Pressão: {pressure} hPa\n"
            f"Velocidade do Vento: {wind_speed} m/s\n"
            f"Condição: {description.capitalize()}"
        )
        return formatted_data
    except KeyError:
        return "Não foi possível formatar os dados do tempo."

def fetch_and_display_weather():
    city_name = city_name_var.get()
    weather_data = get_weather(city_name)
    if weather_data['cod'] != 200:
        messagebox.showerror("Erro", "Não foi possível obter os dados do tempo.")
    else:
        formatted_weather_data = format_weather_data(weather_data)
        text_area.config(state='normal')
        text_area.delete('1.0', 'end')
        text_area.insert('end', formatted_weather_data)
        text_area.config(state='disabled')
        messagebox.showinfo("Sucesso", f"Dados do tempo para {city_name} exibidos com sucesso.")

def save_weather_data(city_name, data):
    directory_name = f"./weather_data/{city_name}"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    file_path = os.path.join(directory_name, "weather_data.txt")
    with open(file_path, 'w') as file:
        file.write(str(data))

app = Tk()
app.title("Tempo Atual")
app.geometry("700x500")

style = ttk.Style()
style.theme_use('clam')
jetbrains_mono_font = font.Font(family="JetBrains Mono", size=10)

style.configure('TLabel', font=jetbrains_mono_font)
style.configure('TButton', font=jetbrains_mono_font)
style.configure('TEntry', font=jetbrains_mono_font)

city_name_var = StringVar()
city_label = ttk.Label(app, text="Digite o nome da cidade:")
city_label.pack(pady=(20, 0))
city_entry = ttk.Entry(app, textvariable=city_name_var)
city_entry.pack(pady=10)

fetch_button = ttk.Button(app, text="Buscar Dados do Tempo", command=fetch_and_display_weather)
fetch_button.pack(pady=10)

text_area_frame = ttk.Frame(app)
text_area_frame.pack(pady=10, expand=True, fill='both')

text_area = Text(text_area_frame, height=10, width=50, state='disabled', font=jetbrains_mono_font)
text_area.pack(side='left', fill='both', expand=True)

scrollbar = ttk.Scrollbar(text_area_frame, orient='vertical', command=text_area.yview)
scrollbar.pack(side='right', fill='y')

text_area.config(yscrollcommand=scrollbar.set)

app.mainloop()
