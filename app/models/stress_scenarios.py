import numpy as np

def stress_test(pnl):
    return {
        "extreme_loss": np.min(pnl),
        "avg_tail_loss": np.mean(pnl[pnl < np.percentile(pnl, 5)])
    }