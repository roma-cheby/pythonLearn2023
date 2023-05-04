SELECT customer.full_name, "order".order_no
FROM "order" LEFT OUTER JOIN customer using(customer_id)
             LEFT OUTER JOIN manager using(manager_id)
WHERE "order".manager_id is null