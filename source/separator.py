def add_space_before_and_after_special_characters(file_path, characters_list):
    try:
        with open(file_path, "r") as f:
            chaine = f.read()
            
        for cle in characters_list:
           for i in range(len(chaine)):
                if chaine[i] == cle:
                    if i != 0 and i != len(chaine)-1 and chaine[i-1] != " " and chaine[i+1] != " ":
                        chaine = chaine[:i] + " " + chaine[i] + " " + chaine[i+1:]
                    elif i!=0  and chaine[i-1] != " ":
                        chaine = chaine[:i] + " " + chaine[i:]
                    elif i!=len(chaine) and chaine[i+1] != " ":
                        chaine = chaine[:i+1] + " " + chaine[i+1:]

        with open(file_path+"spaced", "w") as f:
            f.write(chaine)
        
    except IOError:
        print("Erreur lors de la lecture ou de l'écriture du fichier.")

