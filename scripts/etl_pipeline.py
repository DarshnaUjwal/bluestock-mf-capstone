from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# PATHS

processed_path = Path("data/processed")
db_path = Path("data/db/bluestock_mf.db")

# DATABASE CONNECTION

engine = create_engine(
    f"sqlite:///{db_path}"
)

print("Loading cleaned datasets...\n")

# LOAD CLEANED DATASETS

fund_master = pd.read_csv(
    processed_path / "fund_master_cleaned.csv"
)

nav_history = pd.read_csv(
    processed_path / "nav_history_cleaned.csv"
)

aum = pd.read_csv(
    processed_path / "aum_by_fund_house_cleaned.csv"
)

monthly_sip = pd.read_csv(
    processed_path / "monthly_sip_inflows_cleaned.csv"
)

category_inflows = pd.read_csv(
    processed_path / "category_inflows_cleaned.csv"
)

folio_count = pd.read_csv(
    processed_path / "industry_folio_count_cleaned.csv"
)

performance = pd.read_csv(
    processed_path / "scheme_performance_cleaned.csv"
)

transactions = pd.read_csv(
    processed_path / "investor_transactions_cleaned.csv"
)

holdings = pd.read_csv(
    processed_path / "portfolio_holdings_cleaned.csv"
)

benchmark = pd.read_csv(
    processed_path / "benchmark_indices_cleaned.csv"
)

date_dim = pd.read_csv(
    processed_path / "dim_date.csv"
)

# LOAD TABLES INTO SQLITE

print("Loading tables into SQLite...\n")

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

date_dim.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

monthly_sip.to_sql(
    "monthly_sip",
    engine,
    if_exists="replace",
    index=False
)

category_inflows.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)

folio_count.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

holdings.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

benchmark.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

# VERIFY ROW COUNTS

print("\n========== ROW COUNT VERIFICATION ==========\n")

print(f"dim_fund               : {len(fund_master)}")
print(f"dim_date               : {len(date_dim)}")
print(f"fact_nav               : {len(nav_history)}")
print(f"fact_transactions      : {len(transactions)}")
print(f"fact_performance       : {len(performance)}")
print(f"fact_aum               : {len(aum)}")
print(f"monthly_sip            : {len(monthly_sip)}")
print(f"category_inflows       : {len(category_inflows)}")
print(f"industry_folio_count   : {len(folio_count)}")
print(f"portfolio_holdings     : {len(holdings)}")
print(f"benchmark_indices      : {len(benchmark)}")

print("\n===========================================")
print("SQLite database loaded successfully.")
print(f"Database location: {db_path}")
