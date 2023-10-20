-- 코드를 입력하세요
SELECT flavor
from (select flavor, sum(total_order) as total_order
        from (select * from first_half union all select * from july)
        group by flavor
        order by total_order desc)
where rownum <= 3;
        