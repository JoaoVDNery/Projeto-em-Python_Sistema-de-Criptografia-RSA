# COMANDO PARA INSTALAR A BIBLIOTECA CASO AINDA NAO TENHA!
# !pip install rsa

# Chama o RSA
import rsa


# INICIO DO PROCESSO DE CRIPROGRAFIA DE MENSAGENS!!!


def criptografar_chavePublica():
    print("*ATENÇÃO: Caso já exista um arquivo de mensagem criptografada(Mensagem_Criptografada), este será substituido!\n\nPara voltar ao menu NÃO DIGITE a mensagem e aperte 'ENTER' ")
    Mensagem = input("\nDigite sua mensagem:")

    while True:

        if len(Mensagem) == 0:

            break

        elif len(Mensagem) > 128:
            print("Sua mensagem excede o limite de 128 caracteres!")
            print("\nPara voltar ao menu NÃO DIGITE a mensagem e aperte 'ENTER' ")
            Mensagem = input("\nDigite sua mensagem:")

            continue
        else:

            try:
                with open("Publica.PEM","rb") as f:  # PEGA A CHAVE PUBLICA DO ARQUIVO "Publica.PEM" E ATRIBUI O VALOR NA VARIAVEL Chave_Publica
                    Chave_Publica = rsa.PublicKey.load_pkcs1(f.read())

                    Mensagem_Criptograf = rsa.encrypt(Mensagem.encode(),Chave_Publica)  # UTILIZA A CHAVE PUBLICA PARA A CRIPTOGRAR A MENSAGEM E ARMAZENA NA VARIAVEL Mensagem_Criptograf

                    with open("Mensagem_Criptografada", "wb") as f:  # CRIA UM ARQUIVO.PEM COM A MENSAGEM CRIPTOGRAFADA
                        f.write(Mensagem_Criptograf)

                    print('\nSeu arquivo com a mensagem criptografada foi criado!')
            except:
                print("\nVocê não tem a chave publica!")

        break

# FIM DO PROCESSO DE CRIPTOGRAFIA!!!


# INICIO DO PROCESSO DE DESCRIPTOGRAFIA!!!
def descriptografar_chavePrivada():
    try:
        Mensagem_Criptograf = open("Mensagem_Criptografada","rb").read()  # PEGA A MENSAGEM CRIPTOGRAFADA DO ARQUIVO "Mensagem_Criptografada" E ATRIBUI NA VARIAVEL "Mensagem_Criptograf"

        with open("Privada.PEM","rb") as f:  # PEGA A CHAVE PRIVADA DO ARQUIVO "Privada.PEM" E ATRIBUI O VALOR NA VARIAVEL Chave_Privada
            Chave_Privada = rsa.PrivateKey.load_pkcs1(f.read())

            Mensagem_Descrpit = rsa.decrypt(Mensagem_Criptograf,Chave_Privada)  # UTILIZA A CHAVE PRIVADA PARA DESCRIPTOGRAFAR A MENSAGEM E ARMAZENA NA VARIAVEL Mensagem_Descript

            print('\nEsta é a mensagem descriptografada:', Mensagem_Descrpit.decode())
    except:
        print(
            "\nPara que a mensagem seja descrpitografada é necessário possuir o\nArquivo de Chave Privada(Privada.PEM) e o Arquivo da mensagem criptografada(Mensagem_Criptografada) VÁLIDOS!")


# FIM DO PROCESSO DE DESCRIPTOGRAFIA!!!


# INICIO DO MENU DE ESCOLHAS!!!

escolha = ""

while escolha != "3":

    escolha = input(
        "\n*SISTEMA DE CRIPTOGRAFIA E DESCRIPTOGRAFIA*\n1.Criptografar mensagem.\n2.Descriptografar Mensagem.\n3.Sair.\n\nDigite a opção escolhida: ")

    if escolha == "1":
        criptografar_chavePublica()  # CHAMANDO A FUNÇÃO criptografar_chavePublica()

    elif escolha == "2":
        descriptografar_chavePrivada()  # CHAMANDO A FUNÇÃO descriptografar_chavePrivada()

    elif escolha == "3":
        print("\n\nEncerrando programa...")

    else:
        print("\nOpção inválida")

# FIM DO MENU DE ESCOLHAS!!!