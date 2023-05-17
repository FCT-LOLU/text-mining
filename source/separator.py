def add_space_before_and_after_special_characters(file_path, characters_list):
    try:
        with open(file_path, "r") as f:
            chaine = f.read()
            
        for cle in characters_list:
            chaine = chaine.replace(cle, " ")
        chaine = chaine.replace("  ", " ")
        chaine = chaine.lower()
        with open(file_path, "w") as f:
            f.write(chaine)
        
    except IOError:
        print("Erreur lors de la lecture ou de l'écriture du fichier.")

#add_space_before_and_after_special_characters("test.txt", [";", ",", ".", ":", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "+", "=", "*", "&", "^", "%", "$", "#", "@", "!", "`", "~", "'", "\"", " "])