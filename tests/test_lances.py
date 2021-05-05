import unittest

from src.dominio import Cliente, Lance, Leilao


class TestLances(unittest.TestCase):
    def setUpClass():
        # SetUp antes de todos os testes da classe
        pass

    def setUp(self):
        # SetUp antes de cada testes da classe
        self.phyl = Cliente("Phyl")
        self.lance_do_phyl = Lance(self.phyl, 150.0)
        self.leilao = Leilao("1 Saco de Arroz de 5kg")

    def test_maior_e_menor_valor_de_um_lance_quando_adicionados_ordem_crescente(self):
        igor = Cliente("Igor")
        lance_do_igor = Lance(igor, 100.0)

        self.leilao.propoe(lance_do_igor)
        self.leilao.propoe(self.lance_do_phyl)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_maior_e_menor_valor_de_um_lance_quando_adicionados_ordem_decrescente(self):
        luana = Cliente("Luana")
        lance_do_luana = Lance(luana, 80.0)

        self.leilao.propoe(self.lance_do_phyl)
        self.leilao.propoe(lance_do_luana)

        menor_valor_esperado = 80.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_phyl)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_maior_e_menor_valor_quando_o_leilao_tiver_tres_lances(self):
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

    def tearDown(self):
        # TearDown depois de cada teste
        pass

    def tearDownClass():
        # TearDown depois de todos os testes da classe
        pass
