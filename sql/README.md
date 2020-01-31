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

![demonstração-shell](https://github.com/ernane/desafio/blob/master/gifs/desafio-sql.gif)