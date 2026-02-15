import streamlit as st
from streamlit_kanbanjs import kanban_board

# Przygotowanie danych
kontenery = [
    {"header": "DO ZROBIENIA", "items": ["Zadanie 1", "Zadanie 2"]},
    {"header": "W TRAKCIE", "items": ["Zadanie 3", "Zadanie 4"]},
    {"header": "TESTY", "items": ["Zadanie 5"]},
    {"header": "ZROBIONE", "items": ["Zadanie 6", "Zadanie 7"]},
]

# Uruchomienie
wynik = kanban_board(kontenery)

# Obsługa wyników
if wynik:
    st.write("Zmiana:", wynik)
