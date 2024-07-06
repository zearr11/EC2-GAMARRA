

def fcForm1(z1,z2):
    if z1 == z2:
        return z1*z2
    else:
        if z1 > z2:
            return z1-z2
        else:
            return z1+z2

def fcForm2(z1,z2):
    if z1 == z2:
        return "SE MULTIPLICAN: "
    else:
        if z1 > z2:
            return "EL PRIMERO ES MAYOR, SE RESTAN:"
        else:
            return "NO CUMPLEN NINGUNA CONDICION, SE SUMAN:"