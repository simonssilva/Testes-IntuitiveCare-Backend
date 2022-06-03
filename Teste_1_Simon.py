from bs4 import BeautifulSoup
import requests
import os
import shutil

#função para fazer download de arquivos
def baixar_arquivo(url, endereco):
    #requisição do servidor
    resposta = requests.get(url)
    #obter resposta do link se está OK
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

html = requests.get("https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude").content
soup = BeautifulSoup(html, 'html.parser')

#Nome dos respectivos anexos para download
fileName = ["Anexo I - Lista completa de procedimentos (.pdf)", "Anexo I - Lista completa de procedimentos (.xlsx)", "Anexo II - Diretrizes de utilização (.pdf)", "Anexo III - Diretrizes clínicas (.pdf)", "Anexo IV - Protocolo de utilização (.pdf)"]

links = soup.find_all('a', target='_self', string= fileName)

#diretório destino
OUTPUT_DIR = 'Anexos'

#download dos anexos para o destino
for i in links:
    linkToDownload = i.get('href')
    nomeArquivo = os.path.basename(linkToDownload.split("?")[0]) #variável recebe nome junto com seu respectivo formato
    local = os.path.join(OUTPUT_DIR, nomeArquivo) #variável recebe a junção do diretório destino e seu respectivo nome.formato
    baixar_arquivo(linkToDownload, local)

shutil.make_archive('anexos', 'zip', './', OUTPUT_DIR) #comprimir pasta com os arquivos
