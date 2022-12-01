SELECT manufacturer AS Manufacturer, avg(price) AS Average
FROM Beers2Bars
GROUP BY manufacturer;

/* Output
+----------------+---------+
| Manufacturer   | Average |
+----------------+---------+
| Anheuser-Busch |       3 |
| Heineken       |       2 |
| Pete's         |     3.5 |
+----------------+---------+
*/