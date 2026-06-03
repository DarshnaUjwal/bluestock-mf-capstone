SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

SELECT
transaction_type,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY transaction_type;

SELECT
state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

SELECT
fund_house,
COUNT(*) AS schemes
FROM dim_fund
GROUP BY fund_house;

SELECT
AVG(sharpe_ratio)
FROM fact_performance;

SELECT
risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

SELECT
gender,
SUM(amount_inr)
FROM fact_transactions
GROUP BY gender;

SELECT
city_tier,
AVG(amount_inr)
FROM fact_transactions
GROUP BY city_tier;

SELECT
date,
sip_inflow_crore
FROM monthly_sip
ORDER BY date;