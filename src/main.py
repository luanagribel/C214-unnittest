from src.dominio import Cliente, Lance, Leilao

phyl = Cliente("Phyl")
igor = Cliente("Igor")
luana = Cliente("Luana")
sarah = Cliente("Sarah")

lance_do_phyl = Lance(phyl, 150.0)
lance_do_igor = Lance(igor, 100.0)
lance_da_luana = Lance(luana, 80.0)
lance_da_sarah = Lance(sarah, 200.0)

leilao = Leilao("1 Saco de Arroz de 5kg")

leilao.propoe(lance_do_igor)
leilao.propoe(lance_do_phyl)
leilao.propoe(lance_da_luana)
leilao.propoe(lance_da_sarah)

for lance in leilao.lances:
    print(f"O cliente {lance.cliente.nome} deu um lance de {lance.valor}.")

print(f"O menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}")
