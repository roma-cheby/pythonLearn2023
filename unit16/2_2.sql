SELECT customer.full_name
FROM customer
    EXCEPT
SELECT customer.full_name
FROM "order"
         JOIN customer using(customer_id)
