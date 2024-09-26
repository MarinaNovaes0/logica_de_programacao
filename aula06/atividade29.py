#entrada de dados e conversão de dados 
dist= input('Digite a distância percorrida: ')
dist= float(dist)

comb_gast= input('Digite a quantidade de gasolina gasta: ')
comb_gast= float(comb_gast)

cons_medio= dist/comb_gast #operação matemática
print(f'O consumo médio é igual a: {cons_medio:.2f}km/l')