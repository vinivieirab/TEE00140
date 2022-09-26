import matplotlib.pyplot as plt
import pandas as pd


#o Python vai ler o arquivo excel em formato .xlsx e organizar a coluna "PREÇO" de forma decrescente
data = pd.read_excel(r'C:\Users\MITANG\PycharmProjects\pythonProject1\projeto_1.xlsx')
dp = data.sort_values('PREÇO', ascending= False)
print(dp)

#Definir a variável x como o "volume m^3" e y como "PREÇO"
x = dp['VOLUME M^3']
y = dp['PREÇO']

#Plotando o gráfico em função das duas variáveis
plt.scatter(x,y,color = 'green')
plt.title('Analise')
plt.xlabel('Volume M^3')
plt.ylabel('Preço')
plt.show()

k1, k2 = ([], [])   #Listas que irão armazenar os valores de preço e volume
z, d = (0, 0)   #Contador
cont1, cont2 = (0, 0)   #somatório de volume e preço
print('\n')
for m in x:
    if cont1 <= 3:          #Capacidade máxima do caminhão (3 m^3)
        cont1 = m+cont1
        k1.append(cont1)
        print('x: ', cont1)
        z = z+1
print('\n')
for n in y:
    if d < z:
        cont2 = n+cont2
        k2.append(cont2)
        print('y: ', cont2)
        d = d + 1
print('\n')
print('Resultado aproximado: Volume M^3: ', k1[z-2], 'm^3', '\nPreço em (R$): ',k2[z-2], 'R$')
