import streamlit as st
import streamlit.components.v1 as components
import os
import json

# Pobierz ścieżkę do pliku HTML
parent_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(parent_dir, "frontend", "index.html")

def kanban_board(containers, key=None, container_colors=None, width=300):
    """
    Komponent Kanban Board z dowolną liczbą kontenerów w poziomie
    
    Args:
        containers: Lista słowników z kluczami 'header' i 'items'
        key: Opcjonalny klucz dla komponentu
        container_colors: Opcjonalna lista kolorów dla kontenerów
        width: Szerokość pojedynczego kontenera w pikselach (domyślnie 300)
    
    Returns:
        Dict z informacją o przeniesieniu lub None
    """
    
    # Domyślne kolory jeśli nie podano
    if container_colors is None:
        container_colors = ['#f0f2f6'] * len(containers)
    
    # Sprawdź czy liczba kolorów zgadza się z liczbą kontenerów
    if len(container_colors) != len(containers):
        container_colors = ['#f0f2f6'] * len(containers)
        st.warning("Liczba kolorów nie zgadza się z liczbą kontenerów. Użyto domyślnych kolorów.")
    
    # Wczytaj HTML
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        st.error(f"Nie znaleziono pliku HTML: {html_path}")
        return None
    
    # Przygotuj dane do przesłania
    data = {
        'containers': containers,
        'colors': container_colors,
        'component_key': key,
        'container_width': width  # Dodajemy szerokość kontenera
    }
    
    # Wstaw dane do HTML
    html_content = html_content.replace('/* CONTAINERS_DATA */', json.dumps(data, ensure_ascii=False))
    
    # Dynamiczna wysokość w zależności od liczby kontenerów
    height = max(600, len(containers) * 100)  # Minimum 600px
    
    # Wyświetl komponent
    result = components.html(
        html_content,
        height=height + 200,  # Dodajemy miejsce na pasek przewijania
        scrolling=False
    )
    
    return result
