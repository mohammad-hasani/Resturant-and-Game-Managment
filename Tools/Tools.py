def validation_text(*args):
    for i in args:
        if len(str(i).strip()) == 0:
            return False
    return True

def set_error_text(*args):
    for i in args:
        i.setText('Enter Here...')