DROP TABLE IF EXISTS "fact_order_accumulating";

CREATE TABLE IF NOT EXISTS "fact_order_accumulating" (
  "order_date_id" int,
  "invoice_date_id" int,
  "payment_date_id" int,
  "customer_id" int,
  "order_number" varchar,
  "invoice_number" varchar,
  "payment_number" varchar,
  "total_order_quantity" int,
  "total_order_usd_amount" decimal,
  "order_to_invoice_lag_days" int,
  "invoice_to_payment_lag_days" int
);

INSERT INTO "fact_order_accumulating"
SELECT  
    cast(dd_order.id as int) order_date_id,
    cast(dd_invoice.id as int) invoice_date_id,
    cast(dd_payment.id as int) payment_date_id,
    dc.id customer_id,
    raw.order_number,
    raw.invoice_number,
    raw.payment_number,
    raw.total_order_quantity,
    raw.total_order_usd_amount,
    raw.order_to_invoice_lag_days,
    raw.invoice_to_payment_lag_days
FROM raw
LEFT JOIN dim_date dd_order ON dd_order.date = raw.order_date
LEFT JOIN dim_date dd_invoice ON dd_invoice.date = raw.invoice_date
LEFT JOIN dim_date dd_payment ON dd_payment.date = raw.payment_date
LEFT JOIN dim_customer dc ON dc.id = raw.customer_id;