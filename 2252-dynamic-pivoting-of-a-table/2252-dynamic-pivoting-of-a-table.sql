CREATE PROCEDURE PivotProducts()
BEGIN
  SET SESSION group_concat_max_len = 1000000; # default is 1024 bytes 
	SET @sql = NULL;
  
	SELECT GROUP_CONCAT(
		DISTINCT CONCAT(
			'SUM(IF(store = "', store, '", price, null)) AS ', store
		)
	)
	INTO @sql
	FROM Products;

	SET @sql = CONCAT('SELECT product_id, ', @sql, ' FROM Products GROUP BY 1');

	PREPARE stmt FROM @sql;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;
END