-- 코드를 입력하세요
select a.product_id, b.product_name, (a.total_amount * b.price) as total_sales
from (SELECT product_id, sum(amount) as total_amount
        from food_order
        where to_char(produce_date, 'yyyy-mm') = '2022-05'
        group by product_id) a
inner join food_product b on a.product_id = b.product_id
order by total_sales desc, a.product_id
;