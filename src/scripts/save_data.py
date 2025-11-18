import csv
import re
import os
from datetime import datetime
from typing import List, Tuple
from .errors import log_success, log_error

# funciones auxiliares 
PHONE_RE = re.compile(r'\+?\d[\d\-\s()]*\d')


def normalize_phone(raw: str) -> str:
    if not raw:
        return ""
    m = PHONE_RE.search(raw)
    if not m:
        return ""
    s = m.group(0)
    s = re.sub(r'[()\-\s]', '', s)
    digits = re.sub(r'\D', '', s)
    #10 digitos agregar prefijo +52
    if len(digits) == 10:
        return '+52' + digits
    if digits.startswith('52') and len(digits) > 10:
        return '+' + digits
    if s.startswith('+'):
        return s
    return '+' + digits


def clean_name(raw: str) -> str:
    if not raw:
        return ""
    name = raw.replace('\u202f', ' ').replace('\xa0', ' ').strip()
    name = re.sub(r'^[~\-\s]+', '', name).strip()
    return name


def _sanitize_filename(name: str) -> str:
    return ''.join(c for c in name if c.isalnum() or c in (' ', '_', '-')).rstrip()


def save_to_csv(data: List[Tuple[str, str]], group_name: str) -> str:
    # guarda lista de participantes en archivo csv en carpeta output
    # retorna ruta del archivo o cadena vacia si falla
    try:
        os.makedirs('output', exist_ok=True)
        safe_group = _sanitize_filename(group_name) if group_name else 'sin_nombre'
        filename = f'{safe_group}.csv'
        filepath = os.path.join('output', filename)

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['#', 'Name', 'Phone Number'])
            for i, (name, phone) in enumerate(data, start=1):
                writer.writerow([i, name, phone or ''])

        log_success(f'Datos guardados en {filepath}')
        return filepath
    except Exception as e:
        log_error(f'Error guardando CSV: {e}')
        return ''
