def main():
    numero1 = int(input("primeriro numero"))
    numero2 = int(input("segundo numero"))

    if numero1 < numero2:
        print(numero1, "maior que", numero2)
    else:
        print(numero2, "maior que", numero1)

    if numero2 < numero1:
        print(numero2, "maior que", numero1)
    else:
        print(numero1, "maior que", numero2)


if __name__ == '__main__':
    main()