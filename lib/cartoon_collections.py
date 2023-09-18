CHEESES = ["camembert", "gouda", "cheddar"]

def roll_call_dwarves(dwarves):
    x = 1
    for i in dwarves:
        print(f'{x}. {i}')
        x += 1

def summon_captain_planet(planeteer_calls):
    return [f'{call.title()}!' for call in planeteer_calls]

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
        
    return False

def find_the_cheese(foods):
    for food in foods:
        if food in CHEESES:
            return food
    
    return None

roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])
summon_captain_planet(["Doc", "Dopey", "Bashful", "Grumpy"])