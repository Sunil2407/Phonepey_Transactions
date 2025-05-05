/* Decoding Transaction Dynamics on PhonePe
Scenario
PhonePe, a leading digital payments platform, has recently identified significant variations in transaction behavior across states, quarters, 
and payment categories. While some regions and transaction types demonstrate consistent growth, others show stagnation or decline. 
The leadership team seeks a deeper understanding of these patterns to drive targeted business strategies. */
USE phonepetransaction;


-- 1)Total Transactions and Amount per State per Quarter 
SELECT State, Year, Quarter,
       SUM(Transaction_count) AS Total_Transactions,
       round(SUM(Transaction_amount)) AS Total_Amount
FROM aggregatetransaction
GROUP BY State, Year, Quarter
ORDER BY Year, Quarter, Total_Amount DESC;

-- 2) Transaction Trends by Type (e.g., Recharge, Bill Payment, etc.)

SELECT Transaction_type, Year, Quarter,
       SUM(Transaction_count) AS Total_Transactions,
       round(SUM(Transaction_amount)) AS Total_Amount
FROM aggregatetransaction
GROUP BY Transaction_type, Year, Quarter
ORDER BY Year, Quarter, Transaction_type;

-- 3) Top 5 States with Highest Transaction Growth (Year-over-Year)
SELECT State, Year,
       round(SUM(Transaction_amount)) AS Total_Amount
FROM aggregatetransaction
GROUP BY State, Year
ORDER BY Year, Total_Amount DESC
LIMIT 5;
 
 -- 4) States Showing Decline or Stagnation (Negative or Low Growth)

SELECT a.State, 
       a.Year AS Current_Year,
       round(a.Total_Amount - b.Total_Amount) AS Growth
FROM (
    SELECT State, Year, SUM(Transaction_amount) AS Total_Amount
    FROM aggregatetransaction
    GROUP BY State, Year 
) a
JOIN (
    SELECT State, Year + 1 AS Year, SUM(Transaction_amount) AS Total_Amount
    FROM aggregatetransaction
    GROUP BY State, Year
) b ON a.State = b.State AND a.Year = b.Year
WHERE (b.Total_Amount - a.Total_Amount) <= 0;


/*  2. Device Dominance and User Engagement Analysis
Scenario
PhonePe aims to enhance user engagement and improve app performance by understanding user preferences across different device brands. 
The data reveals the number of registered users and app opens, segmented by device brands, regions, and time periods. However, 
trends in device usage vary significantly across regions, and some devices are disproportionately underutilized despite high registration numbers.
*/

-- 1) Top Device Brands by Registered Users

SELECT Brand_Name, SUM(User_Count) AS Total_Users
FROM aggregateusers
GROUP BY Brand_Name
ORDER BY Total_Users DESC;

-- 2) App Opens vs Registered Users by Region
SELECT State, SUM(Registered_Users) AS Total_Registered,
       SUM(AppOpens) AS Total_App_Opens,
       round((SUM(AppOpens) / SUM(Registered_Users))) * 100 AS Engagement_Rate
FROM mapusers
GROUP BY State
ORDER BY Engagement_Rate DESC; 

-- 3) Underutilized Device Brands (High registration, low app usage)

SELECT a.Brand_Name, SUM(a.User_Count) AS Total_Users,
       SUM(m.AppOpens) AS Total_App_Opens,
       round((SUM(m.AppOpens) / SUM(a.User_Count)) * 100) AS Engagement_Rate
FROM aggregateusers a
JOIN mapusers m ON a.State = m.State AND a.Year = m.Year AND a.Quarter = m.Quarter
GROUP BY a.Brand_Name
ORDER BY Engagement_Rate ASC;  -- Low to high to find underutilized ones

/* 3. Insurance Engagement Analysis
Scenario
PhonePe aims to analyze insurance transactions across various states and districts to understand the uptake of insurance services among users. 
This analysis will provide insights into user behavior, market demand, and potential areas for growth in insurance offerings.
 */
 
 -- 1) Top States by Total Insurance Amount

