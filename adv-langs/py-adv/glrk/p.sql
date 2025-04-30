-- +---------+------------+------+----------+-------+\
-- | sale_id | product_id | year | quantity | price |\
-- +---------+------------+------+----------+-------+ \
-- | 1       | 100        | 2008 | 10       | 5000  |\
-- | 2       | 100        | 2009 | 12       | 5000  |\
-- | 7       | 200        | 2011 | 15       | 9000  |\
-- +---------+------------+------+----------+-------+\

-- SELECT * from produtcs
-- with ranked_sales as (select product_id, year, price, 
--     row_number() over (PARTITION BY product_id) as row_num
-- from produtcs)

-- select * from ranked_sales
-- select * from ranked_sales where row_num = 1

-- create table IF NOT EXISTS produtcs (
--     sale_id int,
--     product_id int,
--     year int,
--     quantity int,
--     price int
-- );

-- insert into produtcs (sale_id, product_id, year, quantity, price) values
--     (1,100,2008,10,5000),
--     (2,100,2009,12,5000),
--     (7,200,2011,15,9000);

-- select * from google_queries_urls

-- create table if not EXISTS employees(
--     id serial primary key,
--     name text,
--     salary integer,
--     managerId int
-- )

-- SELECT * FROM employees

-- insert INTO employees (name, salary, managerId) VALUES  
--     ('Joe'   , 70000  , 3),         
--     ('Henry' , 80000  , 4),        
--     ('Sam'   , 60000  , Null),      
--     ('Max'   , 90000  , Null );    

-- with final as (select e1.id, e1.name, e1.salary, e2.name m, e2.salary ms  from employees as e1 join employees as e2
-- on e1.managerId = e2.id)

-- select * from final

-- select id, name from final where salary > ms





