# Write your MySQL query statement below

SELECT p.firstname, p.lastName, a.city, a.state 
FROM Person p LEFT JOIN Address a
ON p.personId = a.personid
;
