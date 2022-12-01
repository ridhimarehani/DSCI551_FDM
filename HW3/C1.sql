CREATE OR REPLACE VIEW Beers2Bars AS
SELECT b.manf AS manufacturer, b.name AS beer, s.bar, s.price
FROM Beers b
INNER JOIN Sells s
ON b.name = s.beer;

/* Output
Query OK, 0 rows affected (0.00 sec)

select * from Beers2Bars;
+----------------+------------+------------+-------+
| Manufacturer   | name       | bar        | price |
+----------------+------------+------------+-------+
| Anheuser-Busch | Bud        | Bob's bar  |     3 |
| Pete's         | Summerbrew | Bob's bar  |     3 |
| Anheuser-Busch | Bud        | Joe's bar  |     3 |
| Anheuser-Busch | Bud Lite   | Joe's bar  |     3 |
| Anheuser-Busch | Michelob   | Joe's bar  |     3 |
| Pete's         | Summerbrew | Joe's bar  |     4 |
| Anheuser-Busch | Bud        | Mary's bar |  NULL |
| Anheuser-Busch | Bud Lite   | Mary's bar |     3 |
| Heineken       | Budweiser  | Mary's bar |     2 |
+----------------+------------+------------+-------+
*/