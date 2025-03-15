-- create table Weather (
-- 	id serial primary key,
-- 	recordDate date,
-- 	temperature int
-- ) 
-- insert into weather (recordDate, temperature) values ('2015-01-04', 30)
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- select * from Weather
-- dia de mayor temp
-- select * from Weather where temperature = (select max(temperature) from Weather)
-- select id from Weather as w1 
-- where w1.temperature > 
-- (select max(w2.temperature) from Weather as w2 where w2.recordDate < w1.recordDate) 

-- select '1-2-2025'::date - '1-1-2025'::date -- diferencia en dias

-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
-- select id from Weather t1 
-- where t1.temperature > 
-- (select max(t2.temperature) from Weather t2 where t2.recordDate = t1.recordDate - interval '1 day')
-- (select max(t2.temperature) from Weather t2 where t1.recordDate - t2.recordDate = 1)

-- select * from Weather today
-- cross join Weather yesterday
-- where today.temperature > yesterday.temperature and today.recorddate - yesterday.recorddate = 1

-- Write your PostgreSQL query statement below
-- SELECT today.id
-- FROM Weather AS yesterday
-- CROSS JOIN Weather as today
-- WHERE today.recorddate - yesterday.recorddate = 1 AND today.temperature > yesterday.temperature

-- Activity table:
-- +------------+------------+---------------+-----------+
-- | machine_id | process_id | activity_type | timestamp |
-- +------------+------------+---------------+-----------+
-- | 0          | 0          | start         | 0.712     |
-- | 0          | 0          | end           | 1.520     |
-- | 0          | 1          | start         | 3.140     |
-- | 0          | 1          | end           | 4.120     |
-- | 1          | 0          | start         | 0.550     |
-- | 1          | 0          | end           | 1.550     |
-- | 1          | 1          | start         | 0.430     |
-- | 1          | 1          | end           | 1.420     |
-- | 2          | 0          | start         | 4.100     |
-- | 2          | 0          | end           | 4.512     |
-- | 2          | 1          | start         | 2.500     |
-- | 2          | 1          | end           | 5.000     |
-- +------------+------------+---------------+-----------+

-- create type act_name as enum('start', 'end');
-- create table activity (
-- id serial primary key, machine_id int, process_id int, activity_type act_name, timestamp float)
-- INSERT INTO activity (machine_id, process_id, activity_type, timestamp) VALUES
-- (0, 0, 'start', 0.712),
-- (0, 0, 'end', 1.520),
-- (0, 1, 'start', 3.140),
-- (0, 1, 'end', 4.120),
-- (1, 0, 'start', 0.550),
-- (1, 0, 'end', 1.550),
-- (1, 1, 'start', 0.430),
-- (1, 1, 'end', 1.420),
-- (2, 0, 'start', 4.100),
-- (2, 0, 'end', 4.512),
-- (2, 1, 'start', 2.500),
-- (2, 1, 'end', 5.000);

-- select * from activity
-- with initial as (select * from activity where activity_type = 'start'),
-- finish as (select * from activity where activity_type = 'end'),
-- resulting as (select f.machine_id, avg(f.timestamp - i.timestamp) processing_time 
-- from initial i join finish f 
-- on i.machine_id = f.machine_id and i.process_id = f.process_id
-- group by f.machine_id)

-- select res.machine_id, round(res.processing_time::numeric, 3) processing_time from resulting res


-- select t1.machine_id, round(avg(t2.timestamp - t1.timestamp)::decimal, 3) processing_time  
-- from activity t1, activity t2 
-- where t1.machine_id = t2.machine_id and t1.process_id = t2.process_id 
-- and t2.activity_type = 'end' and t1.activity_type = 'start'
-- group by t1.machine_id

-- select a.machine_id, 
-- round(avg( case when a.activity_type = 'end' then a.timestamp else -a.timestamp end)::decimal * 2, 3) processing_time 
-- from activity a
-- group by 1




