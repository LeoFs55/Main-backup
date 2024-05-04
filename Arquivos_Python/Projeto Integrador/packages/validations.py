def num_validation(entrada):
    try:
        num = int(entrada)
        return True, num
    except ValueError:
        return False, ValueError