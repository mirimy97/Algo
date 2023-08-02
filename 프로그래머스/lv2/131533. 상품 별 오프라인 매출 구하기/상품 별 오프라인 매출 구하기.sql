-- 코드를 입력하세요
select c.product_code, (c.price * d.sales_amount) as sales
from product c
inner join (SELECT a.product_code, sum(b.sales_amount) as sales_amount
            from product a
            inner join offline_sale b
            on a.product_id = b.product_id
            group by a.product_code) d
on c.product_code = d.product_code
order by sales desc, c.product_code;