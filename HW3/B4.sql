SELECT DISTINCT(bar) AS Bar
FROM Sells
WHERE price = (SELECT max(price) FROM Sells);

/* Output 
+-----------+
| Bar       |
+-----------+
| Joe's bar |
+-----------+
*/