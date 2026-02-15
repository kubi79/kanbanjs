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

# Wyświetlenie wyniku
if result:
    st.write("Zmiana:", result)
    
    if result.get('type') == 'move':
        st.success(f"Przeniesiono {result['item']} z kontenera {int(result['containerFrom'])+1} do {int(result['containerTo'])+1}")
    elif result.get('type') == 'reorder':
        st.info(f"Zmieniono kolejność w kontenerze {int(result['container'].replace('list-',''))+1}")

st.write("Ostatnia zmiana:", result)
