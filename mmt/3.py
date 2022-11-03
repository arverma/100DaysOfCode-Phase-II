"""
order_item
----------

order_id
item_id
order_ts
order_quantity
order_item_amount

a 10 1
b 10 2
c 10 3
d 9 1


Write a query to print the top 10 selling items quantity yesterday.

iteam, quantity


with cte as(
    select item_id, sum(order_quantity) as net_quantity_sold from cte1 where order_ts>start_ts AND order_ts < end_ts order group by item_id)
    select item_id, net_quantity_sold, ROW_NUMBER() OVER(PARTITION BY item_id ORDER BY net_quantity_sold ASC) as row_num from cte where row_num <=10;


start_ts =
end_ts=

with cte as(
    select item, sum(order_quantity) as total_order_quantity from order_item group by item),
    select item, total_order_quantity from cte, ROW_NUMBER() OVER(PARTITION BY total_order_quantity ORDER BY total_order_quantity) where order_ts>start_ts AND order_ts < end_ts order by total_order_quantity;



#
# list1 = ['a', 'c', 'l','m','z']
# list2 = []
#
# a = list(set(list1).intersection(set(list2)))
# b = list(set(list1).difference(set(list2)))
# c = list(set(list2).difference(set(list1)))
#
# print(a, b, c)
"""
























