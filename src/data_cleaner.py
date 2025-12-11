"""
Модуль для очистки и нормализации данных
"""

import pandas as pd
from typing import List, Dict, Any
import re
from utils import normalize_inn, clean_company_name, determine_segment_tags, load_config


def deduplicate_by_inn(companies: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Дедупликация по ИНН"""
    seen = {}
    for c in companies:
        inn = normalize_inn(c.get('inn', ''))
        if inn and inn not in seen:
            seen[inn] = c
    return list(seen.values())


def filter_by_revenue(companies: List[Dict[str, Any]], min_revenue: int = 200_000_000) -> List[Dict[str, Any]]:
    """Фильтрация по выручке"""
    filtered = []
    no_revenue = []
    below = []
    
    for c in companies:
        rev = c.get('revenue')
        if rev is None:
            no_revenue.append(c)
        elif rev >= min_revenue:
            filtered.append(c)
        else:
            below.append(c)
    
    print(f"\n[*] Результаты фильтрации по выручке >= {min_revenue/1_000_000:.0f} млн ₽:")
    print(f"    - Прошли фильтр: {len(filtered)}")
    print(f"    - Ниже порога: {len(below)}")
    print(f"    - Без данных о выручке: {len(no_revenue)}")
    
    return filtered


def normalize_company_data(company: Dict[str, Any], config: Dict) -> Dict[str, Any]:
    """Нормализация данных компании"""
    return {
        'inn': normalize_inn(company.get('inn', '')),
        'name': clean_company_name(company.get('name', '')),
        'revenue': company.get('revenue'),
        'revenue_year': company.get('revenue_year'),
        'segment_tag': company.get('segment_tag', 'BTL'),
        'source': company.get('source', 'unknown'),
        'okved_main': company.get('okved_main'),
        'employees': company.get('employees'),
        'site': company.get('site'),
        'description': company.get('description'),
        'region': company.get('region'),
        'contacts': company.get('contacts'),
        'rating_ref': company.get('rating_ref'),
    }


def clean_and_normalize_dataset(companies: List[Dict[str, Any]], config: Dict = None) -> List[Dict[str, Any]]:
    """Полная очистка датасета"""
    if config is None:
        config = load_config()
    
    print(f"[*] Начало очистки данных. Исходных записей: {len(companies)}")
    
    # Нормализация
    print("[*] Нормализация данных...")
    normalized = [normalize_company_data(c, config) for c in companies]
    
    # Удаление пустых
    normalized = [c for c in normalized if c.get('inn') and c.get('name')]
    print(f"    После удаления пустых: {len(normalized)}")
    
    # Дедупликация
    print("[*] Дедупликация по ИНН...")
    deduplicated = deduplicate_by_inn(normalized)
    print(f"    После дедупликации: {len(deduplicated)}")
    
    # Фильтрация по выручке
    min_revenue = config.get('min_revenue', 200_000_000)
    filtered = filter_by_revenue(deduplicated, min_revenue)
    
    # Сортировка по выручке
    filtered.sort(key=lambda x: x.get('revenue') or 0, reverse=True)
    
    return filtered


def export_to_csv(companies: List[Dict[str, Any]], output_file: str = "data/companies.csv"):
    """Экспорт в CSV"""
    columns = ['inn', 'name', 'revenue_year', 'revenue', 'segment_tag', 'source',
               'okved_main', 'employees', 'site', 'description', 'region', 'contacts', 'rating_ref']
    
    df = pd.DataFrame(companies)
    for col in columns:
        if col not in df.columns:
            df[col] = None
    
    df = df[columns]
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"\n[*] Данные сохранены в {output_file}")
    print(f"    Всего записей: {len(df)}")
    
    print("\n[*] Распределение по сегментам:")
    for tag in ['BTL', 'EVENT', 'SOUVENIR', 'FULL_CYCLE', 'COMM_GROUP']:
        count = df['segment_tag'].str.contains(tag, na=False).sum()
        print(f"    - {tag}: {count}")


def generate_summary_stats(companies: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Статистика по датасету"""
    df = pd.DataFrame(companies)
    
    stats = {
        "total_companies": len(df),
        "with_revenue": df['revenue'].notna().sum(),
        "by_segment": {},
    }
    
    if df['revenue'].notna().any():
        stats["revenue_stats"] = {
            "min": df['revenue'].min(),
            "max": df['revenue'].max(),
            "mean": df['revenue'].mean(),
            "median": df['revenue'].median(),
        }
    
    for tag in ['BTL', 'EVENT', 'SOUVENIR', 'FULL_CYCLE', 'COMM_GROUP']:
        mask = df['segment_tag'].str.contains(tag, na=False)
        stats["by_segment"][tag] = {"count": mask.sum()}
    
    return stats
