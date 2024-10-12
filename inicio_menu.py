
import first_funtion
import second_funtion
import third_funtion
import fourth_funtion

print(f'''
      EJEMPLO DE MENÚ:
      1 -> first funtion
      2 -> second funtion
      3 -> third funtion
      4 -> fourth funtion
      ''')


while True:
  try:
    
    ingresar = int(input("Ingrese opción: "))
    
    if ingresar == 1:
      first_funtion.mostrando_print()
    elif ingresar == 2:
      second_funtion.mostrando_print()
    elif ingresar == 3:
      third_funtion.mostrando_print()
    elif ingresar == 4:
      fourth_funtion.mostrando_print()
    
    else:
      print("Ingrese opciones permitidas...")

  
  except:
    raise ValueError(f'''
                     
  ---------------------------------------------
  ERROR: ingresó valores no especificados.\n  Saliendo...
  ---------------------------------------------
                     ''')
    break
    
  finally:
    pass

