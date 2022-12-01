# Write your MySQL query statement below

SELECT b.bus_id, COUNT(X.arrival_time) AS passengers_cnt
  FROM Buses b LEFT JOIN
    (
      SELECT p.passenger_id, MIN(b.arrival_time) AS arrival_time
        FROM Passengers p
        INNER JOIN Buses b
        ON p.arrival_time <= b.arrival_time
        GROUP BY passenger_id
    ) X
  ON b.arrival_time = X.arrival_time
  GROUP BY b.bus_id
  ORDER BY b.bus_id;