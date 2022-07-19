import re


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._orders = []
        self._inventory = { **self.MINIMUM_INVENTORY }

    def add_new_order(self, customer, order, day):
        mockedInventory = { **self._inventory }
        for ingredient in self.INGREDIENTS[order]:
                mockedInventory[ingredient] -= 1
        for ingredient in mockedInventory:
            if mockedInventory[ingredient] < 0:
                return False
        for ingredient in self.INGREDIENTS[order]:
                self._inventory[ingredient] -= 1
        return self._orders.append({'cliente': customer, 'pedido': order, 'dia': day})

    def get_quantities_to_buy(self):
        newDict = {}
        for ingredient in self.MINIMUM_INVENTORY:
            newDict[ingredient] = self.MINIMUM_INVENTORY[ingredient] - self._inventory[ingredient]
        return newDict
    
    def get_available_dishes(self):
        invalidRecipes = set()
        allRecipes = set()
        for recipe in self.INGREDIENTS:
            allRecipes.add(recipe)
            mockedInventory = { **self._inventory }
            for ingredient in self.INGREDIENTS[recipe]:
                mockedInventory[ingredient] -= 1
                if mockedInventory[ingredient] < 0:
                    invalidRecipes.add(recipe)
        return allRecipes.difference(invalidRecipes)
            