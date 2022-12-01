SELECT DISTINCT(first_name), last_name
FROM employees emp INNER JOIN salaries sal
ON emp.emp_no = sal.emp_no
WHERE sal.salary >= 150000;

/* Output 
+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Tokuyasu   | Pesch     |
| Ibibia     | Junet     |
| Xiahua     | Whitcomb  |
| Lansing    | Kambil    |
| Willard    | Baca      |
| Tsutomu    | Alameldin |
| Charmane   | Griswold  |
| Weicheng   | Hatcliff  |
| Mitsuyuki  | Stanfel   |
| Sanjai     | Luders    |
| Honesty    | Mukaidono |
| Weijing    | Chenoweth |
| Shin       | Birdsall  |
| Mohammed   | Moehrke   |
| Lidong     | Meriste   |
+------------+-----------+
*/