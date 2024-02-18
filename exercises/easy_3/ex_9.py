
def clean_up(_str: str):
    new_str = ""
    for char in _str:
        if char.isalpha():
            new_str += char
        elif not new_str.endswith(" "):
            new_str += " "
    return new_str

print(clean_up("---what's my +*& line?") == " what s my line ")
