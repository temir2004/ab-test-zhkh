import pandas as pd

def calculate_funnel(df: pd.DataFrame) -> pd.DataFrame:
    """Считает воронку и конверсию по группам."""
    funnel = df.groupby('group').agg(
        step1_opened=('step1_opened', 'count'),
        step2_entered=('step2_entered', 'count'),
        step3_confirmed=('step3_confirmed', 'count'),
        step4_success=('step4_success', 'count')
    )
    
    # Считаем CR (из шага 1 в шаг 4)
    funnel['CR'] = funnel['step4_success'] / funnel['step1_opened']
    return funnel