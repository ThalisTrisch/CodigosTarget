
estados = ['SP','RJ','MG','ES','Outros']
faturamento = [67836.43,36678.66,29229.88,27165.48,19849.53]
total = 0

for i in range(5):
    total += faturamento[i]
    
for i in range(5):
    calculo = faturamento[i]*100/total
    print(" O percentual do faturamento de",estados[i],"sobre o faturamento mensal é de ",round(calculo,2),"%")
