# 📋 Streamlit KanbanJS Component

<div align="center">
    <h3>Komponent Kanban Board dla Streamlit z SortableJS</h3>
    <p>Dowolna liczba pionowych kontenerów w poziomym układzie z drag and drop</p>
    
    ![GitHub](https://img.shields.io/github/license/kubi79/kanbanjs)
    ![GitHub last commit](https://img.shields.io/github/last-commit/kubi79/kanbanjs)
    ![GitHub issues](https://img.shields.io/github/issues/kubi79/kanbanjs)
</div>

## 📋 Spis treści
- [✨ Funkcje](#-funkcje)
- [📦 Instalacja](#-instalacja)
- [🚀 Szybki start](#-szybki-start)
- [📖 Dokumentacja](#-dokumentacja)
  - [Parametry komponentu](#parametry-komponentu)
  - [Struktura danych](#struktura-danych)
  - [Zwracane wartości](#zwracane-wartości)
- [🎨 Przykłady użycia](#-przykłady-użycia)
  - [Podstawowa tablica](#1-podstawowa-tablica)
  - [Tablica z kolorami](#2-tablica-z-kolorami)
  - [Dynamiczna liczba kontenerów](#3-dynamiczna-liczba-kontenerów)
  - [Zapis stanu w session_state](#4-zapis-stanu-w-session_state)
  - [Obsługa wielu tablic](#5-obsługa-wielu-tablic)
  - [Dostosowywanie wyglądu](#6-dostosowywanie-wyglądu-css)
- [🔄 Obsługa zdarzeń](#-obsługa-zdarzeń)
- [❓ Najczęstsze problemy](#-najczęstsze-problemy)
- [🤝 Współpraca](#-współpraca)
- [📄 Licencja](#-licencja)

## ✨ Funkcje

| Funkcja | Opis |
|---------|------|
| **📦 Dowolna liczba kontenerów** | Możesz mieć tyle kolumn ile potrzebujesz (nie tylko 8!) |
| **⬅️ Przewijanie poziome** | Gdy kontenerów jest więcej niż miejsca na ekranie |
| **🔄 Drag & drop między kontenerami** | Przeciągaj zadania między różnymi kolumnami |
| **⬆️ Zmiana kolejności wewnątrz kontenera** | Sortuj zadania w obrębie jednej kolumny |
| **🎨 Konfigurowalne kolory** | Każdy kontener może mieć inny kolor |
| **📤 Pełna komunikacja z Pythonem** | Zwraca informacje o każdej zmianie |
| **📱 Responsywny design** | Dostosowuje się do ekranu |
| **✨ Płynne animacje** | Przyjemne dla oka przejścia |
| **📏 Regulowana szerokość** | Możesz ustawić własną szerokość kontenerów |

## 📦 Instalacja

### Instalacja z GitHub (zalecana)
```bash
pip install git+https://github.com/kubi79/kanbanjs.git

Szybki start
python

import streamlit as st
from streamlit_kanbanjs import kanban_board

# Konfiguracja strony
st.set_page_config(layout="wide")
st.title("Moja Tablica Kanban")

# Przygotowanie danych
kontenery = [
    {
        "header": "DO ZROBIENIA",
        "items": ["Zadanie 1", "Zadanie 2", "Zadanie 3"]
    },
    {
        "header": "W TRAKCIE",
        "items": ["Zadanie 4", "Zadanie 5"]
    },
    {
        "header": "TESTY",
        "items": ["Zadanie 6"]
    },
    {
        "header": "ZROBIONE",
        "items": ["Zadanie 7", "Zadanie 8"]
    }
]

# Uruchomienie komponentu
wynik = kanban_board(kontenery)

# Wyświetlenie wyniku
if wynik:
    st.write("Zmiana:", wynik)

📖 Dokumentacja
Parametry komponentu
python

kanban_board(
    containers: List[Dict],           # Lista kontenerów (wymagane)
    key: Optional[str] = None,         # Unikalny klucz Streamlit
    container_colors: Optional[List[str]] = None,  # Lista kolorów
    width: int = 300                    # Szerokość kontenera w px
)

Parametr	Typ	Wymagany	Domyślnie	Opis
containers	List[Dict]	✅	-	Lista kontenerów z zadaniami
key	str	❌	None	Unikalny klucz dla wielu instancji
container_colors	List[str]	❌	['#f0f2f6'] * n	Kolory dla każdego kontenera
width	int	❌	300	Szerokość pojedynczego kontenera (px)
Struktura danych

Każdy kontener w liście containers musi być słownikiem:
python

{
    "header": "Nazwa kontenera",  # str - nagłówek
    "items": [                     # list - lista zadań
        "Zadanie 1",
        "Zadanie 2",
        "Zadanie 3"
    ]
}

Zwracane wartości

Komponent zwraca None (gdy brak zmian) lub słownik z informacją o zmianie.
Typ 1: Przeniesienie między kontenerami
python

{
    'type': 'move',                    # typ zdarzenia
    'item': 'Zadanie 1.1',              # nazwa zadania
    'from': 'list-0',                   # ID źródłowej listy
    'to': 'list-2',                     # ID docelowej listy
    'oldIndex': 1,                       # stary indeks
    'newIndex': 0,                       # nowy indeks
    'containerFrom': '0',                 # numer źródłowego kontenera
    'containerTo': '2',                   # numer docelowego kontenera
    'key': 'moj_klucz'                    # klucz komponentu (jeśli podany)
}

Typ 2: Zmiana kolejności wewnątrz kontenera
python

{
    'type': 'reorder',                  # typ zdarzenia
    'item': 'Zadanie 3.2',               # nazwa zadania
    'container': 'list-3',               # ID listy
    'oldIndex': 2,                        # stary indeks
    'newIndex': 0,                        # nowy indeks
    'key': 'moj_klucz'                    # klucz komponentu (jeśli podany)
}

🎨 Przykłady użycia
1. Podstawowa tablica
python

import streamlit as st
from streamlit_kanbanjs import kanban_board

# Prosta tablica z 4 kontenerami
kontenery = [
    {"header": "TODO", "items": ["Task 1", "Task 2"]},
    {"header": "DOING", "items": ["Task 3"]},
    {"header": "REVIEW", "items": []},
    {"header": "DONE", "items": ["Task 4", "Task 5"]}
]

wynik = kanban_board(kontenery)

2. Tablica z kolorami
python

# Definiujemy kolory (HEX, RGB, nazwy, gradienty)
kolory = [
    '#ff6b6b',                    # HEX
    'rgb(78, 205, 196)',          # RGB
    'lightblue',                   # nazwa
    'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',  # gradient
    '#96ceb4',
    '#ffeaa7',
    '#dfe6e9',
    '#ffcccc'
]

wynik = kanban_board(
    kontenery, 
    container_colors=kolory,
    width=350  # szersze kontenery
)

3. Dynamiczna liczba kontenerów
python

# Generowanie dowolnej liczby kontenerów
liczba_kontenerow = st.slider("Liczba kontenerów", 3, 20, 8)

kontenery = []
for i in range(liczba_kontenerow):
    kontenery.append({
        "header": f"KOLUMNA {i+1}",
        "items": [f"Zadanie {i+1}.{j}" for j in range(1, 4)]
    })

# Automatyczne generowanie kolorów
kolory = [f'hsl({i * 360/liczba_kontenerow}, 70%, 80%)' for i in range(liczba_kontenerow)]

wynik = kanban_board(kontenery, container_colors=kolory)

4. Zapis stanu w session_state
python

# Inicjalizacja stanu
if 'kontenery' not in st.session_state:
    st.session_state.kontenery = [
        {"header": "Backlog", "items": ["Task 1", "Task 2"]},
        {"header": "Do zrobienia", "items": ["Task 3"]},
        {"header": "Gotowe", "items": ["Task 4", "Task 5"]},
    ]

# Wyświetlenie komponentu
wynik = kanban_board(st.session_state.kontenery, key="main_board")

# Aktualizacja stanu po zmianach
if wynik and wynik.get('type') == 'move':
    from_idx = int(wynik['containerFrom'])
    to_idx = int(wynik['containerTo'])
    item = wynik['item']
    
    # Usuń z źródła
    if item in st.session_state.kontenery[from_idx]['items']:
        st.session_state.kontenery[from_idx]['items'].remove(item)
    
    # Dodaj do celu
    st.session_state.kontenery[to_idx]['items'].insert(
        wynik['newIndex'], item
    )
    st.rerun()

5. Obsługa wielu tablic
python

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tablica Projekt A")
    result_a = kanban_board(kontenery_a, key="projekt_a")

with col2:
    st.subheader("Tablica Projekt B")
    result_b = kanban_board(kontenery_b, key="projekt_b")

# Sprawdzanie wyników z konkretnej tablicy
if result_a and result_a.get('key') == 'projekt_a':
    st.info(f"Zmiana w projekcie A: {result_a['item']}")

6. Dostosowywanie wyglądu (CSS)
python

st.markdown("""
<style>
    /* Szerokość kontenerów */
    .container {
        flex: 0 0 350px !important;
    }
    
    /* Styl nagłówków */
    .container h3 {
        font-size: 18px;
        font-weight: bold;
        text-transform: uppercase;
    }
    
    /* Styl zadań */
    .item {
        background: white;
        border-left: 4px solid #4CAF50;
        border-radius: 4px;
    }
    
    .item:hover {
        background: #f5f5f5;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Kolor paska przewijania */
    #board::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #888, #555);
    }
</style>
""", unsafe_allow_html=True)

wynik = kanban_board(kontenery)

🔄 Obsługa zdarzeń

Kompletny przykład obsługi wszystkich zdarzeń:
python

def handle_kanban_event(event):
    """Funkcja obsługująca zdarzenia z tablicy Kanban"""
    
    if not event:
        return
    
    event_type = event.get('type')
    
    if event_type == 'move':
        from_cont = int(event.get('containerFrom', 0)) + 1
        to_cont = int(event.get('containerTo', 0)) + 1
        item = event.get('item', 'nieznane')
        
        st.success(f"📦 Przeniesiono **{item}** z kontenera {from_cont} do {to_cont}")
        
        # Dodatkowe akcje
        st.balloons()
        
    elif event_type == 'reorder':
        container = int(event.get('container', 'list-0').replace('list-', '')) + 1
        item = event.get('item', 'nieznane')
        
        st.info(f"🔄 Zmieniono kolejność **{item}** w kontenerze {container}")
    
    # Logowanie zdarzenia
    if 'history' not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append(event)

# Użycie
wynik = kanban_board(kontenery, key="logowany_kanban")
handle_kanban_event(wynik)

# Wyświetlenie historii
with st.expander("📋 Historia zmian"):
    st.json(st.session_state.get('history', []))

❓ Najczęstsze problemy
Problem: Kontenery zawijają się do nowej linii

Rozwiązanie: Dodaj CSS wymuszający brak zawijania
python

st.markdown("""
<style>
    #board {
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
    }
</style>
""", unsafe_allow_html=True)

Problem: Drag & drop nie działa

Debugowanie:
python

st.components.v1.html("""
<script>
    console.log('SortableJS:', typeof Sortable);
    console.log('Elementy .item:', document.querySelectorAll('.item').length);
</script>
""", height=0)

Problem: Kolory nie są widoczne

Sprawdź format kolorów:
python

# ✅ Poprawne formaty
kolory = [
    '#ff0000',                    # HEX
    'rgb(255, 0, 0)',              # RGB
    'rgba(255, 0, 0, 0.5)',        # RGBA
    'red',                          # Nazwa
    'hsl(0, 100%, 50%)',            # HSL
    'linear-gradient(45deg, red, blue)'  # Gradient
]

# ❌ Niepoprawne
kolory = [
    'ff0000',     # Brak #
    'rgb(300,0,0)' # Wartość poza zakresem
]

Problem: Za mało miejsca na ekranie

Rozwiązanie: Zmniejsz szerokość kontenerów
python

wynik = kanban_board(kontenery, width=250)  # Węższe kontenery

Problem: Komponent nie aktualizuje się

Rozwiązanie: Użyj key do wymuszenia odświeżenia
python

if 'counter' not in st.session_state:
    st.session_state.counter = 0

wynik = kanban_board(kontenery, key=f"kanban_{st.session_state.counter}")

if wynik:
    st.session_state.counter += 1
    st.rerun()

🤝 Współpraca

Chcesz pomóc w rozwoju? Super! Oto jak możesz to zrobić:

    Fork repozytorium

    Utwórz branch (git checkout -b feature/NowaFunkcja)

    Commit (git commit -m 'Dodaj nową funkcję')

    Push (git push origin feature/NowaFunkcja)

    Otwórz Pull Request

Zgłaszanie problemów

Jeśli znajdziesz błąd, otwórz issue z:

    Opisem problemu

    Krokami do reprodukcji

    Wersją Pythona i Streamlit

    Zrzutem ekranu (jeśli dotyczy)

📄 Licencja

MIT License

Copyright (c) 2024 kubi79

Zezwala się na używanie, kopiowanie, modyfikowanie i dystrybucję tego oprogramowania z zastrzeżeniem zachowania powyższej informacji o prawach autorskich.
<div align="center"> <sub>⭐ Jeśli podoba Ci się ten projekt, daj gwiazdkę na GitHubie! ⭐</sub> <br> <sub>Stworzone z ❤️ dla społeczności Streamlit</sub> </div> ```
Co zawiera ten README:

    Pełną dokumentację wszystkich parametrów

    6 różnych przykładów użycia

    Obsługę zdarzeń z przykładem

    Rozwiązywanie problemów - najczęstsze błędy

    Informacje o licencji i współpracy

    Ładne formatowanie z emoji i tabelami

    Spis treści dla łatwej nawigacji

Teraz Twój projekt na GitHubie ma profesjonalną dokumentację! 
