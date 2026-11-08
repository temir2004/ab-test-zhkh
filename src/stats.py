from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
import numpy as np

def run_ab_test(funnel: pd.DataFrame):
    """Проводит Z-test для двух пропорций."""
    successes = [funnel.loc['B', 'step4_success'], funnel.loc['A', 'step4_success']]
    nobs = [funnel.loc['B', 'step1_opened'], funnel.loc['A', 'step1_opened']]

    z_stat, p_value = proportions_ztest(successes, nobs, alternative='two-sided')
    
    cr_a = funnel.loc['A', 'CR']
    cr_b = funnel.loc['B', 'CR']
    lift = ((cr_b - cr_a) / cr_a) * 100

    return {
        'cr_a': cr_a,
        'cr_b': cr_b,
        'lift_percent': lift,
        'z_stat': z_stat,
        'p_value': p_value,
        'is_significant': p_value < 0.05
    }