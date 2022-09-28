# PROJETO 1
# Alunos: RAFAEL ECKHARDT LUCENA; HENRIQUE MACEDO TORRES
v = [0.751, 0.00350, 0.0319, 0.527, 0.000089, 0.496, 0.635, 0.400, 0.290, 0.200, 0.498, 0.0544, 0.0424, 0.870]
p = [999.9, 2499.9, 299.29, 3999.9, 2199.12, 199.9, 849, 4346.99, 3999.9, 2999.9, 1999.9, 429.9, 429.9, 1199.98]
r = []
rs = []
resultado = []
aux = 0
for i in range(0,len(v)):
    r.append(p[i]/v[i])
    rs.append(p[i]/v[i])
rs.sort()
rs.reverse()
for i in range(0, len(rs)):
    for j in range(0, len(rs)):
        if(rs[i] == r[j]):
            rs[i] = j

for i in range(0,len(rs)):
    if((aux + v[rs[i]]) < 3):
        aux = aux + v[rs[i]]
        resultado.append(rs[i]+1)

resultado.sort()
print(f'O melhor conjunto de produtos a serem transportados visando maximizar os lucros são os itens: {resultado}.')
