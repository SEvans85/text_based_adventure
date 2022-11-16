hero, name, weapon, items, health_points = '', '', '', [], ''

def choose_hero():
    global hero, name, weapon, items, health_points
    choose = input("Choose you hero: Archer, Mage or Warrior: ")
    heroes = {
        'mage' : {
            'name' : 'Electra',
            'weapon' : 'Wand',
            'items' : ['10 gold pieces', '1x health potion', '2 x mana potion'],
            'health points' : 10
            },
        'warrior' : {
            'name' : 'Zeus',
            'weapon' : 'Battle Axe',
            'items' : ['15 gold pieces', '2x health potion', 'shield', 'sword'],
            'health points' : 20
            },
        'archer' : {
            'name' : 'Laergo',
            'weapon' : 'bow',
            'items' : ['arrows', '3x health potion', 'anti-poison', 'diamond'],
            'health points' : 15
            }
        }
    if choose.lower() == 'mage':
        hero = list(heroes.keys())[0]
    elif choose.lower() == 'warrior':
        hero = list(heroes.keys())[1]
    elif choose.lower() == 'archer':
        hero = list(heroes.keys())[2]
    
    name = heroes[choose]['name']
    weapon = heroes[choose]['weapon']
    items = heroes[choose]['items']
    health_points = heroes[choose]['health points']
    

choose_hero()

print(f"You chose the {hero.capitalize()}!")
print(f'Your name is: {name}, Your weapon of choice is: {weapon} and you have {health_points} health points.')
print(f'Your backpack contains the following items: ')
for i in items:
    print(f'\t{i}')