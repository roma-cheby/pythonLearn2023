SELECT customer.full_name, manager.full_name, "order".purchase_amount, "order".date
FROM "order" LEFT OUTER JOIN customer using(customer_id)
             LEFT OUTER JOIN manager using(manager_id)