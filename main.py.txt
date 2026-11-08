import os
from src.data_processing import load_and_clean_data, save_processed_data
from src.metrics import calculate_funnel
from src.stats import run_ab_test

def main():
    RAW_DATA_PATH = "data/raw/dannye-dlia-keisa-po-pa.xlsx" # Переименуй файл, если надо
    PROCESSED_PATH = "data/processed/clean_data.csv"

    # 1. Загрузка и очистка
    df = load_and_clean_data(RAW_DATA_PATH)
    save_processed_data(df, PROCESSED_PATH)

    # 2. Метрики
    funnel = calculate_funnel(df)
    print("\n--- Воронка оплат ---")
    print(funnel.to_string())

    # 3. Статистика
    results = run_ab_test(funnel)
    print("\n--- Результаты A/B теста ---")
    print(f"Конверсия A: {results['cr_a']:.2%}")
    print(f"Конверсия B: {results['cr_b']:.2%}")
    print(f"Относительный прирост (Lift): {results['lift_percent']:.2f}%")
    print(f"p-value: {results['p_value']:.4f}")
    
    if results['is_significant']:
        print("Вывод: Различия статистически значимы (p < 0.05). Тест успешен, можно внедрять.")
    else:
        print("Вывод: Различия статистически НЕ значимы (p >= 0.05). Внедрять новую форму рано.")

if __name__ == "__main__":
    main()