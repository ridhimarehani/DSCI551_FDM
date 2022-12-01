SELECT dept_no
FROM dept_manager
GROUP BY dept_no
HAVING COUNT(DISTINCT(emp_no)) >= 3;

/* Output
---------+
| dept_no |
+---------+
| d004    |
| d006    |
| d009    |
+---------+
 */