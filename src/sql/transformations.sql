-- Example transformations

SELECT
    Store,
    Date,
    Sales,
    Customers,
    Promo,
    StoreType,
    Assortment,
    CompetitionDistance,
    Year,
    Month,
    WeekOfYear,
    IsWeekend
FROM sales_data
WHERE Sales > 0;