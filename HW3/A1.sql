SELECT emp_no
FROM employees
WHERE first_name = 'mary' 
AND SUBSTRING(last_name, length(last_name)-1,1) = LOWER('o') 
AND ASCII(substring(last_name, length(last_name)-1,1)) BETWEEN 97 AND 122;

/* OUTPUT
+--------+
| emp_no |
+--------+
|  16021 |
|  21756 |
|  52983 |
|  73998 |
|  78783 |
|  88698 |
| 101753 |
| 216534 |
| 263268 |
| 410311 |
| 423386 |
| 459548 |
| 491899 |
+--------+ 
*/