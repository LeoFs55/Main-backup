def first_name_validation(name):
    valid_name = name.isalpha()
    if valid_name:
        return True
    return False

def rep_first_letter(name):
    if first_name_validation(name):
        quant = len(name)
        rep_letter = (name[:1] for i in range(quant))
        if name != rep_letter:



first_name_validation('')