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

class Attrib_Gen():

    names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi', 'Sebastian', 'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew', 'Luke', 'Asher', 'Carter', 'Julian', 'Grayson', 'Leo', 'Jayden', 'Gabriel', 'Isaac', 'Lincoln', 'Anthony', 'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles', 'Christopher', 'Jaxon', 'Maverick', 'Josiah', 'Isaiah', 'Andrew', 'Elias', 'Joshua', 'Nathan', 'Caleb', 'Ryan', 'Adrian', 'Miles']


    def make_random_name():


ade = Human(name = "ade", age = 34, aggression=9, address="montgomery road, yaba", vocal_frequency = 300) ## CLASS INSTANTIATION

print(ade.eyes)
print(ade.hair_color)
print(ade.address)
print(ade.make_sound())
shade = Human(name = "shade", age = 28, aggression=9, address="Opi Iweka road, Aba", vocal_frequency = 1400) ## CLASS INSTANTIATION

print(shade.eyes)
print(shade.hair_color)
print(shade.address)
print(shade.make_sound())