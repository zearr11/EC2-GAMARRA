

def PromNota(v1,v2,v3,v4):
    totalnt = [v1,v2,v3,v4]
    totalnt.remove(min(totalnt))
    formu = (totalnt[0] * 0.2) + (totalnt[1] * 0.3) + (totalnt[2] * 0.5)    
    promFinal = formu / 3
    return promFinal