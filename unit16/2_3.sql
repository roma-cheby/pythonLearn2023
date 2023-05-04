SELECT "order".order_no, manager.full_name, customer.full_name
FROM "order" LEFT OUTER JOIN customer using(customer_id)
             LEFT OUTER JOIN manager using(manager_id)
WHERE customer.city != manager.city