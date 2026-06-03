# Data Dictionary

## Project

Bluestock Fintech - Mutual Fund Analytics Capstone

---

## dim_date

Source: Generated from NAV history dates

| Column     | Data Type | Description    |
| ---------- | --------- | -------------- |
| date       | DATE      | Calendar date  |
| year       | INTEGER   | Year value     |
| quarter    | INTEGER   | Quarter number |
| month      | INTEGER   | Month number   |
| month_name | TEXT      | Month name     |
| weekday    | TEXT      | Day of week    |

---

## dim_fund

Source: 01_fund_master.csv

| Column             | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| amfi_code          | INTEGER   | Unique AMFI scheme code     |
| fund_house         | TEXT      | Mutual fund company         |
| scheme_name        | TEXT      | Scheme name                 |
| category           | TEXT      | Fund category               |
| sub_category       | TEXT      | Fund sub-category           |
| plan               | TEXT      | Direct or Regular plan      |
| launch_date        | DATE      | Scheme launch date          |
| benchmark          | TEXT      | Benchmark index             |
| expense_ratio_pct  | REAL      | Expense ratio percentage    |
| exit_load_pct      | REAL      | Exit load percentage        |
| min_sip_amount     | REAL      | Minimum SIP investment      |
| min_lumpsum_amount | REAL      | Minimum lump sum investment |
| fund_manager       | TEXT      | Fund manager name           |
| risk_category      | TEXT      | Risk category               |
| sebi_category_code | TEXT      | SEBI classification code    |

---

## fact_nav

Source: 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | INTEGER   | Scheme code     |
| date      | DATE      | NAV date        |
| nav       | REAL      | Net Asset Value |

---

## fact_transactions

Source: 08_investor_transactions.csv

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Investor identifier        |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Scheme code                |
| transaction_type   | TEXT      | SIP, Lumpsum or Redemption |
| amount_inr         | REAL      | Transaction amount in INR  |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age category      |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakhs     |
| payment_mode       | TEXT      | Payment method             |
| kyc_status         | TEXT      | KYC verification status    |

---

## fact_performance

Source: 07_scheme_performance.csv

| Column             | Data Type | Description                      |
| ------------------ | --------- | -------------------------------- |
| amfi_code          | INTEGER   | Scheme code                      |
| return_1yr_pct     | REAL      | 1-year return percentage         |
| return_3yr_pct     | REAL      | 3-year return percentage         |
| return_5yr_pct     | REAL      | 5-year return percentage         |
| benchmark_3yr_pct  | REAL      | Benchmark 3-year return          |
| alpha              | REAL      | Alpha metric                     |
| beta               | REAL      | Beta metric                      |
| sharpe_ratio       | REAL      | Sharpe ratio                     |
| sortino_ratio      | REAL      | Sortino ratio                    |
| std_dev_ann_pct    | REAL      | Annualized standard deviation    |
| max_drawdown_pct   | REAL      | Maximum drawdown percentage      |
| aum_crore          | REAL      | Assets under management in crore |
| expense_ratio_pct  | REAL      | Expense ratio percentage         |
| morningstar_rating | INTEGER   | Morningstar rating               |
| risk_grade         | TEXT      | Risk grade classification        |

---

## fact_aum

Source: 03_aum_by_fund_house.csv

| Column         | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Reporting date            |
| fund_house     | TEXT      | Fund house name           |
| aum_lakh_crore | REAL      | AUM in lakh crore         |
| aum_crore      | REAL      | AUM in crore              |
| num_schemes    | INTEGER   | Number of schemes managed |
