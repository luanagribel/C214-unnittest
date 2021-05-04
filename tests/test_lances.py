from unittest import TestCase

from src.dominio import Cliente, Lance, Leilao


class TestLances(TestCase):
    def setUp(self):
        self.phyl = Cliente("Phyl")
        self.lance_do_phyl = Lance(self.phyl, 150.0)
        self.leilao = Leilao("1 Saco de Arroz de 5kg")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        igor = Cliente("Igor")
        lance_do_igor = Lance(igor, 100.0)

        self.leilao.propoe(lance_do_igor)
        self.leilao.propoe(self.lance_do_phyl)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        luana = Cliente("Luana")
        lance_do_luana = Lance(luana, 80.0)

        self.leilao.propoe(self.lance_do_phyl)
        self.leilao.propoe(lance_do_luana)

        menor_valor_esperado = 80.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_phyl)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        igor = Cliente("Igor")
        lance_do_igor = Lance(igor, 10.0)
        sarah = Cliente("Sarah")

        lance_da_sarah = Lance(sarah, 200.0)

        self.leilao.propoe(lance_do_igor)
        self.leilao.propoe(self.lance_do_phyl)
        self.leilao.propoe(lance_da_sarah)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
