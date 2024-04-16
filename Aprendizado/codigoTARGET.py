# 1º QUESTÃO ---------------------------------------------------------------------------

# ENREDO
# 1) Observe o trecho de código abaixo:

# int INDICE = 13, SOMA = 0, K = 0;

# enquanto K < INDICE faça

# {

# K = K + 1;

# SOMA = SOMA + K;

# }

# imprimir(SOMA);




def primeira_questao():
    indice = 13
    SOMA = 0
    K = 0

    while K < indice:

        K = K + 1;
        SOMA = SOMA + K;

    print(SOMA); # SOMA = 91


# 2º QUESTÃO  ---------------------------------------------------------------------------
# ENREDO:
# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
    
    
    

def verificaSequenciaFibonacci(numero):
    aux1, aux2 = 0, 1
    while aux2 < numero:
        aux1, aux2 = aux2, aux1 + aux2
        # print("aux1 = ", aux1)
        # print("aux2 = ", aux2)
        
    if aux2 == numero:
        return True
    else:
        return False       



def segundaquestao():    
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if verificaSequenciaFibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci")

    
# 3º QUESTÃO     ---------------------------------------------------------------------------

#3) Descubra a lógica e complete o próximo elemento:

# a) 1,3,5,7,                      9
# b) 2,4,8,16,32,                 64
# c) 0,1,4,9,16,25,36,            49
# d) 4,16,36,64,                 100
# e) 1, 1, 2, 3, 5, 8,            13
# f) 2,10, 12, 16, 17, 18, 19,   200


# 4º QUESTÃO     ---------------------------------------------------------------------------
#ENREDO
#4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?


# Ligaria um interruptor por alguns minutos (5-8 minutos) e em seguida ligaria outro interruptor. Assim, iria para as salas e concluiria que 
# se a sala que entrei está com a lâmpada acesa e quente, então o primeiro interruptor a controla 
# se a sala que entrei está com a lâmpada acesa e relativamente fria, então o segundo interruptor a controla
# se a sala que entrei está com a lâmpada apaga, então o terceiro interruptor a controla


# 5º QUESTÃO     ---------------------------------------------------------------------------
# 5) Escreva um programa que inverta os caracteres de um string.


# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;



def inverter_string(string):
    comprimento = len(string)
    string_final = ''
    for i in range(comprimento - 1, -1, -1): # (start=comprimento - 1, stop=-1, step=-1(para decrementar))
        string_final += string[i]
    return string_final



def quinta_questao():
    string_original = "TARGET, ME DÁ ESSA OPORTUNIDADE"
    #string_original = input('Digite a string que deseja inverter: ')
    string_invertida = inverter_string(string_original)

    # Exibindo o resultado
    print("String original:", string_original)
    print("String invertida:", string_invertida)


def main():
    primeira_questao()
    #segundaquestao()
    #quinta_questao()