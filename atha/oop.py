# basic class

# class Human():# CLASS DEFINITION
#     pass

# ade = Human() ## CLASS INSTANTIATION

# print(ade)

# class Human():# CLASS DEFINITION WITH SOME CLASS ATTRIBUTES
#     hair_color = "red"
#     skin_color = "caramel"
#     eyes = 2
#     nose = 1
#     mouth = 1


# ade = Human() ## CLASS INSTANTIATION

# print(ade.eyes)
# print(ade.hair_color)
# print(ade.skin_color)
# kunle = Human() ## CLASS INSTANTIATION

# print(kunle.eyes)
# print(kunle.hair_color)
# print(kunle.skin_color)


# class Human():# CLASS DEFINITION WITH SOME CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES
#     hair_color = "red"
#     skin_color = "caramel"
#     eyes = 2
#     nose = 1
#     mouth = 1

#     def __init__(self, name, age, aggression, address) -> None: #INITIALIZATION FUNCTION
#         self.aggression = aggression
#         self.name = name
#         self.age = age
#         self.address = address


# ade = Human(name = "ade", age = 34, aggression=9, address="montgomery road, yaba") ## CLASS INSTANTIATION

# print(ade.eyes)
# print(ade.hair_color)
# print(ade.address)
# kunle = Human(name = "kunle", age = 28, aggression=9, address="Opi Iweka road, Aba") ## CLASS INSTANTIATION

# print(kunle.eyes)
# print(kunle.hair_color)
# print(kunle.address)

import winsound
# import random


# class Human():# CLASS DEFINITION WITH SOME CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES AND A MAKE_SOUND METHOD
#     hair_color = "red"
#     skin_color = "caramel"
#     eyes = 2
#     nose = 1
#     mouth = 1

#     def __init__(self, name, age, aggression, address, vocal_frequency) -> None: #INITIALIZATION FUNCTION
#         self.aggression = aggression
#         self.name = name
#         self.age = age
#         self.address = address
#         self.voice = vocal_frequency

#     def make_sound(self):
#         winsound.Beep(self.voice,1000)

# class Attrib_Gen():

#     names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi', 'Sebastian', 'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew', 'Luke', 'Asher', 'Carter', 'Julian', 'Grayson', 'Leo', 'Jayden', 'Gabriel', 'Isaac', 'Lincoln', 'Anthony', 'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles', 'Christopher', 'Jaxon', 'Maverick', 'Josiah', 'Isaiah', 'Andrew', 'Elias', 'Joshua', 'Nathan', 'Caleb', 'Ryan', 'Adrian', 'Miles']


#     def make_random_name(self):
#         random_fname = random.choice(self.names)
#         random_lname = random.choice(self.names)

#         return f"{random_fname} {random_lname}"
    
#     def make_random_address(self):
#         random_street = random.choice(self.names)

#         return f"No {random.randint(1,300)}, {random_street} Road, {random_street[:2].upper()}"

# atrib_gen= Attrib_Gen()


# humans = []
# for i in range(50):

#     new_human = Human(name = atrib_gen.make_random_name(), age = random.randint(20, 88), aggression=random.randint(1, 9), address=atrib_gen.make_random_address(), vocal_frequency=random.randint(400, 5000)) ## CLASS 
    
#     humans.append(new_human)


# print(humans[0].name)
# print(humans[0].age)
# print(humans[0].address)
# humans[0].make_sound()


# class Animal:

#     def __init__(self, color) -> None:
#         pass
#         self.color = color

#     def __str__(self):
#         desc = self.color
#         return desc

#     def describe(self):
#         print("Hello I am of the color : " + self.red) 

# new_animal = Animal("red")
# print(new_animal)

class Human():# CLASS DEFINITION WITH SOME CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES AND A MAKE_SOUND METHOD
    hair_color = "red"
    skin_color = "caramel"
    eyes = 2
    nose = 1
    mouth = 1

    def __init__(self, name, age, aggression, address, vocal_frequency) -> None: #INITIALIZATION FUNCTION
        self.aggression = aggression
        self.name = name
        self.age = age
        self.address = address
        self.voice = vocal_frequency

    def make_sound(self):
        winsound.Beep(self.voice,1000)

class Warrior(Human):

    shield = True
    sword = True

    def __init__(self, name, age, aggression, address, vocal_frequency) -> None:
        super().__init__(name, age, aggression, address, vocal_frequency)

    def make_sound(self):
        for i in range(self.aggression//3):
             super().make_sound()


ogbuefi = Warrior("ogbuefi", 30, 6, "No 10, Salami str", 500)
print(ogbuefi.name)
print(ogbuefi.make_sound())
# kunle = Human("kunle", 30, 6, "No 10, Salami str", 500)
# print(kunle.name)
# print(kunle.make_sound())