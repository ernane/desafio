# Desafio Escadinha

**Problema:** Como engenheiro de dados, você foi requisitado a fazer uma ETL em um novo
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

## Para solucionar o problema, entregue um código que

**1)** Verifica se há escadinha, dada uma matriz como os exemplos acima.

**2)** Se houver escadinha, mapear os dados corretamente, retornando a matriz correta.

**3)** Se não houver escadinha, retorne se a matriz está com uma formatação que pode
ser utilizada (padrão correto) ou se corresponde a um padrão inutilizável.

**4)** Caso fossem possíveis números negativos nos valores dos meses (não no total), a
sua solução ainda seria válida? Caso não, como seria a nova solução?
**Resposta:** A solução também atende números negativos

**Solução:** Para resolução do desafio, foi criado um script python **main.py**

**Resultado:** Resultado da execução do script **main.py**

```shell
1) Questão
 Matriz: Correta é Escadinha? False
 Matriz: Escadinha é Escadinha? True
 Matriz: EscadinhaEstendida é Escadinha? True
 Matriz: EscadinhaReversa é Escadinha? False
 Matriz: Inutilizavel_1 é Escadinha? False
 Matriz: Inutilizavel_2 é Escadinha? False
 Matriz: EscadinhaNegativo é Escadinha? True
2) Questão
 Matriz: Correta não é Escadinha
 Matrix Escadinha Atual
     0   1   2   3   4   5   6   7   8   9  10  11  12
0   11  12  78   1   2   3   4   5   6   7   8   9  10
1   10  11  12  78   1   2   3   4   5   6   7   8   9
2    9  10  11  12  78   1   2   3   4   5   6   7   8
3    8   9  10  11  12  78   1   2   3   4   5   6   7
4    7   8   9  10  11  12  78   1   2   3   4   5   6
5    6   7   8   9  10  11  12  78   1   2   3   4   5
6    5   6   7   8   9  10  11  12  78   1   2   3   4
7    4   5   6   7   8   9  10  11  12  78   1   2   3
8    3   4   5   6   7   8   9  10  11  12  78   1   2
9    2   3   4   5   6   7   8   9  10  11  12  78   1
10   1   2   3   4   5   6   7   8   9  10  11  12  78
11  78   1   2   3   4   5   6   7   8   9  10  11  12
 Matrix Escadinha Depois
    0  1  2  3  4  5  6  7  8   9  10  11  12
0   1  2  3  4  5  6  7  8  9  10  11  12  78
1   1  2  3  4  5  6  7  8  9  10  11  12  78
2   1  2  3  4  5  6  7  8  9  10  11  12  78
3   1  2  3  4  5  6  7  8  9  10  11  12  78
4   1  2  3  4  5  6  7  8  9  10  11  12  78
5   1  2  3  4  5  6  7  8  9  10  11  12  78
6   1  2  3  4  5  6  7  8  9  10  11  12  78
7   1  2  3  4  5  6  7  8  9  10  11  12  78
8   1  2  3  4  5  6  7  8  9  10  11  12  78
9   1  2  3  4  5  6  7  8  9  10  11  12  78
10  1  2  3  4  5  6  7  8  9  10  11  12  78
11  1  2  3  4  5  6  7  8  9  10  11  12  78

 Matrix EscadinhaEstendida Atual
     0   1   2   3   4   5   6   7   8   9  10  11  12
0   11  12  78   1   2   3   4   5   6   7   8   9  10
1   10  11  12  78   1   2   3   4   5   6   7   8   9
2    9  10  11  12  78   1   2   3   4   5   6   7   8
3    8   9  10  11  12  78   1   2   3   4   5   6   7
4    7   8   9  10  11  12  78   1   2   3   4   5   6
5    6   7   8   9  10  11  12  78   1   2   3   4   5
6    5   6   7   8   9  10  11  12  78   1   2   3   4
7    4   5   6   7   8   9  10  11  12  78   1   2   3
8    3   4   5   6   7   8   9  10  11  12  78   1   2
9    2   3   4   5   6   7   8   9  10  11  12  78   1
10   1   2   3   4   5   6   7   8   9  10  11  12  78
11  78   1   2   3   4   5   6   7   8   9  10  11  12
12  12  78   1   2   3   4   5   6   7   8   9  10  11
13  11  12  78   1   2   3   4   5   6   7   8   9  10
14  10  11  12  78   1   2   3   4   5   6   7   8   9
15   9  10  11  12  78   1   2   3   4   5   6   7   8
16   8   9  10  11  12  78   1   2   3   4   5   6   7
17   7   8   9  10  11  12  78   1   2   3   4   5   6
18   6   7   8   9  10  11  12  78   1   2   3   4   5
19   5   6   7   8   9  10  11  12  78   1   2   3   4
 Matrix EscadinhaEstendida Depois
    0  1  2  3  4  5  6  7  8   9  10  11  12
0   1  2  3  4  5  6  7  8  9  10  11  12  78
1   1  2  3  4  5  6  7  8  9  10  11  12  78
2   1  2  3  4  5  6  7  8  9  10  11  12  78
3   1  2  3  4  5  6  7  8  9  10  11  12  78
4   1  2  3  4  5  6  7  8  9  10  11  12  78
5   1  2  3  4  5  6  7  8  9  10  11  12  78
6   1  2  3  4  5  6  7  8  9  10  11  12  78
7   1  2  3  4  5  6  7  8  9  10  11  12  78
8   1  2  3  4  5  6  7  8  9  10  11  12  78
9   1  2  3  4  5  6  7  8  9  10  11  12  78
10  1  2  3  4  5  6  7  8  9  10  11  12  78
11  1  2  3  4  5  6  7  8  9  10  11  12  78
12  1  2  3  4  5  6  7  8  9  10  11  12  78
13  1  2  3  4  5  6  7  8  9  10  11  12  78
14  1  2  3  4  5  6  7  8  9  10  11  12  78
15  1  2  3  4  5  6  7  8  9  10  11  12  78
16  1  2  3  4  5  6  7  8  9  10  11  12  78
17  1  2  3  4  5  6  7  8  9  10  11  12  78
18  1  2  3  4  5  6  7  8  9  10  11  12  78
19  1  2  3  4  5  6  7  8  9  10  11  12  78

 Matrix EscadinhaNegativo Atual
     0   1   2   3   4   5   6   7   8   9  10  11  12
0  -11 -12  78  -1  -2  -3  -4  -5  -6  -7  -8  -9 -10
1  -10 -11 -12  78  -1  -2  -3  -4  -5  -6  -7  -8  -9
2   -9 -10 -11 -12  78  -1  -2  -3  -4  -5  -6  -7  -8
3   -8  -9 -10 -11 -12  78  -1  -2  -3  -4  -5  -6  -7
4   -7  -8  -9 -10 -11 -12  78  -1  -2  -3  -4  -5  -6
5   -6  -7  -8  -9 -10 -11 -12  78  -1  -2  -3  -4  -5
6   -5  -6  -7  -8  -9 -10 -11 -12  78  -1  -2  -3  -4
7   -4  -5  -6  -7  -8  -9 -10 -11 -12  78  -1  -2  -3
8   -3  -4  -5  -6  -7  -8  -9 -10 -11 -12  78  -1  -2
9   -2  -3  -4  -5  -6  -7  -8  -9 -10 -11 -12  78  -1
10  -1  -2  -3  -4  -5  -6  -7  -8  -9 -10 -11 -12  78
11  78  -1  -2  -3  -4  -5  -6  -7  -8  -9 -10 -11 -12
 Matrix EscadinhaNegativo Depois
    0  1  2  3  4  5  6  7  8   9  10  11  12
0  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
1  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
2  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
3  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
4  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
5  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
6  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
7  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
8  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
9  -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
10 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78
11 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12  78

 Matriz: EscadinhaReversa não é Escadinha
 Matriz: Inutilizavel_1 não é Escadinha
 Matriz: Inutilizavel_2 não é Escadinha
3) Questão
 Matrix Correta Pradao Correto
 Matriz: Escadinha é Escadinha
 Matriz: EscadinhaEstendida é Escadinha
 Matrix EscadinhaReversa Pradao Inutilizavel
 Matrix Inutilizavel_1 Pradao Inutilizavel
 Matrix Inutilizavel_2 Pradao Inutilizavel
 Matriz: EscadinhaNegativo é Escadinha
```

## Execução Local

Para execução do script localmente, previamente é necessária a instalação dos componentes abaixo:

- [3.6+](https://www.python.org/downloads/)
- [pipenv](https://pypi.org/project/pipenv/)
- [Pandas](https://pypi.org/project/pandas/)

## Demonstração da solução

Clonar o repositório e entrar no diretório do desafio python

```shell
git clone https://github.com/ernane/desafio.git && cd desafio/python
```

Instalar as dependências através do **pipenv**

```shell
pipenv install
```

Executar o script **main.py**

```shell
pipenv run python main.py
```

## Você também pode conferir o passo a passo no exemplo abaixo

![escadinha-shell](https://github.com/ernane/desafio/blob/master/assets/gifs/desafio-escadinha.gif)
