with open("devices.txt", "r") as arquivo:
lista_equipamentos = [linha.strip() for linha in arquivo]

while True:
nome_equipamento = input("Equipamento a procurar (sair p/terminar): ")
if nome_equipamento.lower() == "sair":
break

quant = 0
for equip in lista_equipamentos:
if nome_equipamento.lower() in equip.lower():
quant += 1
print(equip)

if quant == 0:
print("Equipamento Não existe na Lista!")
else:
print(f"Quantidade: {quant}")

python3 Equipamentos_Eduardo_Sousa.py
