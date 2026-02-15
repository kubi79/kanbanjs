import streamlit as st
from streamlit_kanbanjs import kanban_board

st.set_page_config(layout="wide")
st.title("8 Pionowych Kontenerów - Przykład")

# Przygotowanie danych
containers = []
for i in range(1, 9):
    containers.append({
        "header": f"KONTENER {i}",
        "items": [f"Zadanie {i}.1", f"Zadanie {i}.2", f"Zadanie {i}.3"]
    })

# Definiujemy kolory dla kontenerów
kolory = [
    '#ff9999',  # czerwony
    '#99ff99',  # zielony
    '#9999ff',  # niebieski
    '#ffff99',  # żółty
    '#ff99ff',  # różowy
    '#99ffff',  # cyjan
    '#ffb366',  # pomarańczowy
    '#c299ff'   # fioletowy
]

# Użycie komponentu z kolorami
result = kanban_board(containers, key="kanban1", container_colors=kolory)

# Wyświetlenie wyniku - POPRAWIONE
if result is not None and isinstance(result, dict):
    st.write("Zmiana:", result)
    
    # Sprawdzanie typu bez używania .get()
    if 'type' in result:
        if result['type'] == 'move':
            container_from = int(result.get('containerFrom', '0')) + 1
            container_to = int(result.get('containerTo', '0')) + 1
            st.success(f"Przeniesiono {result.get('item', '')} z kontenera {container_from} do {container_to}")
        elif result['type'] == 'reorder':
            container = int(result.get('container', 'list-0').replace('list-','')) + 1
            st.info(f"Zmieniono kolejność w kontenerze {container}")
elif result is not None:
    st.write("Ostatnia zmiana:", result)
