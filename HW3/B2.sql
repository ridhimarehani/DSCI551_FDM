SELECT name AS Drinker
FROM Drinkers
WHERE name NOT IN (SELECT drinker FROM Frequents);

/* 
Empty set
*/



