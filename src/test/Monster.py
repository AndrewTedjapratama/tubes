from src.helpers.CSV import pisah, read_csv_file

# Functions 
def base_attribute(monster_id):
    monster = read_csv_file(r'data/csv/monster.csv')
    type = monster[monster_id][1]
    atk_power = monster[monster_id][2]
    def_power = monster[monster_id][3]
    hp = monster[monster_id][4]
    base_attribute = [type, atk_power, def_power, hp]
    return base_attribute

def get_attribute_with_level(level, base_attribute):
    multiplier = 1 + ((level-1)*0.1)
    base_attribute[1] *= multiplier
    base_attribute[2] *= multiplier
    base_attribute[3] *= multiplier
    return base_attribute


def potion(atk_power, def_power, potion_type, base_hp):
    hp = base_hp
    if (potion_type.lower() == 'strength'):
        atk_power *= 1.05
    elif (potion_type.lower() == 'resilience'):
        def_power *= 1.05
    elif (potion_type.lower() == 'healing'):
        hp = min(hp + 0.25*base_hp, base_hp)
    return [atk_power, def_power, hp] 


def show_drink_potion(potion_type, monsterName):
    effect = "ATK Power increased by 5%"
    if (potion_type == "resilience"):
        effect = "DEF Power increased by 5%"
    if (potion_type == "healing"):
        effect = "restored 25% Health"
    return (f"{monsterName} used {potion_type} potion, {effect}")

# Test
print(base_attribute(1))
print(potion(500, 200, 'strength', 100))
print(show_drink_potion('strength', 'Ambatron'))
a#a

