import random


MENOR_SENHA = 1
MAIOR_SENHA = 100
MAX_TENTATIVAS = 7


def mostrar_intro():
    print("=== Adivinha Senha ===")
    print("Voce acordou dentro de uma sala digital trancada.")
    print("No painel da porta existe uma senha numerica escondida.")
    print("Descubra a senha correta para desbloquear a saida.")


def gerar_senha():
    return random.randint(MENOR_SENHA, MAIOR_SENHA)


def avaliar_palpite(palpite, senha_secreta):
    if palpite == senha_secreta:
        return "acertou"
    if palpite > senha_secreta:
        return "alto"
    return "baixo"


def mostrar_dica(resultado):
    if resultado == "acertou":
        print("Acertou! A porta foi desbloqueada.")
    elif resultado == "alto":
        print("Muito alto.")
    else:
        print("Muito baixo.")


def ler_palpite():
    while True:
        entrada = input("Digite sua tentativa: ").strip()

        if not entrada:
            print("Digite um numero.")
            continue

        try:
            palpite = int(entrada)
        except ValueError:
            print("Digite apenas numeros.")
            continue

        if palpite < MENOR_SENHA or palpite > MAIOR_SENHA:
            print(f"Digite um numero entre {MENOR_SENHA} e {MAIOR_SENHA}.")
            continue

        return palpite


def jogar(senha_secreta=None):
    senha_secreta = senha_secreta if senha_secreta is not None else gerar_senha()
    tentativas = 0

    while tentativas < MAX_TENTATIVAS:
        tentativa = ler_palpite()
        tentativas += 1
        resultado = avaliar_palpite(tentativa, senha_secreta)
        mostrar_dica(resultado)

        if resultado == "acertou":
            print(f"Voce precisou de {tentativas} tentativa(s).")
            return True

        restantes = MAX_TENTATIVAS - tentativas
        if restantes > 0:
            print(f"Tentativas restantes: {restantes}")

    print("Suas tentativas acabaram. A porta continuou trancada.")
    print(f"A senha era {senha_secreta}.")
    return False


def main():
    mostrar_intro()
    print(f"A senha esta entre {MENOR_SENHA} e {MAIOR_SENHA}.")
    print(f"Voce tem {MAX_TENTATIVAS} tentativas.")
    jogar()


if __name__ == "__main__":
    main()
