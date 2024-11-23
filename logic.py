from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(200, 400)
        self.power = randint(30, 50)
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
        

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(minutes=feed_interval)   
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  
        
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
                chance = randint(1,3)
                if chance == 1:
                    return "Покемон-волшебник применил магический щит в сражении🪄"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}\n" +\
                   f"@{self.pokemon_trainer} нанес {self.power} урона\n" +\
                   f"Здоровье @{enemy.pokemon_trainer} {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}\nЗдоровье:{self.hp}\nУрон:{self.power}\n'Защита:{self.defense}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
  
class Wizard(Pokemon):
    def info(self):
        return super().info() + '\nУ тебя покемон волшебник'
    
    def feed(self, feed_interval=10, hp_increase=10):
        return super().feed(feed_interval, hp_increase)

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(1,15)
        # увеличиваем атаку
        self.power += super_power
        # применяем родительский метод
        result =  super().attack(enemy)
        self.power -= super_power
        return 'была применена суперсила🔥\n' + result
    
    def info(self):
        return super().info() + "\nУ тебя покемон боец"
    
    def feed(self, feed_interval=20, hp_increase=20):
        return super().feed(feed_interval, hp_increase)
        


pok_1 = Fighter('123')
print(pok_1.info())
pok_2 = Wizard('1234')
print(pok_2.info())
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
print(pok_1.attack(pok_2))
