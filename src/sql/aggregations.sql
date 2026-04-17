-- Monthly sales per store

SELECT 
    Store,
    Year ,
    Month,
    SUM(Sales) AS Total_Sales,
    AVG(Sales) As Avg_Sales
FROM sales_data
GROUP BY Store, Year, Month
ORDER BY Store, Year, Month;

-- Weekly sales per trend

SELECT
    Year,
    WeekOfYear,
    SUM(Sales) AS  Total_Sales
FROM sales_data
GROUP BY Year, WeekOfYear
ORDER BY Year, WeekOfYear;

-----------------------------------------

-- 1. Sales by Store

CREATE TABLE sales_by_store AS
SELECT 
    Store,
    SUM(Sales) AS total_sales,
    AVG(Sales) AS avg_sales,
    SUM(Customers) AS total_customers
FROM sales_data
GROUP BY Store;


-- 2. Monthly Sales Trend

CREATE TABLE monthly_sales AS
SELECT 
    Year,
    Month,
    SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Year, Month
ORDER BY Year, Month;


-- 3. Weekly Sales Pattern

CREATE TABLE weekly_sales AS
SELECT 
    WeekOfYear,
    SUM(Sales) AS total_sales
FROM sales_data
GROUP BY WeekOfYear
ORDER BY WeekOfYear;


--CTE
CREATE TABLE monthly_sales_final AS

WITH base AS (
    SELECT 
        Year,
        Month,
        SUM(Sales) AS total_sales
    FROM sales_data
    GROUP BY Year, Month
)

SELECT 
    Year,
    Month,
    total_sales,

    -- Running total
    SUM(total_sales) OVER (ORDER BY Year, Month) AS running_total,

    -- Moving average
    AVG(total_sales) OVER (
        ORDER BY Year, Month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3,

    -- Growth %
    ROUND(
        (
            (total_sales - LAG(total_sales) OVER (ORDER BY Year, Month))
            / LAG(total_sales) OVER (ORDER BY Year, Month)
        )::NUMERIC * 100,
        2
    ) AS growth_pct

FROM base
ORDER BY Year, Month;