# Começo importando as bibliotecas que vou usar.

import requests
from bs4 import BeautifulSoup
import pandas as pd
#criando uma lista que vai ser preenchida com as informações raspadas do site.
lista_noticias = []
# Fazendo a requisição de dados do site.
response = requests.get('https://record.r7.com/noticias/')

content = response.content
# Convertemos o conteúdo para formato html, normal, mas caso não esteja em html, vai ficar e organizado também.
site = BeautifulSoup(content, 'html.parser')
# print(site)
# HTML da notícia,... Agora vai la no site e encontra onde tem todas as classes: b-ultimas-list__item-content
notícias = site.findAll('div', attrs={'class': 'b-ultimas-list__item-content'})
for noticia in notícias:

#Neste caso não preciso evidenciar a classe, pois somente têm um link clicável, que é o ue esse 'a' me retorna.
# com isso irei usar a função .text após o título para extrair somente o texto.
    título = noticia.find('a', attrs={'class': ''})
    print(f'Título: {título.text}')
    # Print aqui o BeautifulSoup deixa os itens separados como uma lista, quando eu dou print['href'], isso irá mostrar o link clicável
    print(título['href'])

# Neste caso o subtítulo está dentro de um parágrafo, marcado com 'p'
    subtítulo = noticia.find('p', attrs={'class': 'dark:base-text-neutral-high-400 base-text-[calc(theme(fontSize.xxxs)_*_var(--font-size,_1))] base-font-normal base-font-primary base-text-neutral-low-500 base-text-left'})
    if (subtítulo):
        print(f'Subtítulo: {subtítulo.text}')
        # Adicionando os itens encontrados dentro da lista criada lá no começo.
        lista_noticias.append([título.text, subtítulo.text, título['href']])
    # Para caso não tenha subtítulo na notícia, traga para a nossa lista apenas os outros valores encontrados.
    else:
        lista_noticias.append([título.text, '', título['href']])
# Transformando a lista em uma tabela
news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])
#salvando a tabela em formato excel('.xlsx')
news.to_excel('notícias.xlsx', index=False)
# Salvando em formato csv('.csv')
news.to_csv('Notícias.csv', index=False)
print(news)