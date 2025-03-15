CREATE TABLE job_listings (
    id SERIAL PRIMARY KEY,
    title TEXT,
    company TEXT,
    location TEXT,
    published DATE,
    applicants INT,
    url TEXT UNIQUE,
    description TEXT
);
