# Desafio SQL

**Problema:** Você tem duas tabelas em um banco de dados relacional(Vendedor e Venda). Retorne a lista com a venda de valor mais alto de cada vendedor para o ano de 2016.

**Solução:** Consulta abaixo retorna a maior venda de dados os vendedores para o ano de 2016.

```sql
SELECT x.vendedor_nome,
       x.venda_data,
       x.venda_valor
  FROM (
        SELECT v.venda_id,
            v.vendedor_id,
            z.vendedor_nome,
            v.venda_data,
            v.venda_valor,
            rank() OVER (PARTITION BY v.vendedor_id ORDER BY v.venda_valor DESC) AS rank
          FROM venda v
          JOIN vendedor z
            ON z.vendedor_id = v.vendedor_id
         WHERE EXTRACT(YEAR FROM v.venda_data) = 2016
       ) x
 WHERE x.rank = 1
ORDER BY x.venda_valor DESC;
```

**Resultado:** Resultado da consulta SQL acima

![resultado-sql](https://github.com/ernane/desafio/blob/master/assets/images/consulta-sql.png)

## Stack

Para execução da Stack e demonstração da solução do desafio, previamente é necessária a instalação das ferramentas abaixo:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Tecnologias e Ferramentas utilizadas

- [Git](https://git-scm.com/)
- [Github](https://github.com)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)
- [pgAdmin](https://www.pgadmin.org/)

## Demonstração da solução

Clonar o repositório e entrar no diretório do desafio SQL

```shell
git clone https://github.com/ernane/desafio.git && cd desafio/sql
```

Subir a Stack via docker-compose

```shell
docker-compose up
```

Após o **docker-compose** baixar as imagens e iniciar os containers com as configurações pré-definidas.
Você pode abrir um novo shell e ganhar terminal para o container onde está instalado o banco de dados

```shell
docker exec -it sql_postgres-server_1 psql -U postgres
```

Dentro do terminal shell do container **sql_postgres-server_1** você pode executar a consulta abaixo e conferir o resultado

```sql
SELECT x.vendedor_nome,
       x.venda_data,
       x.venda_valor
  FROM (
        SELECT v.venda_id,
            v.vendedor_id,
            z.vendedor_nome,
            v.venda_data,
            v.venda_valor,
            rank() OVER (PARTITION BY v.vendedor_id ORDER BY v.venda_valor DESC) AS rank
          FROM venda v
          JOIN vendedor z
            ON z.vendedor_id = v.vendedor_id
         WHERE EXTRACT(YEAR FROM v.venda_data) = 2016
       ) x
 WHERE x.rank = 1
ORDER BY x.venda_valor DESC;
```

## Você também pode conferir o passo a passo no exemplo abaixo

![demonstração-shell](https://github.com/ernane/desafio/blob/master/assets/gifs/desafio-sql.gif)

## Demonstração da solução via pgAdmin

Após a construção da Stack, também é iniciado o serviço web do [pgAdmin](http://localhost:8080/) que está rodando na porta 8080.
Os parametros de configuração para utilização da ferramenta são:

```shell
PGADMIN_EMAIL: challenge@email.com
PGADMIN_PASSWORD: challenge2020

POSTGRES_HOST: postgres-server
POSTGRES_USER: postgres
POSTGRES_PASSWORD: challenge2020
```

Caso a Stack não estiver ativa, você pode executar o comando abaixo, a partir do diretório do desafio. Isso permite acesso via browser no endereço [http://localhost:8080/](http://localhost:8080/)

```shell
docker-compose up
```

## Você também pode visualizar o passo a passo no exemplo abaixo

![demonstração-pgadmin](https://github.com/ernane/desafio/blob/master/assets/gifs/desafio-sql-pgadmin.gif)
