import streamlit as st
from streamlit_kanbanjs import kanban_board

st.set_page_config(layout="wide")
st.title("Kanban z dowolną liczbą kontenerów")

# Przykład z 12 kontenerami
containers = []
for i in range(1, 13):  # Teraz 12 kontenerów!
    containers.append({
        "header": f"SPRINT {i}",
        "items": [f"Task {chr(65+j)}-{i}" for j in range(3)]
    })

# Generujemy kolory dla każdego kontenera
kolory = [f'hsl({i * 30}, 70%, 80%)' for i in range(len(containers))]

# Użycie komponentu z szerszymi kontenerami
result = kanban_board(
    containers, 
    key="wielki_kanban", 
    container_colors=kolory,
    width=350  # Szersze kontenery
)

if result:
    st.write("Zmiana:", result)
    
    if result.get('type') == 'move':
        st.success(f"Przeniesiono do kontenera {int(result.get('containerTo', 0)) + 1}")
