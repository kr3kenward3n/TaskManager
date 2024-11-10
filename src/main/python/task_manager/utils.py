from datetime import datetime

def parse_date(date_str):
    """Парсит строку даты в объект datetime."""
    return datetime.strptime(date_str, '%Y-%m-%d')

def format_date(date_obj):
    """Форматирует объект datetime в строку."""
    return date_obj.strftime('%Y-%m-%d')