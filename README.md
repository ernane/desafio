# Desafio Engenheiro de Dados

## Questão 1

Como engenheiro de dados, você foi requisitado a fazer uma ETL em um novo
projeto. Esta ETL consiste na leitura de um arquivo excel, extração do valor de
algumas colunas do excel e transformação destes dados. Por fim, os dados serão
armazenados em uma instância do SQL Server.

O arquivo .xls consiste em dados coletados da ANP, com o valor das vendas de
combustíveis para cada mês dos anos entre 2000 e o ano/mês atual. Estes valores
de venda são números inteiros positivos. Por motivos técnicos, você não poderá
fazer a leitura desse arquivo como .xls, mas sim como um arquivo da biblioteca
libreoffice do Linux : .ods. Ao fazer a conversão de .xls para .ods, você verificou que
para alguns arquivos os valores no .ods encontram-se fora da ordem correta.

As colunas presentes no arquivo .ods são: Nome do Combustível, Unidade de
Medida, Refinaria, Estado, Ano, Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho,
Agosto, Setembro, Outubro, Novembro, Dezembro, Total. As colunas dos meses
contém os valores das vendas correspondentes para aquele mês, e a coluna Total
contém a soma dos valores de cada mês da linha correspondente. Entretanto, em
algumas conversões de arquivos, os valores dos meses e do total sofrem um shuffle
de n + k casas para a direita, a partir da primeira linha, com k sendo incrementado
de 1 a cada linha seguinte. Mais especificamente, a primeira linha sofre um shuffle
de n casas, a segunda linha sofre um shuffle de n + 1 casas, a terceira linha sofre um
shuffle de n + 2 casas... a décima terceira linha sofre um shuffle de 13 casas
(retornando à configuração original), e assim até o fim do arquivo.

## Resolução Questão 1

[Implementação e Solução da Questão 1](https://github.com/ernane/desafio/tree/master/python)

---

## Questão 2

Você tem duas tabelas em um banco de dados relacional.

```shell
Tabela Vendedor:
vendedor_id (int)
vendedor_nome (string)
```

```shell
Tabela Venda:
venda_id (int)
vendedor_id (int)
venda_data (data dd/mm/aaaa)
venda_valor (double)
```

Retorne a lista com a venda de valor mais alto de cada vendedor para o ano de 2016.
Não utilize as funções Min/Max.

## Resolução Questão 2

[Implementação e Solução da Questão 2](https://github.com/ernane/desafio/tree/master/sql)
