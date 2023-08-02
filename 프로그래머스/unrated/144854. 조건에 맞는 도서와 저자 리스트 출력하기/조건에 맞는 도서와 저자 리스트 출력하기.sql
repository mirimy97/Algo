-- 코드를 입력하세요
SELECT a.book_id, b.author_name, to_char(a.published_date, 'YYYY-MM-DD') as published_date
from book a
inner join author b
on a.author_id = b.author_id
where a.category = '경제'
order by a.published_date;