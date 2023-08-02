-- 코드를 입력하세요
select *
from (SELECT name, datetime
        from animal_ins
        where animal_id not in (select a.animal_id
                                 from animal_ins a
                                 inner join animal_outs b
                                 on a.animal_id = b.animal_id)
        order by datetime)
where rownum <= 3;