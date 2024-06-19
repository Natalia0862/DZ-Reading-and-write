import os
import pprint

with open("recipes.txt") as file:
    cook_book = {}

    for k in file:
        ingridients = []
        recept_name = k.strip()
        ingridients_count = file.readline().strip()
        cook_book[recept_name] = ingridients
        
        for p in range(int(ingridients_count)):
            recepie = file.readline().strip().split(" | ")
            product, quantity, weight = recepie
            ingridients.append({"Ингридиент": product, "количество": quantity, "единица измерения": weight})
        file.readline()
    cook_book[recept_name] = ingridients

    pprint.pprint(cook_book)

    pprint.pprint(ingridients)
