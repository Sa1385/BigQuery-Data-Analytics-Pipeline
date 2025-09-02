# Calculated Fields for E-Commerce Dashboard

## KPIs
- **Total Revenue**
  ```sql
  SUM(revenue)
  ```
- **Total Orders**
  ```sql
  COUNT(DISTINCT order_id)
  ```
- **Total Customers**
  ```sql
  COUNT(DISTINCT customer_id)
  ```
- **Average Order Value**
  ```sql
  SUM(revenue) / COUNT(DISTINCT order_id)
  ```

## Time Analysis
- **Monthly Revenue**
  ```sql
  DATE_TRUNC(order_date, MONTH)
  ```
- **Year**
  ```sql
  EXTRACT(YEAR FROM order_date)
  ```

## YoY Comparison
- **Revenue This Year**
  ```sql
  CASE WHEN EXTRACT(YEAR FROM order_date) = EXTRACT(YEAR FROM CURRENT_DATE()) 
       THEN revenue END
  ```
- **Revenue Last Year**
  ```sql
  CASE WHEN EXTRACT(YEAR FROM order_date) = EXTRACT(YEAR FROM CURRENT_DATE()) - 1 
       THEN revenue END
  ```
- **YoY Growth %**
  ```sql
  (SUM(Revenue_This_Year) - SUM(Revenue_Last_Year)) / SUM(Revenue_Last_Year)
  ```

## Customer Analysis
- **Customer Type**
  ```sql
  CASE 
    WHEN order_count = 1 THEN "New Customer"
    ELSE "Returning Customer"
  END
  ```
