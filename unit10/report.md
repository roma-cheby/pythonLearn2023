TASK 2
1) SELECT phone_color FROM table_checkout
   WHERE sold_count = (SELECT (max(sold_count)) FROM table_checkout)

2) SELECT phone_color FROM table_checkout
   WHERE sold_count = (
   SELECT (max(sold_count)) FROM table_checkout
   WHERE phone_color = "Blue" or phone_color = "Red")

3) SELECT phone_color FROM table_checkout
   WHERE sold_count = (
   SELECT (min(sold_count)) FROM table_checkout)