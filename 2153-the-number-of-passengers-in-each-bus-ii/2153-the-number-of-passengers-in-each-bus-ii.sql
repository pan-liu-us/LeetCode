# Write your MySQL query statement below

WITH temp1 AS (
  SELECT bus_id, b.arrival_time, capacity, COUNT(passenger_id) AS num
  FROM Buses b LEFT JOIN Passengers p ON p.arrival_time <= b.arrival_time
  WHERE bus_id IS NOT NULL
  GROUP BY bus_id
  ORDER BY arrival_time
)

SELECT bus_id, passengers_cnt
  FROM (
    SELECT bus_id, capacity, num,
        @passengers_cnt:= LEAST(capacity, num - @accum) AS passengers_cnt, 
        @accum:= @accum + @passengers_cnt AS accum
        FROM temp1, (SELECT @accum:= 0, @passengers_cnt:= 0) init
  ) temp2
  ORDER BY bus_id;

