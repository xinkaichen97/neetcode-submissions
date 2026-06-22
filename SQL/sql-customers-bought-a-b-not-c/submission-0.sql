SELECT c.customer_id, c.customer_name
FROM customers c
JOIN (
    SELECT customer_id
    FROM orders
    WHERE product_name IN ('A', 'B', 'C')
    GROUP BY customer_id
    HAVING MAX(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END) = 1
       AND MAX(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END) = 1
       AND MAX(CASE WHEN product_name = 'C' THEN 1 ELSE 0 END) = 0
) o ON c.customer_id = o.customer_id
ORDER BY c.customer_name;