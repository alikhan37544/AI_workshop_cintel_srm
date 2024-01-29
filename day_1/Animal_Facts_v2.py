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

def is_warm_blooded(animal):
    if animal["type"] == "mammal":
        return True
    else:
        return False

def is_pet(animal):
    if animal["domesticated"] == True:
        return True
    else:
        return False

# Query examples
for animal_name, animal_info in animal_facts.items():
    print(f"Animal: {animal_name}")
    print(f"Type: {animal_info['type']}")
    print(f"Domesticated: {animal_info['domesticated']}")
    print(f"Lifespan: {animal_info['lifespan']} years")
    print(f"Weight: {animal_info['weight']} kg")
    print(f"Height: {animal_info['height']} ft")
    print(f"Is warm blooded: {is_warm_blooded(animal_info)}")
    print(f"Is a pet: {is_pet(animal_info)}")
    print("\n")