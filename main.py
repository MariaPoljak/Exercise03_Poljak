#count_vowels(text)

def count_vowels(text):
    if type(text) != str:
        return 42
    count = 0
    vowels = set("aeiouAEIOU")
    for alphabet in text:
       if alphabet in vowels:
            count = count + 1
    return count and print("Your string contains {} vowel(s).".format(count))


#hamming(text1, text2)

def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    distance = 0
    for index in range(len(text1)):
        if text1[index] != text2[index]:
            distance = distance + 1
    return distance and print('The hamming distance is:{}'.format(distance))


#Vehicle_Car_Bus

class Vehicle:
    def __init__(self, color: str, fuel_type: str):
        self.color = color
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color: str, fuel_type: str, doors):
        Vehicle.__init__(self, color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color:{self.color}, Fuel Type:{self.fuel_type}, Doors:{self.doors}"

class Bus(Vehicle):
    def __init__(self, color: str, fuel_type: str, passengers):
        Vehicle.__init__(self,color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color:{self.color}, Fuel Type:{self.fuel_type}, Passenger:{self.passengers}"


#Book

class Book:
    def __init__(self, name = str, author = str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"


#Bookshelf

class Bookshelf:
    def __init__(self, books = list, author = str):
        self.books = books
        self.author = author

    def add_book_list(self, books):
        self.books.append(books)

    def get_books(self):
        return self.books

    def clear_shelf(self):
        self.books = []