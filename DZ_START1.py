class Hero:

    def __init__(self, name, rank, power):
        self.name = name
        self.health = 100
        self.rank = rank
        self.power = power

    def get_power(self):
        return f'GET POVER {self.name} : {self.__power}'

    def set_power(self, value):
        value = self.__health
        self.__power = value * 0.10
        return self.__power

    def get_rank(self):
        return f'GET RANK {self.name} : {self.__rank}'

    def set_rank(self, value):
        if value in range(1, 4):
            self.__rank = value
            f'GET RANK {self.name} : {self.__rank}'
        else:
            raise Exception

    def get_health(self):
        return f'GET HEALTH {self.name} : {self.__health}'

    def set_health(self, value):
        if 0 <= value <= 100:
            self.__health = value
        else:
            self.__health = 0

    def hit(self, other_hero):
        damage = 7
        if other_hero.__health <= 5:
            print(f'{other_hero.name} is done, health is {other_hero.__health}')
        else:
            print(f'Hero {self.name} hit {other_hero.name}')
            other_hero.__health = other_hero.__health - damage
            other_hero.__power = other_hero.__health * 0.1
            print(f'Hero {other_hero.name} health left: {other_hero.__health} ')

    health = property(get_health, set_health)
    rank = property(get_rank, set_rank)
    power = property(get_power, set_power)

hero1 = Hero('Hero1', 1, 10)
hero2 = Hero('Hero2', 3, 10)

# hero1.hit(hero2)
# print(hero2.health)
# print(hero2.rank)


print(hero2.power)
hero1.hit(hero2)
print(hero2.health)
print(hero2.power)
print('fight !')
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
hero1.hit(hero2)
print(hero2.power)