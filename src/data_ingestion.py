from ucimlrepo import fetch_ucirepo
import pandas as pd
from pathlib import Path

def load_default_credit_data(save_csv: bool=True):
    credit = fetch_ucirepo(id=350)

    df = pd.DataFrame(credit.data.features)
    df['default_payment_next_month'] = credit.data.targets

    if save_csv:
        Path('data/raw').mkdir(parents=True, exist_ok=True)
        df.to_csv('data/raw/default_credit_card.csv', index=False)

    return df