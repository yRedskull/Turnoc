def val_isnumber(inp):
    try:
        if inp == "":
            return True
        int(inp)
        return True
    except ValueError:
        return False
