
import requests
import xml.etree.ElementTree as ET


def main():
    
    api_url = 'http://instituto.islagaia.pt/ws/wsCambio.asmx/cambioUSD'

    try:
      
        response = requests.get(api_url)

        
        if response.status_code == 200:
           
            print('Resposta da API:')
            
            
            root = ET.fromstring(response.text)
            serie = root.find('.//Serie').text
            numero_sorteado = root.find('.//Numero').text
            
            print(f'Série: {serie}, Número Sorteado: {numero_sorteado}')
        else:
            print(f'Erro na solicitação. Código de status: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')


if __name__ == "__main__":
    main()

python consome_api_Tiago_Silva

