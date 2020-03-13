def normalize_string(string:str):
    for target in ("-", "_", "'"):
        string = string.replace(target, " ")
    string = " ".join(string.split())
    string = string.upper()
    return string