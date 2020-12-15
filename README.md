# classificacao_de_capins
Projeto com API de classificação dos capins rodando em container docker. 

Para replicar os containers basta executar o comando:

docker-compose up -d 

na pasta raiz do projeto.

Para acessar basta abrir a localhost no navegador.
O botão GET serve só para ver se tá funcionando o container da aplicação.
Para classificar um capim basta clicar em choose file e fazer upload da imagem do dossel dos capins, após alguns segunda a imagem classificada deverá ser exibida na página.
OBSERVAÇÃO 1: Não está sendo feitas verificações se o upload é a imagem de capim ou outra coisa, portanto, se fizer upload de outra coisa que seja diferente de capim resultará em erro.
OBSERVAÇÃO 2: O tamanho da imagem também deve ser das mesmas dimensões das imagens que deixei para exemplo neste repositório. Para fazer classificações de imagens de dimensões diferentes, deverá ser atualizado as dimensões e outros cálculos necessários no código dos scripts utilizados pela API Flask.

Todas as imagens recebidas e tratadas estão sendo salvas no docker volume images-data.

A parte de front-end ficou por conta do container com Nginx(mas pode ser mudado por outro sem problemas), ele apenas exemplifica que já é possível enviar imagens para processamento e receber a resposta com a imagem classificada.

A parte do container do back-end está rodando uma API feita com Flask, ela recebe as imagens e faz todo o processamento necessário e ao final devolve a imagem classificada. 

O que este projeto entrar em produção de fato:
  ser colocado para executar requisições no flask de forma assíncrona; e
  atualizar o modelo de classificação treinado com dados dos capins e solos expostos.
