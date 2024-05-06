def first_name_validation(name):
    valid_name = name.isalpha()
    if valid_name:
        return True
    return False

def rep_first_letter(name):
    if first_name_validation(name):
        quant = len(name)
        rep_letter = name[:1]*quant
        if name != rep_letter:
            return True
        return False

def name(name):
    if first_name_validation(name) and rep_first_letter(name):
        return name.lower()
    return 'Nome Invalido'

def surname(surname):
    surnames = surname.split()
    validations_surname = list()
    for i in surnames:
        validations_surname.append(first_name_validation(i))
        validations_surname.append(rep_first_letter(i))
    return 'sobrenome invalido' if False in validations_surname else surname.lower()