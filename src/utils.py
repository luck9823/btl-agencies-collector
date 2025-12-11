"""
Вспомогательные функции для сбора данных о BTL-агентствах
"""

import re
import json
import time
from typing import Optional, Dict, List, Any
from pathlib import Path


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Загрузка конфигурации из JSON файла"""
    default_config = {
        "min_revenue": 200_000_000,
        "revenue_year": 2023,
        "output_file": "data/companies.csv",
        "segment_keywords": {
            "BTL": ["btl", "промо", "мерчандайзинг", "brand activation"],
            "EVENT": ["event", "ивент", "мероприятия", "mice"],
            "SOUVENIR": ["сувенир", "промо-материал"],
            "FULL_CYCLE": ["полный цикл", "интегрированные"],
            "COMM_GROUP": ["группа компаний", "холдинг"]
        }
    }
    
    config_file = Path(config_path)
    if config_file.exists():
        with open(config_file, 'r', encoding='utf-8') as f:
            user_config = json.load(f)
            default_config.update(user_config)
    
    return default_config


def normalize_inn(inn: str) -> Optional[str]:
    """Нормализация ИНН"""
    if not inn:
        return None
    inn_clean = re.sub(r'\D', '', str(inn))
    if len(inn_clean) == 10 or len(inn_clean) == 12:
        return inn_clean
    return None


def normalize_revenue(revenue_str: str) -> Optional[int]:
    """Нормализация выручки в рубли"""
    if not revenue_str:
        return None
    
    revenue_str = str(revenue_str).lower().strip()
    if '-' in revenue_str or '–' in revenue_str:
        return None
    
    revenue_str = re.sub(r'[₽руб\.рублей]', '', revenue_str)
    
    multiplier = 1
    if 'млрд' in revenue_str:
        multiplier = 1_000_000_000
        revenue_str = re.sub(r'млрд', '', revenue_str)
    elif 'млн' in revenue_str:
        multiplier = 1_000_000
        revenue_str = re.sub(r'млн', '', revenue_str)
    
    revenue_str = re.sub(r'\s+', '', revenue_str).replace(',', '.')
    
    match = re.search(r'[\d.]+', revenue_str)
    if not match:
        return None
    
    try:
        return int(float(match.group()) * multiplier)
    except ValueError:
        return None


def determine_segment_tags(company_name: str, description: str, okved: str, 
                          rating_category: str, keywords_config: Dict) -> List[str]:
    """Определение segment_tag"""
    tags = set()
    text = ' '.join([company_name or '', description or '', rating_category or '']).lower()
    
    for tag, keywords in keywords_config.items():
        for keyword in keywords:
            if keyword.lower() in text:
                tags.add(tag)
                break
    
    if okved:
        okved_mapping = {'73.11': 'BTL', '73.12': 'BTL', '82.30': 'EVENT', '70.21': 'COMM_GROUP'}
        for code, tag in okved_mapping.items():
            if okved.startswith(code):
                tags.add(tag)
    
    return sorted(list(tags)) if tags else ['BTL']


def clean_company_name(name: str) -> str:
    """Очистка названия компании"""
    if not name:
        return ''
    name = ' '.join(name.split())
    name = re.sub(r'[«»""]', '"', name)
    return name.strip(' .,;:-')


def save_json(data: Any, filepath: str):
    """Сохранение в JSON"""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(filepath: str) -> Any:
    """Загрузка из JSON"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
