SELECT s.name
FROM sales_person s
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    JOIN company c 
    ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
    AND o.sales_id = s.sales_id
);