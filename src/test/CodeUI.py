import csv
from io import StringIO

data = """id;type;atk_power;def_power;hp
1;Kaori;700;30;1500
2;Wiratama;450;45;2000
3;Sagiri;600;25;1800
4;Aldoy;800;10;1200
5;Joko;500;40;1600
6;Nameless;750;20;1400
7;Letz;550;35;1750
8;FarizPancong;650;15;1400
9;Lickman;480;50;2200
10;Fathurwithyou;850;5;1000"""

# Parse the CSV data into a dictionary
def parse_data(data):
    file_like = StringIO(data)
    reader = csv.DictReader(file_like, delimiter=';')
    characters = {row['id']: row for row in reader}
    return characters

# Main function to run the user interface
def main():
    characters = parse_data(data)

    while True:
        print("Masukkan ID:")
        id_input = input()
        if id_input.lower() == 'exit':
            break
        elif id_input in characters:
            character = characters[id_input]
            print("=====================================================================")
            print(f"                             {character['type']}            ")
            print("=====================================================================")
            print(f"Atk : {character['atk_power']}")
            print(f"Def: {character['def_power']}")
            print(f"HP: {character['hp']}")
            print("====================================================================\n")
        else:
            print("ID not found. Please try again.\n")

if __name__ == "__main__":
    main()
