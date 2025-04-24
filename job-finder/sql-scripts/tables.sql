-- list tables
-- SELECT table_name
-- FROM information_schema.tables
-- WHERE table_schema = 'job_finder'; -- Replace 'your_database_name

-- create table if not exists google_query (
--     id serial primary key,
--     query TEXT,
--     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
-- )

-- create TABLE IF NOT EXISTS google_queries_urls (
--     id serial primary key,
--     google_query_id integer REFERENCES google_query(id),
--     url text
-- )

-- create TABLE IF NOT EXISTS jobs (
--     id serial primary key,
--     google_queries_urls_id integer REFERENCES google_queries_urls(id),
--     jobid INTEGER,
--     url text,
--     title text,
--     company text,
--     location text,
--     published text,
--     applications text,
--     description text
-- )

-- select * from google_query
-- select * from google_queries_urls