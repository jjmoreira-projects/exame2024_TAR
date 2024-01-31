
import os
def ler_arquivo_devices(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def main():

    file_path = 'devices.txt'


    if not os.path.exists(file_path):
        print(f'O arquivo {file_path} não foi encontrado.')
        return


    equipamentos = ler_arquivo_devices(file_path)

    while True:

        equipamento_procurar = input('Equipamento a procurar (sair p/terminar): ')

        if equipamento_procurar.lower() == 'sair':
            break

        equipamentos_encontrados = [equip for equip in equipamentos if equipamento_procurar.lower() in equip.lower()]

        if equipamentos_encontrados:
            print(f'Equipamentos encontrados: {", ".join(equipamentos_encontrados)}')
            print(f'Total de equipamentos encontrados: {len(equipamentos_encontrados)}')
        else:
            print('Equipamento Não existe na Lista!')

if __name__ == "__main__":
    main()
    
python3 Equipamentos_Tiago_Silva.py
