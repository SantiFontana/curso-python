ingreso_mensual = 1200
gasto_mensual = 800

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien")
    else:
        print("Estas gastando una banda, no se si te alcanza")
        
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamerica")
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 600:
        print("Estas bien")
    else:
        print("Estas gastando una banda, no se si te alcanza")
    
elif ingreso_mensual > 500:
    print("Estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")
    
else:
    print("Sos pobre")


# otro ejemplo sobre temperatura
temperatura = 10

if temperatura > 30:
    print("Cuidado, hace muchisimo calor")
elif temperatura > 20:
    print("Hace buena temperatura")
elif temperatura > 0:
    print("Hace frio")
elif temperatura <= 0:
    print("QUE FRIO")
else:
    print("Dato no valido")