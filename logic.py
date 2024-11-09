from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.attack = self.get_attack()
        self.defense = self.get_defense()


        Pokemon.pokemons[pokemon_trainer] = self

    
    def get_defense(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][2]['base_stat']
        else:
            return 5
    
    
    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][1]['base_stat']
        else:
            return 5
    
    
    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][0]['base_stat']
        else:
            return 50


    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return "https://cdn2.vectorstock.com/i/1000x1000/32/36/cartoon-broken-heart-vector-4613236.jpg"

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def show_hp(self):
        return f'HP: {self.hp}'
    def show_attack(self):
        return f'Attack: {self.attack}'
    def show_defense(self):
        return f'Defense: {self.defense}'



