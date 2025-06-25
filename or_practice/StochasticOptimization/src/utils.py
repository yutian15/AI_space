import numpy as np
import pandas as pd

def load_demand_samples(filepath):
    df = pd.read_csv(filepath)
    return df['demand'].values 