SELECT State,
       round(SUM(Insurance_Amount)) AS Total_Insurance_Amount,
       SUM(Insurance_Count) AS Total_Policies
FROM aggregateinsurance
GROUP BY State
ORDER BY Total_Insurance_Amount DESC;

-- 2) Quarterly Insurance Trends by State

SELECT State, Year, Quarter,
       round(SUM(Insurance_Amount)) AS Quarterly_Insurance,
       SUM(Insurance_Count) AS Policy_Count
FROM aggregateinsurance
GROUP BY State, Year, Quarter
ORDER BY State, Year, Quarter;

-- 3) District-wise Insurance Performance

SELECT State, District,
       round(SUM(Insurance_Amount)) AS District_Insurance,
       SUM(Insurance_Count) AS District_Policies
FROM topinsurance
GROUP BY State, District
ORDER BY District_Insurance DESC;

-- 4) Comparing States with High Users vs. Low Insurance Usage

SELECT a.State,
       SUM(a.User_Count) AS Total_Users,
       SUM(i.Insurance_Count) AS Insurance_Users,
       ROUND(SUM(i.Insurance_Count) / SUM(a.User_Count) * 100, 2) AS Insurance_Engagement_Rate
FROM aggregateusers a
JOIN aggregateinsurance i ON a.State = i.State AND a.Year = i.Year AND a.Quarter = i.Quarter
GROUP BY a.State
ORDER BY Insurance_Engagement_Rate ASC;


/* 4)Transaction Analysis Across States and Districts
Scenario
PhonePe is conducting an analysis of transaction data to identify the top-performing states, districts, and pin codes in terms of transaction 
volume and value. This analysis will help understand user engagement patterns and identify key areas for targeted marketing efforts.. */

-- 1. Top Performing States by Transaction Value

SELECT State,
       round(SUM(Transaction_Amount)) AS Total_Transaction_Value,
       SUM(Transaction_Count) AS Total_Transactions
FROM aggregatetransaction
GROUP BY State
ORDER BY Total_Transaction_Value DESC;

-- 2. Top Performing Districts by Transaction Count

SELECT State, District,
       SUM(Transaction_Count) AS Total_Transactions
FROM toptransaction
GROUP BY State, District
ORDER BY Total_Transactions DESC
LIMIT 10;

-- 3. Transaction Trends Over Time

SELECT State, Year, Quarter,
       round(SUM(Transaction_Amount)) AS Quarterly_Transaction_Value,
       SUM(Transaction_Count) AS Quarterly_Transactions
FROM aggregatetransaction
GROUP BY State, Year, Quarter
ORDER BY State, Year, Quarter;

-- 4.Underperforming States (Low Volume and Value)

SELECT State,
       SUM(Transaction_amount) AS Total_Value,
       SUM(Transaction_count) AS Total_Count
FROM aggregatetransaction
GROUP BY State
having Total_Value < 100000000000
ORDER BY Total_Value ASC;

/* 5. User Registration Analysis
Scenario
PhonePe aims to conduct an analysis of user registration data to identify the top states, districts, and pin codes from which the most 
users registered during a specific year-quarter combination. This analysis will provide insights into user engagement patterns and 
highlight potential growth areas
*/

-- 1)Top States by Registrations (Year-Quarter-wise)

SELECT 
    State, Year, Quarter,
    SUM(User_Count) AS Total_Registrations
FROM aggregateusers
GROUP BY State, YEAR, QUARTER
ORDER BY Total_Registrations DESC
LIMIT 10;

-- 2. Yearly Growth in Registrations per State

SELECT 
    State,
    Year,
    SUM(User_Count) AS Yearly_Registrations
FROM aggregateusers
GROUP BY State, Year
ORDER BY State, Year;

-- 3. Average Quarterly Registrations per State

SELECT 
    State,
    AVG(User_Count) AS Avg_Quarterly_Registrations
FROM phonepetransaction.aggregateusers
GROUP BY State
ORDER BY Avg_Quarterly_Registrations DESC
LIMIT 10;