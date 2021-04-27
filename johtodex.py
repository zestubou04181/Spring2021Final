import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import webbrowser
import urllib3
from io import BytesIO

# GUI Window
window = tk.Tk()
window.geometry("700x700")
window.title("Zamir Shelton Final Pokedex Project")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Zamir's Omnibus Pokedex")
title_label.config(font=("Arial", 32), fg="red")
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack()

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

# FUNCTION
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image = img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=f"{pokemon.types}")

# FEATURES INSIDE GUI WINDOW
def callback(url):
    webbrowser.open_new(url)

label_id_name = tk.Label(window, text = "Enter Pokemon Dex ID or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text= "Load Pokemon", command=load_pokemon)
#INSERT: ", command=load_pokemon)" inside above function
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

link1= tk.Label(window, text="Take me to a battle!", bg="#EE1515", cursor="hand2")
link1.config(font=("Impact", 30))
link1.pack(padx=20, pady=20)
link1.bind("<Button-1>", lambda e: callback("https://pokemonshowdown.com"))

link2= tk.Label(window, text="Quiz Me!", bg="#FF8533",
                fg="white", cursor="hand2")
link2.config(font=("Arial", 20))
link2.pack(padx=10, pady=10)
link2.bind("<Button-1>", lambda e: callback("https://www.sporcle.com/search/quizzes/?s=pokemon"))


# MUST BE AT END OF PROGRAM
window.mainloop()
