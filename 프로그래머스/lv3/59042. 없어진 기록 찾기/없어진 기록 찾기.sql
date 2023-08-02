-- 코드를 입력하세요
SELECT b.animal_id, b.name
from animal_ins a
right join animal_outs b
on a.animal_id = b.animal_id
where b.animal_id not in (select animal_id
                         from animal_ins)
order by b.animal_id, b.name;