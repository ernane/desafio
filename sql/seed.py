#!/usr/bin/env python

import random
import datetime

vendedores = (
    {"id": 1, "quantidade": 163},
    {"id": 2, "quantidade": 120},
    {"id": 3, "quantidade": 260},
    {"id": 4, "quantidade": 180},
    {"id": 5, "quantidade": 263},
    {"id": 6, "quantidade": 130},
    {"id": 7, "quantidade": 261},
    {"id": 8, "quantidade": 133},
)


def print_(venda):
    quantidade = int(venda['quantidade'])
    vendedor = venda['id']
    file_name = f"insert_{vendedor}.sql"
    with open(file_name, 'w') as saida:
        for x in range(quantidade):
            valor = round(random.uniform(x, quantidade), 2)
            data = str(datetime.datetime.strptime(
                '{} {}'.format(random.randint(1, 366),
                               random.randint(2015, 2018)), '%j %Y'))

            print(
                f"INSERT INTO public.venda(vendedor_id, venda_data, \
venda_valor) VALUES({vendedor}, '{data[0:10]}', {valor});", file=saida)


if __name__ == "__main__":
    for v in vendedores:
        print_(v)
