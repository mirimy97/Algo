-- 코드를 입력하세요
SELECT a.category, sum(b.sales) as total_sales
from book a
inner join book_sales b
on a.book_id = b.book_id
where extract(year from b.sales_date) = 2022 and extract(month from b.sales_date) = 1
group by a.category
order by a.category;