# classificacao_de_capins
Projeto com API de classificação dos capins rodando em container docker. 

Para replicar os containers basta executar o comando:

docker-compose up -d 

na pasta raiz do projeto.

Todas as imagens recebidas e tratadas estão sendo salvas no docker volume image-data.

A parte de front-end ficou por conta do container com Nginx(mas pode ser mudado por outro sem problemas), ele apenas exemplifica que já é possível enviar imagens para processamento e receber a resposta com a imagem classificada.

A parte do container do back-end está rodando uma API feita com Flask, ela recebe as imagens e faz todo o processamento necessário e ao final devolve a imagem classificada. 

O que este projeto entrar em produção de fato:
  ser colocado para executar requisições no flask de forma assíncrona; e
  atualizar o modelo de classificação treinado com dados dos capins e solos expostos.
