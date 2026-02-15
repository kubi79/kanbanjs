from setuptools import setup, find_packages

setup(
    name="streamlit-kanbanjs",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'streamlit_kanbanjs': ['frontend/*.html'],
    },
    install_requires=["streamlit"],
    author="Twój Nick",
    description="Komponent Kanban Board dla Streamlit z SortableJS",
    long_description="8 pionowych kontenerów z drag and drop między nimi, zmianą kolejności wewnątrz kontenera i kolorami",
    url="https://github.com/twojlogin/streamlit-kanbanjs",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
