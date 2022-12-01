SELECT bar AS Bar, COUNT(beer) AS Total
FROM Sells
WHERE price >= 2
GROUP BY bar;

/* Output
+------------+-------+
| Bar        | Total |
+------------+-------+
| Bob's bar  |     2 |
| Joe's bar  |     4 |
| Mary's bar |     2 |
+------------+-------+
*/