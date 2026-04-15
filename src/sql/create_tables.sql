-- Create main sales table

CREATE TABLE sales_data (
    Store INT,
    Date DATE,
    Sales FLOAT,
    Customers INT,
    Promo INT,
    StateHoliday VARCHAR(10),
    SchoolHoliday INT,
    StoreType VARCHAR(5),
    Assortment VARCHAR(5),
    CompetitionDistance FLOAT,
    Promo2 INT,
    Year INT,
    Month INT,
    WeekOfYear INT,
    IsWeekend INT
);