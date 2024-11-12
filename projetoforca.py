import random

def escolher_palavra():
    """
    Escolhe uma palavra aleat ria da lista de palavras.
    """
    # Lista de palavras
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogo', 'forca']
    # Escolher uma palavra
    return random.choice(palavras)

def exibir_forca(tentativas):
    
    estagios = [
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        ''',
        '''
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        ''',
        '''
           -----
           |   |
           |   O
           |  /|
           |
           |
        ''',
        '''
           -----
           |   |
           |   O
           |
           |
           |
        ''',
        '''
           -----
           |   |
           |
           |
           |
           |
        ''',
        '''
           -----
           |
           |
           |
           |
           |
        ''',
    ]
    return estagios[6 - tentativas]

def jogar():

    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6
    vitoria = False

    print("Bem-vindo ao jogo da forca!")

    while not vitoria and tentativas > 0:
        # Mostra a forca
        print(exibir_forca(tentativas))
        # Mostra a palavra com as letras adivinhadas
        print("Palavra: ", end=' ')
        for letra in palavra:
            if letra in letras_adivinhadas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print()

        # Pede uma letra ao usu rio
        tentativa = input("Adivinhe uma letra: ").lower()

        # Verifica se a letra j  foi tentada
        if tentativa in letras_adivinhadas:
            print("Você j  tentou essa letra. Tente outra.")
        # Verifica se a letra esta  na palavra
        elif tentativa in palavra:
            letras_adivinhadas.append(tentativa)
            print("Boa! A letra est  na palavra.")
        else:
            # Decrementa as tentativas
            tentativas -= 1
            letras_adivinhadas.append(tentativa)
            print("Ops! A letra não esta na palavra.")

        # Verifica se todas as letras foram adivinhadas
        if all(letra in letras_adivinhadas for letra in palavra):
            vitoria = True

    # Mostra o resultado final
    if vitoria:
        print(f"Parabéns! Voc  adivinhou a palavra: {palavra}")
    else:
        print(exibir_forca(tentativas))
        print(f"Você perdeu! A palavra era: {palavra}")

if __name__== "__main__":
    jogar()