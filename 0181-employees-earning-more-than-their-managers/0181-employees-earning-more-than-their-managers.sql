# Write your MySQL query statement below

SELECT a.name As Employee
FROM Employee a, Employee b
WHERE a.managerId = b.id AND a.salary > b.salary;