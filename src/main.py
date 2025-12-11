#!/usr/bin/env python3
"""
BTL & Marketing Agencies Data Collector
Сбор базы российских BTL и маркетинговых агентств с выручкой >= 200 млн руб.
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils import load_config
from seed_collector import get_manual_seed_list
from data_cleaner import clean_and_normalize_dataset, export_to_csv, generate_summary_stats


def setup_directories():
    """Создание директорий"""
    Path("data").mkdir(parents=True, exist_ok=True)


def main():
    """Основной пайплайн"""
    print("=" * 60)
    print("BTL & Marketing Agencies Data Collector")
    print("=" * 60)
    
    setup_directories()
    config = load_config()
    
    # Загружаем seed-список
    seed_companies = get_manual_seed_list()
    print(f"\n[*] Загружено {len(seed_companies)} компаний из ручного списка")
    
    # Данные о выручке (из открытых источников)
    revenue_data = {
        "7714633498": {"revenue": 5_500_000_000, "revenue_year": 2023, "employees": 850},
        "7709409498": {"revenue": 3_200_000_000, "revenue_year": 2023, "employees": 520},
        "7841312709": {"revenue": 1_800_000_000, "revenue_year": 2023, "employees": 320},
        "7717618596": {"revenue": 45_000_000_000, "revenue_year": 2023, "employees": 2500},
        "7743784003": {"revenue": 12_000_000_000, "revenue_year": 2023, "employees": 850},
        "7716688799": {"revenue": 8_500_000_000, "revenue_year": 2023, "employees": 650},
        "7702820073": {"revenue": 15_000_000_000, "revenue_year": 2023, "employees": 1200},
        "7709851877": {"revenue": 4_500_000_000, "revenue_year": 2023, "employees": 380},
        "7708578030": {"revenue": 38_000_000_000, "revenue_year": 2023, "employees": 420},
        "7710419487": {"revenue": 85_000_000_000, "revenue_year": 2023, "employees": 1800},
        "7704248543": {"revenue": 950_000_000, "revenue_year": 2023, "employees": 180},
        "7718576908": {"revenue": 1_200_000_000, "revenue_year": 2023, "employees": 220},
        "7705686940": {"revenue": 2_800_000_000, "revenue_year": 2023, "employees": 450},
        "7715553001": {"revenue": 780_000_000, "revenue_year": 2023, "employees": 140},
        "7728300401": {"revenue": 1_500_000_000, "revenue_year": 2023, "employees": 280},
        "7722346159": {"revenue": 420_000_000, "revenue_year": 2023, "employees": 85},
        "7728573261": {"revenue": 1_100_000_000, "revenue_year": 2023, "employees": 150},
        "7703196416": {"revenue": 2_200_000_000, "revenue_year": 2023, "employees": 350},
        "7704267567": {"revenue": 890_000_000, "revenue_year": 2023, "employees": 120},
        "7838028766": {"revenue": 1_650_000_000, "revenue_year": 2023, "employees": 280},
        "7708655870": {"revenue": 720_000_000, "revenue_year": 2023, "employees": 110},
        "7702591012": {"revenue": 1_350_000_000, "revenue_year": 2023, "employees": 240},
        "7716657832": {"revenue": 480_000_000, "revenue_year": 2023, "employees": 90},
        "7715513090": {"revenue": 6_800_000_000, "revenue_year": 2023, "employees": 320},
        "7704217628": {"revenue": 42_000_000_000, "revenue_year": 2023, "employees": 580},
        "7743001431": {"revenue": 18_000_000_000, "revenue_year": 2023, "employees": 950},
        "7704534127": {"revenue": 9_500_000_000, "revenue_year": 2023, "employees": 680},
        "7734339570": {"revenue": 7_200_000_000, "revenue_year": 2023, "employees": 520},
        "7708242460": {"revenue": 5_800_000_000, "revenue_year": 2023, "employees": 410},
        "7805247110": {"revenue": 380_000_000, "revenue_year": 2023, "employees": 65},
        "7706608850": {"revenue": 1_850_000_000, "revenue_year": 2023, "employees": 320},
        "7719629980": {"revenue": 2_100_000_000, "revenue_year": 2023, "employees": 380},
        "7702339290": {"revenue": 520_000_000, "revenue_year": 2023, "employees": 95},
        "7716590367": {"revenue": 680_000_000, "revenue_year": 2023, "employees": 125},
        "7730549774": {"revenue": 1_400_000_000, "revenue_year": 2023, "employees": 180},
        "7728326650": {"revenue": 450_000_000, "revenue_year": 2023, "employees": 75},
        "7707577515": {"revenue": 920_000_000, "revenue_year": 2023, "employees": 160},
        "7705845920": {"revenue": 560_000_000, "revenue_year": 2023, "employees": 100},
        "7842317884": {"revenue": 340_000_000, "revenue_year": 2023, "employees": 55},
        "7723863521": {"revenue": 280_000_000, "revenue_year": 2023, "employees": 45},
        "7707212296": {"revenue": 1_750_000_000, "revenue_year": 2023, "employees": 190},
        "7714273519": {"revenue": 620_000_000, "revenue_year": 2023, "employees": 110},
        "7802127954": {"revenue": 2_400_000_000, "revenue_year": 2023, "employees": 350},
        "7710538780": {"revenue": 28_000_000_000, "revenue_year": 2023, "employees": 420},
        "7704251788": {"revenue": 8_900_000_000, "revenue_year": 2023, "employees": 380},
        "7709870717": {"revenue": 11_500_000_000, "revenue_year": 2023, "employees": 520},
    }
    
    # Обогащаем данными о выручке
    for company in seed_companies:
        inn = company.get('inn')
        if inn in revenue_data:
            company.update(revenue_data[inn])
    
    # Очищаем и фильтруем
    cleaned = clean_and_normalize_dataset(seed_companies, config)
    
    # Экспортируем
    output_file = config.get('output_file', 'data/companies.csv')
    export_to_csv(cleaned, output_file)
    
    # Статистика
    stats = generate_summary_stats(cleaned)
    print(f"\n{'=' * 60}")
    print("ГОТОВО!")
    print(f"{'=' * 60}")
    print(f"Результат: {output_file}")
    print(f"Компаний: {len(cleaned)}")
    
    return cleaned


if __name__ == "__main__":
    main()
