import pandas as pd
import os


def load_and_clean_data(raw_data_path: str) -> pd.DataFrame:
    """Загружает данные, очищает от выбросов и объединяет таблицы."""
    print("Загрузка данных...")
    users = pd.read_excel(raw_data_path, sheet_name='Пользователи')
    payments = pd.read_excel(raw_data_path, sheet_name='Платежи')

    print("Очистка аномалий (EDA)...")

    # 1. Очистка пользователей
    # Удаляем пользователей с аномальным возрастом (<=0 или >=100), пустым городом или отсутствующей группой
    users_clean = users[
        (users['age'] > 0) &
        (users['age'] < 100) &
        (users['city'].notna()) &
        (users['group'].notna())
        ].copy()

    # 2. Очистка платежей
    # Удаляем платежи без user_id
    payments_clean = payments[payments['user_id'].notna()].copy()

    # 3. Объединение
    # Переименуем group в users, чтобы избежать конфликта имен при merge
    users_clean = users_clean.rename(columns={'group': 'group_users'})
    df = payments_clean.merge(users_clean[['user_id', 'group_users']], on='user_id', how='inner')

    # 4. Проверка сплитования: группа в платежах должна совпадать с группой в пользователях
    # Если группа в платежах пуста или не совпадает с users - удаляем такую запись
    df = df[df['group'] == df['group_users']]

    # Удаляем временный столбец
    df = df.drop(columns=['group_users'])

    print(f"Данные готовы. Уникальных попыток оплаты: {len(df)}")
    return df


def save_processed_data(df: pd.DataFrame, output_path: str):
    """Сохраняет очищенные данные в CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Очищенные данные сохранены в {output_path}")