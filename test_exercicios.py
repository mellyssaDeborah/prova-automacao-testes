import pytest
from unittest.mock import patch

from exercicios import (
    classificar_nota,
    analisar_texto,
    analisar_numero,
    gerar_saudacao,
    criar_conta,
    confirmar_reserva,
)


# ---------- Exercício 1 ----------
def test_nota_8_aprovado():
    assert classificar_nota(8) == "Aprovado"


def test_nota_6_recuperacao():
    assert classificar_nota(6) == "Recuperação"


def test_nota_4_reprovado():
    assert classificar_nota(4) == "Reprovado"


def test_nota_10_aprovado():
    assert classificar_nota(10) == "Aprovado"


def test_nota_negativa_invalida():
    assert classificar_nota(-1) == "Nota inválida"


def test_nota_11_invalida():
    assert classificar_nota(11) == "Nota inválida"


# ---------- Exercício 2 ----------
def test_frase_com_5_palavras():
    assert analisar_texto("Eu estudo testes com Python") == 5


def test_frase_com_uma_palavra():
    assert analisar_texto("Python") == 1


def test_frase_vazia():
    assert analisar_texto("") == 0


def test_frase_com_espacos_no_inicio_e_fim():
    assert analisar_texto("   Olá mundo   ") == 2


def test_frase_com_varios_espacos_entre_palavras():
    assert analisar_texto("Eu    estudo     Python") == 3


# ---------- Exercício 3 ----------
def test_positivo_e_par():
    assert analisar_numero(10) == "Positivo e par"


def test_positivo_e_impar():
    assert analisar_numero(7) == "Positivo e ímpar"


def test_negativo_e_par():
    assert analisar_numero(-4) == "Negativo e par"


def test_negativo_e_impar():
    assert analisar_numero(-3) == "Negativo e ímpar"


def test_zero():
    assert analisar_numero(0) == "Zero e par"


# ---------- Exercício 4 ----------
def test_saudacao_gerada_corretamente():
    with patch("exercicios.buscar_nome", return_value="Carlos"):
        assert gerar_saudacao(1) == "Olá, Carlos! Seja bem-vindo."


def test_buscar_nome_foi_chamada():
    with patch("exercicios.buscar_nome", return_value="Carlos") as mock_buscar:
        gerar_saudacao(1)
        mock_buscar.assert_called_once()


def test_buscar_nome_chamada_com_id_correto():
    with patch("exercicios.buscar_nome", return_value="Carlos") as mock_buscar:
        gerar_saudacao(42)
        mock_buscar.assert_called_once_with(42)


def test_saudacao_com_diferentes_nomes():
    for nome in ["Ana", "Pedro", "Maria"]:
        with patch("exercicios.buscar_nome", return_value=nome):
            assert gerar_saudacao(1) == f"Olá, {nome}! Seja bem-vindo."


# ---------- Exercício 5 ----------
def test_criar_conta_com_senha_valida():
    assert criar_conta("Ana", "senha1234") == "Conta criada com sucesso"


def test_criar_conta_com_senha_invalida():
    assert criar_conta("Ana", "123") == "Senha inválida"


def test_verificar_senha_foi_chamada():
    with patch("exercicios.verificar_senha", return_value=True) as mock_verificar:
        criar_conta("Ana", "qualquer")
        mock_verificar.assert_called_once()


def test_verificar_senha_chamada_com_senha_correta():
    with patch("exercicios.verificar_senha", return_value=True) as mock_verificar:
        criar_conta("Ana", "abc12345")
        mock_verificar.assert_called_once_with("abc12345")


def test_mock_simulando_senha_valida():
    with patch("exercicios.verificar_senha", return_value=True):
        assert criar_conta("Ana", "x") == "Conta criada com sucesso"


def test_mock_simulando_senha_invalida():
    with patch("exercicios.verificar_senha", return_value=False):
        assert criar_conta("Ana", "x") == "Senha inválida"


# ---------- Exercício 6 ----------
def test_reserva_realizada_com_sucesso():
    with patch("exercicios.verificar_assento", return_value=True), \
         patch("exercicios.reservar_assento", return_value="Assento reservado"):
        assert confirmar_reserva(3) == "Assento reservado"


def test_assento_indisponivel():
    with patch("exercicios.verificar_assento", return_value=False), \
         patch("exercicios.reservar_assento"):
        assert confirmar_reserva(3) == "Assento indisponível"


def test_verificar_assento_foi_chamada():
    with patch("exercicios.verificar_assento", return_value=True) as mock_verificar, \
         patch("exercicios.reservar_assento"):
        confirmar_reserva(3)
        mock_verificar.assert_called_once_with(3)


def test_reservar_assento_chamada_quando_disponivel():
    with patch("exercicios.verificar_assento", return_value=True), \
         patch("exercicios.reservar_assento") as mock_reservar:
        confirmar_reserva(3)
        mock_reservar.assert_called_once_with(3)


def test_reservar_assento_nao_chamada_quando_indisponivel():
    with patch("exercicios.verificar_assento", return_value=False), \
         patch("exercicios.reservar_assento") as mock_reservar:
        confirmar_reserva(3)
        mock_reservar.assert_not_called()


def test_mock_simulando_os_cenarios():
    # Cenário 1: assento disponível
    with patch("exercicios.verificar_assento", return_value=True), \
         patch("exercicios.reservar_assento", return_value="Assento reservado"):
        assert confirmar_reserva(1) == "Assento reservado"

    # Cenário 2: assento indisponível
    with patch("exercicios.verificar_assento", return_value=False), \
         patch("exercicios.reservar_assento") as mock_reservar:
        assert confirmar_reserva(1) == "Assento indisponível"
        mock_reservar.assert_not_called()
