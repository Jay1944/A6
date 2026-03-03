"""
Name - Jaydeep Shah
NSID - LDB845
Student Number - 11436148
Professor - Kemin Wang 
"""
def record(species,type,level):
    pokemon_new = {"Species":species , "Type" : type , "Level" : level}
    return pokemon_new

def main():

    PokeDex = []
    print("Welcome to PokeDex Logger !")
    print("Enter your newly caught Pokemon")
    species = input("Pokemon's species: ")
    type = input("Type of your pokemon?: ")
    level = int(input("Level of your Pokemon?: "))
    PokeDex.append(record(species,type,level))
 
    #Using Try and except to get a valid input while adding more pokemon.
    while True:
        print("----------")
 
        while True:
            try:
                more_or_not = str(input("Are there More Pokemon Do you want to add? (y/n)"))
            except:
                print("Please enter your response again")
                continue
            if more_or_not in ["y","Y","n","N"]:
                break
            else:
                print("Please enter your response again")
                continue

        if more_or_not in ["n","N"]:
            break

        else:
            species = input("Pokemon's species: ")
            type = input("Type of your pokemon?: ")
            level = int(input("Level of your Pokemon?: "))
            PokeDex.append(record(species,type,level))
 
    print("Logging Complete. Printing Final PokeDex --")
    print(PokeDex)

main()    

    