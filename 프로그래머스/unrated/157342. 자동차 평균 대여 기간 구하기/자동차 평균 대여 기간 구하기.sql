-- 코드를 입력하세요
SELECT car_id, round(avg(end_date - start_date + 1), 1) as average_duration
from car_rental_company_rental_history
group by car_id
having round(avg(end_date - start_date + 1) * 10) / 10 >= 7
order by round(avg(end_date - start_date + 1) * 10) / 10 desc, car_id desc;