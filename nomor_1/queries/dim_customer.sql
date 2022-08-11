DROP TABLE IF EXISTS "dim_customer";

CREATE TABLE IF NOT EXISTS "dim_customer" (
  "id" int,
  "name" varchar
);

INSERT INTO "dim_customer" 
SELECT * FROM "customers";