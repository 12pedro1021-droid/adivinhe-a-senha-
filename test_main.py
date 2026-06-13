import unittest
from unittest.mock import patch

import main


class TestAdivinhaSenha(unittest.TestCase):
    def test_gerar_senha_fica_no_intervalo_configurado(self):
        for _ in range(100):
            senha = main.gerar_senha()
            self.assertGreaterEqual(senha, main.MENOR_SENHA)
            self.assertLessEqual(senha, main.MAIOR_SENHA)

    def test_avaliar_palpite_quando_acerta(self):
        self.assertEqual(main.avaliar_palpite(42, 42), "acertou")

    def test_avaliar_palpite_quando_palpite_e_alto(self):
        self.assertEqual(main.avaliar_palpite(80, 42), "alto")

    def test_avaliar_palpite_quando_palpite_e_baixo(self):
        self.assertEqual(main.avaliar_palpite(10, 42), "baixo")

    def test_mostrar_dica_exibe_mensagem_de_acerto(self):
        with patch("builtins.print") as print_mock:
            main.mostrar_dica("acertou")

        print_mock.assert_called_once_with("Acertou! A porta foi desbloqueada.")

    def test_jogar_ignora_entradas_invalidas_sem_gastar_tentativa(self):
        entradas = iter(["abc", "0", "42"])

        with patch("builtins.input", lambda _: next(entradas)):
            self.assertTrue(main.jogar(senha_secreta=42))

    def test_jogar_falha_apos_sete_tentativas_validas(self):
        entradas = iter(["1", "2", "3", "4", "5", "6", "7"])

        with patch("builtins.input", lambda _: next(entradas)):
            self.assertFalse(main.jogar(senha_secreta=42))


if __name__ == "__main__":
    unittest.main()
