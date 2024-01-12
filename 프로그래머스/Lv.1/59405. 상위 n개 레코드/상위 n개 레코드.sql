-- 코드를 입력하세요
select name
from (SELECT name, datetime
from animal_ins
order by datetime)
where rownum = 1;