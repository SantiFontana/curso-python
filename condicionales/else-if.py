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
