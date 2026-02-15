import streamlit as st
import streamlit.components.v1 as components
import os
import json

# Pobierz ścieżkę do pliku HTML
parent_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(parent_dir, "frontend", "index.html")

def kanban_board(containers, key=None, container_colors=None):
    """
    Komponent Kanban Board z 8 kontenerami w poziomie
    
    Args:
        containers: Lista słowników z kluczami 'header' i 'items'
        key: Opcjonalny klucz dla komponentu
        container_colors: Opcjonalna lista kolorów dla kontenerów
    
    Returns:
        Dict z informacją o przeniesieniu lub None
    """
    
    # Domyślne kolory jeśli nie podano
    if container_colors is None:
        container_colors = ['#f0f2f6'] * len(containers)
    
    # Wczytaj HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Przygotuj dane do przesłania
    data = {
        'containers': containers,
        'colors': container_colors
    }
    
    # Wstaw dane do HTML
    html_content = html_content.replace('/* CONTAINERS_DATA */', json.dumps(data, ensure_ascii=False))
    
    # Wyświetl komponent
    result = components.html(
        html_content,
        height=800,
        scrolling=False,
        key=key
    )
    
    return result
