import pandas as pd
import tkinter as tk
from tkinter import ttk

df = pd.read_csv('pokemon.csv')


class Pokemon:
    def __init__(self, index):
        self.name = df.iloc(0)[index][1]
        self.type = df.iloc(0)[index][2]
        self.hp = df.iloc(0)[index][5]
        self.attack = df.iloc(0)[index][6]

    def __str__(self):
        return f"Name: {self.name}\nType: {self.type}\nHP: {self.hp}\nAttack: {self.attack}"


# TO-DO: add a button to call the pokemon class and display stats.
class ComboBox:
    def __init__(self, parent):
        pokemonList = []
        for i in range(len(df.index)):
            pokemonList.append(df.iloc(0)[i][1])
        self.parent = parent
        self.string_var = tk.StringVar()
        self.box = ttk.Combobox(parent, width=40, values=pokemonList, textvariable=self.string_var)


class App:
    def __init__(self, parent):
        self.title = tk.Label(parent, font=("Times New Roman", 14), text='Pokemon:')
        self.combobox = ComboBox(parent)
        self.button = tk.Button(parent, width=10, text="Submit", command=self.submit)
        self.textbox = tk.Text(parent, width=59, height=8, font=("Times New Roman", 14), state='disabled')

        self.textbox.place(x=10, y=40)
        self.combobox.box.grid(column=1, row=1, padx=20, pady=5)
        self.button.grid(column=2, row=1, padx=5, pady=5)
        self.title.grid(column=0, row=1, padx=5, pady=5)
        self.frame = tk.Frame(parent, width=200, height=400)

    def submit(self):
        pokemonIndex = df[df['Name'] == self.combobox.string_var.get()].index[0]
        pokemon = Pokemon(pokemonIndex)
        text = f'''Name: {pokemon.name}        Type: {pokemon.type}   
            
Attack: {pokemon.attack}        HP: {pokemon.hp}
        '''
        self.textbox.configure(state='normal')
        self.textbox.delete('1.0', 'end')
        self.textbox.insert('end', text)
        self.textbox.configure(state='disabled')


root = tk.Tk()
obj = App(root)
root.geometry('{}x{}'.format(500, 200))
root.resizable(width=False, height=False)
root.mainloop()

