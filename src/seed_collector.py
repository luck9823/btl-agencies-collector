"""
Модуль для сбора seed-списка BTL/Event агентств
"""

from typing import List, Dict, Any


def get_manual_seed_list() -> List[Dict[str, Any]]:
    """Ручной seed-список известных BTL/Event агентств с ИНН"""
    return [
        {"name": "EMG", "inn": "7714633498", "segment_tag": "BTL,FULL_CYCLE", "source": "manual_seed", "rating_ref": "РРАР-2024 BTL", "description": "Крупнейшее российское агентство интегрированных маркетинговых коммуникаций"},
        {"name": "ООО ОПЕН", "inn": "7709409498", "segment_tag": "BTL,FULL_CYCLE", "source": "manual_seed", "rating_ref": "РРАР-2024 BTL", "description": "Агентство маркетинговых коммуникаций, мерчандайзинг"},
        {"name": "REMAR Group", "inn": "7841312709", "segment_tag": "BTL,EVENT,SOUVENIR", "source": "manual_seed", "rating_ref": "РРАР-2024 BTL", "description": "Организация мероприятий, промо-акции, MICE"},
        {"name": "АДВ Груп", "inn": "7717618596", "segment_tag": "COMM_GROUP,FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex 2024", "description": "Коммуникационная группа полного цикла"},
        {"name": "Игроник", "inn": "7743784003", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex 2024", "description": "Коммуникационная группа"},
        {"name": "ГК Родная речь", "inn": "7716688799", "segment_tag": "COMM_GROUP,FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex 2024", "description": "Коммуникационная группа"},
        {"name": "Оккам", "inn": "7702820073", "segment_tag": "COMM_GROUP,FULL_CYCLE", "source": "manual_seed", "rating_ref": "АКАР DNMR 2024", "description": "Коммуникационная группа, digital и маркетинговые услуги"},
        {"name": "Mosaic", "inn": "7709851877", "segment_tag": "FULL_CYCLE", "source": "manual_seed", "rating_ref": "АКАР DNMR 2024", "description": "Агентство интегрированных коммуникаций"},
        {"name": "Media Instinct", "inn": "7708578030", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex Обороты 2024", "description": "Медиабаинговое агентство"},
        {"name": "Group4Media", "inn": "7710419487", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex Обороты 2024", "description": "Медийная группа"},
        {"name": "Подъёжики", "inn": "7704248543", "segment_tag": "EVENT", "source": "manual_seed", "rating_ref": "AdIndex Event 2024", "description": "Event-агентство"},
        {"name": "Eventum Premo", "inn": "7718576908", "segment_tag": "EVENT,FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex Event 2024", "description": "Event-агентство полного цикла"},
        {"name": "MaxiMarkt", "inn": "7705686940", "segment_tag": "BTL", "source": "manual_seed", "rating_ref": "РАМУ BTL 2024", "description": "BTL-агентство, мерчандайзинг, промо"},
        {"name": "Action", "inn": "7715553001", "segment_tag": "BTL,EVENT", "source": "manual_seed", "rating_ref": "РАМУ BTL 2024", "description": "BTL-агентство, event-маркетинг"},
        {"name": "TMA-Draft", "inn": "7728300401", "segment_tag": "BTL", "source": "manual_seed", "rating_ref": "РАМУ BTL 2024", "description": "BTL и трейд-маркетинг"},
        {"name": "АМАДЕО Принт", "inn": "7722346159", "segment_tag": "SOUVENIR", "source": "manual_seed", "rating_ref": "РРАР Сувениры", "description": "Производство сувенирной продукции"},
        {"name": "Oasis Rus", "inn": "7728573261", "segment_tag": "SOUVENIR", "source": "manual_seed", "rating_ref": "РРАР Сувениры", "description": "Дистрибуция сувенирной продукции"},
        {"name": "КРОС", "inn": "7703196416", "segment_tag": "COMM_GROUP,FULL_CYCLE", "source": "manual_seed", "rating_ref": "РРАР PR", "description": "Коммуникационная группа, PR"},
        {"name": "Fleishman Hillard Vanguard", "inn": "7704267567", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "РРАР PR", "description": "Международное коммуникационное агентство"},
        {"name": "SPN Communications", "inn": "7838028766", "segment_tag": "COMM_GROUP,EVENT", "source": "manual_seed", "rating_ref": "РРАР PR", "description": "Коммуникационное агентство"},
        {"name": "Progression", "inn": "7708655870", "segment_tag": "BTL,FULL_CYCLE", "source": "manual_seed", "rating_ref": "РАМУ BTL", "description": "BTL-агентство полного цикла"},
        {"name": "Ace Target", "inn": "7702591012", "segment_tag": "BTL", "source": "manual_seed", "rating_ref": "РАМУ BTL", "description": "Агентство торгового маркетинга"},
        {"name": "Boost Team", "inn": "7716657832", "segment_tag": "BTL,EVENT", "source": "manual_seed", "rating_ref": "РАМУ BTL", "description": "BTL и event-маркетинг"},
        {"name": "Initiative", "inn": "7715513090", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex", "description": "Медийное агентство"},
        {"name": "OMD OM Group", "inn": "7704217628", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex Обороты 2024", "description": "Медийная группа"},
        {"name": "Dentsu Russia", "inn": "7743001431", "segment_tag": "COMM_GROUP,FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex", "description": "Международная коммуникационная группа"},
        {"name": "МГКом", "inn": "7704534127", "segment_tag": "FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex Digital 2024", "description": "Digital-агентство полного цикла"},
        {"name": "E-Promo", "inn": "7734339570", "segment_tag": "FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex Digital 2024", "description": "Performance-маркетинг"},
        {"name": "Realweb", "inn": "7708242460", "segment_tag": "FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex", "description": "Digital-агентство"},
        {"name": "SFM", "inn": "7706608850", "segment_tag": "BTL", "source": "manual_seed", "rating_ref": "РАМУ Мерчандайзинг", "description": "Агентство мерчандайзинга"},
        {"name": "Leader Team", "inn": "7719629980", "segment_tag": "BTL", "source": "manual_seed", "rating_ref": "РАМУ BTL", "description": "BTL и мерчандайзинг"},
        {"name": "Моссовет", "inn": "7702339290", "segment_tag": "EVENT", "source": "manual_seed", "rating_ref": "AdIndex Event", "description": "Event-агентство"},
        {"name": "Клеверенс", "inn": "7716590367", "segment_tag": "EVENT,FULL_CYCLE", "source": "manual_seed", "rating_ref": "AdIndex Event", "description": "Event и интегрированные коммуникации"},
        {"name": "Upjet Travel", "inn": "7730549774", "segment_tag": "EVENT", "source": "manual_seed", "rating_ref": "AdIndex MICE", "description": "MICE и бизнес-туризм"},
        {"name": "Конференция", "inn": "7728326650", "segment_tag": "EVENT", "source": "manual_seed", "rating_ref": "AdIndex Event", "description": "Организация конференций"},
        {"name": "Field Force", "inn": "7707577515", "segment_tag": "BTL", "source": "manual_seed", "rating_ref": "РАМУ BTL", "description": "Мерчандайзинг и полевой маркетинг"},
        {"name": "Глобус", "inn": "7705845920", "segment_tag": "BTL,EVENT", "source": "manual_seed", "rating_ref": "РАМУ BTL", "description": "BTL и event"},
        {"name": "Ривелти групп", "inn": "7842317884", "segment_tag": "BTL,SOUVENIR", "source": "manual_seed", "rating_ref": "РАМУ", "description": "BTL и промо-продукция"},
        {"name": "PRonline", "inn": "7723863521", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "РРАР PR", "description": "Digital PR агентство"},
        {"name": "Михайлов и Партнеры", "inn": "7707212296", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "РРАР PR", "description": "Стратегические коммуникации"},
        {"name": "CLIPPER", "inn": "7714273519", "segment_tag": "SOUVENIR", "source": "manual_seed", "rating_ref": "РРАР Сувениры", "description": "Сувенирная продукция"},
        {"name": "Проект 111", "inn": "7802127954", "segment_tag": "SOUVENIR", "source": "manual_seed", "rating_ref": "РРАР Сувениры", "description": "Сувенирная и промо-продукция"},
        {"name": "ОМД Медиа Дирекшн", "inn": "7710538780", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex", "description": "Медийная группа"},
        {"name": "Starlink", "inn": "7704251788", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex", "description": "Медийное агентство"},
        {"name": "NMi Group", "inn": "7709870717", "segment_tag": "COMM_GROUP", "source": "manual_seed", "rating_ref": "AdIndex", "description": "Медийная группа"},
        {"name": "Артика СПб", "inn": "7805247110", "segment_tag": "BTL,EVENT", "source": "manual_seed", "rating_ref": "РАМУ региональный", "description": "BTL и event в Санкт-Петербурге"},
    ]


def collect_seed_list() -> List[Dict[str, Any]]:
    """Сбор полного seed-списка"""
    companies = get_manual_seed_list()
    print(f"[*] Загружено {len(companies)} компаний из seed-списка")
    return companies
