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


def modify_file_to_single_line(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    modified_content = content.replace('\n', ' ')

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(modified_content)

