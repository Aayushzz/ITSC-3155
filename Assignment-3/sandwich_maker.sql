CREATE DATABASE sandwich_maker;
USE sandwich_maker;

CREATE TABLE sandwiches (
	sandwich_size varchar(50),
    price decimal(5,2)
);

INSERT INTO sandwiches (sandwich_size, price) VALUES
  ('small', 1.75),
  ('medium', 3.25),
  ('large', 5.50);
  
  SELECT * FROM sandwiches;
  
CREATE TABLE resources (
  item   VARCHAR(50),
  amount INT
);

INSERT INTO resources (item, amount) VALUES
  ('bread', 12),
  ('ham', 18),
  ('cheese', 24);
  
SELECT * FROM resources;

CREATE TABLE recipes (
  sandwich_size VARCHAR(50),
  item          VARCHAR(50),
  amount        INT
);

INSERT INTO recipes (sandwich_size, item, amount) VALUES
  ('small',  'bread',  2),
  ('small',  'ham',    4),
  ('small',  'cheese', 4),
  ('medium', 'bread',  4),
  ('medium', 'ham',    6),
  ('medium', 'cheese', 8),
  ('large',  'bread',  6),
  ('large',  'ham',    8),
  ('large',  'cheese', 12);
  
  SELECT * FROM recipes
	
