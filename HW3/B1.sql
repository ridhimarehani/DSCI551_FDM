SELECT manf AS Manufacturer
FROM Beers
GROUP BY manf
HAVING count(name) >= 3;

/* Output
+----------------+
| Manufacturer   |
+----------------+
| Anheuser-Busch |
+----------------+
*/