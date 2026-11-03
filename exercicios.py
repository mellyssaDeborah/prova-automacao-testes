# ---------- Exercício 1 ----------
def classificar_nota(nota):
    if nota < 0 or nota > 10:
        return "Nota inválida"
    if nota >= 7:
        return "Aprovado"
    if nota >= 5:
        return "Recuperação"
    return "Reprovado"


# ---------- Exercício 2 ----------
def analisar_texto(texto):
    return len(texto.split())


# ---------- Exercício 3 ----------
def analisar_numero(numero):
    if numero > 0:
        sinal = "Positivo"
    elif numero < 0:
        sinal = "Negativo"
    else:
        sinal = "Zero"

    paridade = "par" if numero % 2 == 0 else "ímpar"
    return f"{sinal} e {paridade}"


# ---------- Exercício 4 ----------
def buscar_nome(usuario_id):
    nomes = {1: "Carlos", 2: "Ana", 3: "Beatriz"}
    return nomes.get(usuario_id, "Visitante")


def gerar_saudacao(usuario_id):
    nome = buscar_nome(usuario_id)
    return f"Olá, {nome}! Seja bem-vindo."


# ---------- Exercício 5 ----------
def verificar_senha(senha):
    tem_tamanho = len(senha) >= 8
    tem_numero = any(c.isdigit() for c in senha)
    tem_letra = any(c.isalpha() for c in senha)
    return tem_tamanho and tem_numero and tem_letra


def criar_conta(nome, senha):
    if verificar_senha(senha):
        return "Conta criada com sucesso"
    return "Senha inválida"


# ---------- Exercício 6 ----------
ASSENTOS_DISPONIVEIS = {1, 2, 3, 4, 5}


def verificar_assento(numero_assento):
    return numero_assento in ASSENTOS_DISPONIVEIS


def reservar_assento(numero_assento):
    return "Assento reservado"


def confirmar_reserva(numero_assento):
    if verificar_assento(numero_assento):
        return reservar_assento(numero_assento)
    return "Assento indisponível"
