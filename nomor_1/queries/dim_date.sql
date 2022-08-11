DROP TABLE IF EXISTS "dim_date";

CREATE TABLE IF NOT EXISTS "dim_date" (
  "id" INTEGER PRIMARY KEY,
  "date" date,
  "month" int,
  "quarter_of_year" int,
  "year" int,
  "is_weekend" boolean
);

INSERT INTO "dim_date" (date, month, quarter_of_year, year, is_weekend)
WITH RECURSIVE
-- Define a CTE to hold the recursive output
rDateDimensionMinute (CalendarDateInterval)
AS
    (
        -- The anchor of the recursion is the start date of the date dimension
        SELECT datetime('2018-01-01 00:00:00')
        UNION ALL
        -- The recursive query increments the time interval by the desired amount
        -- This can be any time increment (monthly, daily, hours, minutes)
        SELECT datetime(CalendarDateInterval, '+24 hour') FROM rDateDimensionMinute
        -- Set the number of recursions
        -- Functionally, this is the number of periods in the date dimension
        LIMIT 100000
    )

SELECT
    date(CalendarDateInterval),
    cast(strftime('%m', CalendarDateInterval) as int),
    case 
        when 0 + strftime('%m', CalendarDateInterval) between  1 and  3 then 1
        when 0 + strftime('%m', CalendarDateInterval) between  4 and  6 then 2
        when 0 + strftime('%m', CalendarDateInterval) between  7 and  9 then 3
        when 0 + strftime('%m', CalendarDateInterval) between 10 and 12 then 4
    end as quarter,
    cast(strftime('%Y', CalendarDateInterval) as int),
    case
        when 0 + strftime('%w', CalendarDateInterval) = 0 then 1
        when 0 + strftime('%w', CalendarDateInterval) = 6 then 1
        else 0
    end as is_weekend
FROM rDateDimensionMinute;
