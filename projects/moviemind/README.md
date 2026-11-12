# MovieMind

MovieMind is a Python desktop prototype that recommends films using similarities between rating patterns. Click **Refresh recommendations** to draw another selection for the synthetic demo profile. The recommendation list uses fictional movie titles and built-in sample ratings.

## Run the demo

From this directory, with Python 3.11 or later, run these commands in a virtual environment.

```sh
python -m pip install -r requirements.txt
python Main.py
```

The launcher creates a temporary SQLite database from the sample data and removes it when the app closes normally. The demo runs offline with no account setup.

## Source map

| Path | Purpose |
| --- | --- |
| [`Main.py`](Main.py) | Opens the PySide6 window and manages the temporary database directory. |
| [`UI/ui_mainwindow.py`](UI/ui_mainwindow.py) | Displays and refreshes the recommendation cards. |
| [`BackEnd/Initial_System.py`](BackEnd/Initial_System.py) | Seeds fictional movies, demo profiles and sample ratings. |
| [`BackEnd/System.py`](BackEnd/System.py) and [`BackEnd/Recommendation_system.py`](BackEnd/Recommendation_system.py) | Connect the data layer to the NumPy rating and cosine-similarity logic. |
| [`Dataset/MovieMindProDB.py`](Dataset/MovieMindProDB.py) | Defines SQLite tables and operations for users, movies, preferences and personal movie links. |

This portfolio version adapts the core app from [MovieMind, revision `7203ce8`](https://github.com/mtbasktm/MovieMind/tree/7203ce823c01beb4fb623bceb4b1f20e0dee4f8f) for an offline demo. See the [project case study](../moviemind.md) for my SQLite work and the relevant original commits.
