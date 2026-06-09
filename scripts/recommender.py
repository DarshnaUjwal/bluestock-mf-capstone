import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

performance = pd.read_csv(
    BASE_DIR /
    "data" /
    "processed" /
    "scheme_performance_cleaned.csv"
)

def recommend_funds(risk_level):

    recommendations = performance[
        performance["risk_grade"]
        .str.contains(
            risk_level,
            case=False,
            na=False
        )
    ]

    recommendations = recommendations.sort_values(
        "sharpe_ratio",
        ascending=False
    )

    return recommendations[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio"
        ]
    ].head(3)

if __name__ == "__main__":

    risk = input(
        "Enter Risk Appetite (Low / Moderate / High): "
    )

    print("\nTop Recommended Funds:\n")

    print(
        recommend_funds(risk)
    )