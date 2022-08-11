DROP TABLE IF EXISTS "raw";

CREATE TABLE "raw" AS
SELECT 
    o.date order_date,
    i.date invoice_date,
    pmt.date payment_date,
    c.id customer_id,
    o.order_number,
    i.invoice_number,
    pmt.payment_number,
    sum(ol.quantity) total_order_quantity,
    sum(ol.usd_amount) total_order_usd_amount,
    julianday(i.date) - julianday(o.date) order_to_invoice_lag_days,
    julianday(pmt.date) - julianday(i.date) invoice_to_payment_lag_days
FROM order_lines ol
LEFT JOIN orders o ON o.order_number = ol.order_number
LEFT JOIN products p ON p.id = ol.product_id
LEFT JOIN invoices i ON i.order_number = ol.order_number
LEFT JOIN payments pmt ON pmt.invoice_number = i.invoice_number
LEFT JOIN customers c ON c.id = o.customer_id
GROUP BY 1,2,3,4,5,6,7,10,11