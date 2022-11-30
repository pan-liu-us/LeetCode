# Write your MySQL query statement below

SELECT a.name As Employee
    FROM Employee a JOIN Employee b
        ON a.managerId = b.id 
    WHERE a.salary > b.salary;