# Write your MySQL query statement below

SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary 
  FROM Department d JOIN Employee e
  ON d.id = e.departmentId
  WHERE (e.departmentId, Salary) IN 
    (SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId);
