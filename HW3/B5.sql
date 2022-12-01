SELECT DISTINCT(drinker) AS Drinker
FROM Likes l1
WHERE EXISTS (SELECT beer FROM Likes l2 WHERE l1.drinker = l2.drinker AND beer = 'Bud')
AND NOT EXISTS (SELECT beer FROM Likes l2 WHERE l1.drinker = l2.drinker AND beer = 'Summerbrew');

/* Output
+----------+
| Drinker  |
+----------+
| Bill     |
| Jennifer |
+----------+
*/