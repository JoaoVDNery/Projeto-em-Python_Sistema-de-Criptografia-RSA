# COMANDO PARA INSTALAR A BIBLIOTECA CASO AINDA NAO TENHA!
# !pip install rsa
import rsa


def Gerar_Chaves():
    print('\nGerando chaves, aguarde...')
    Chave_Publica, Chave_Privada = rsa.newkeys(2048)  # COM BASE NA LOGICA MATEMATICA GERA AS CHAVES PUBLICAS E PRIVADAS COM 2048 BITS

    with open("Publica.PEM", "wb") as f:  # CRIA O ARQUIVO COM A CHAVE PUBLICA "Publica.PEM"
        f.write(Chave_Publica.save_pkcs1("PEM"))

    with open("Privada.PEM", "wb") as f:  # CRIA O ARQUIVO COM A CHAVE PRIVADA "Privada.PEM"
        f.write(Chave_Privada.save_pkcs1("PEM"))
    print('Os arquivos de chave privada(Privada.PEM) e pública(Publica.PEM) foram criados!')


escolha = ""

while escolha != "2":

    escolha = input("\n*SISTEMA GERADOR DE CHAVES PUBLICA E PRIVADA*\n1.Gerar chaves(ATENÇÃO: Caso já existam arquivos de chave privada e publica estes serão substituidos!).\n2.Sair.\n\nDigite a opção escolhida: ")

    if escolha == "1":
        Gerar_Chaves()  # chamando função para gerar as chaves

    elif escolha == "2":
        print("\n\nEncerrando programa...")

    else:
        print("\nOpção inválida")