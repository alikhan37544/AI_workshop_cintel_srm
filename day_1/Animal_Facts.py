animal_facts = {
    "dog": {"type": "mammal", "domesticated" : True, "lifespan": 10, "weight": 50, "height": 2},
    "cat": {"type": "mammal", "domesticated" : True, "lifespan": 15, "weight": 10, "height": 1},
    "lion": {"type": "mammal", "domesticated" : False, "lifespan": 12, "weight": 200, "height": 4},
    "tiger": {"type": "mammal", "domesticated" : False, "lifespan": 10, "weight": 150, "height": 3},
    "elephant": {"type": "mammal", "domesticated" : False, "lifespan": 60, "weight": 1000, "height": 10},
    "giraffe": {"type": "mammal", "domesticated" : False, "lifespan": 25, "weight": 500, "height": 6},
    "zebra": {"type": "mammal", "domesticated" : False, "lifespan": 20, "weight": 300, "height": 5},
    "horse": {"type": "mammal", "domesticated" : True, "lifespan": 30, "weight": 700, "height": 6},
}

# Rules to determine if an animal is warm-blooded
def is_warm_blooded(animal):
    if animal["type"] == "mammal":
        return True
    else:
        return False
    
# Rules to determine if an animal is a pet
def is_pet(animal):
    if animal["domesticated"] == True:
        return True
    else:
        return False

# Query examples
print(is_warm_blooded(animal_facts["dog"]))
print(is_pet(animal_facts["dog"]))
print(is_warm_blooded(animal_facts["lion"]))
print(is_pet(animal_facts["lion"]))
    


