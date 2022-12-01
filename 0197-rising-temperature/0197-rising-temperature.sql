# Write your MySQL query statement below

SELECT w2.id
  FROM Weather w1 JOIN Weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
  WHERE w1.temperature < w2.temperature;