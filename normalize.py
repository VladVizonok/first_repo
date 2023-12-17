import re 


def normalize(file_name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}
    for key, value in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(key)] = value
        TRANS[ord(key.upper())] = value.upper()

    file_name, *extencion = file_name.name.split('.')
    new_file_name = re.sub(r'\W', '_', file_name).translate(TRANS)

    return f"{new_file_name}.{'.'.join(extencion)}"

