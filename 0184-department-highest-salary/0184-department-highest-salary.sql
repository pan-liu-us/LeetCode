# Write your MySQL query statement below

WITH temp AS
(SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary 
  FROM Department d JOIN Employee e
  ON d.id = e.departmentId)


SELECT * FROM temp
  WHERE (Department, Salary) IN 
  (SELECT Department, MAX(Salary) FROM temp GROUP BY Department);
