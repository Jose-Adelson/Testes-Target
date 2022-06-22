SP = float(67836.43)
RJ = float(36678.66)
MG = float(29229.88)
ES = float(27165.48)
Outros = float(19849.53)
Total = float(SP + RJ + MG + ES + Outros)

porcentagem = "%"
porcentagem_SP = (SP/Total) * 100
porcentagem_RJ = (RJ/Total) * 100
porcentagem_MG = (MG/Total) * 100
porcentagem_ES = (ES/Total) * 100

print("O percentual do estado de SP é  %s%.2f " %(porcentagem,porcentagem_SP))
print("O percentual do estado de RJ é  %s%.2f " %(porcentagem,porcentagem_RJ))
print("O percentual do estado de MG é  %s%.2f " %(porcentagem,porcentagem_MG))
print("O percentual do estado de ES é  %s%.2f " %(porcentagem,porcentagem_ES))

