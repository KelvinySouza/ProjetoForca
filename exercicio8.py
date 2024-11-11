def main():
    sexo = input("qual é seu sexo, f ou m ?")

    match sexo.lower(): 
        case "m":
            print("masculino")
        case "f":
            print("feminino")
        case _:
            print("sexo invalido")
            
if __name__ == '__main__':
    main()