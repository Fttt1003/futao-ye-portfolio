# MovieMind — Movie Recommendation Desktop App

**Python · SQLite · PySide6 · NumPy**

MovieMind is a desktop prototype for personalised movie recommendations. The PySide6 interface connects to a Python backend, with SQLite for persistence and a NumPy module that estimates scores from movie-to-movie cosine similarity.

**[Browse the source code and run the demo](moviemind/)**

## My contribution

- Updated the SQLite schema and queries for user-added movie links. Each entry gained a personal movie ID, and a lookup by user and movie name could return the ID needed to retrieve the corresponding link.
- Updated the query for listing user-added movie links, added link removal, and adjusted user ID assignment so the first account starts at ID 1.

## Source and contribution history

- [Original MovieMind repository](https://github.com/mtbasktm/MovieMind)
- [Personal movie IDs and link lookup](https://github.com/mtbasktm/MovieMind/commit/cc56ddae0106c11b32d76359e537dd2f2d9bcbd1)
- [Listing and removing user-added movie links](https://github.com/mtbasktm/MovieMind/commit/d1028df1095c94bbcc5f16b0aabfb8f0eaf2b18b)
- [User ID assignment](https://github.com/mtbasktm/MovieMind/commit/1ec33116eebce1d3cd7b43f43744ea4c3f32c992)
- [All my MovieMind commits](https://github.com/mtbasktm/MovieMind/commits/main/?author=Fttt1003)

The portfolio version uses fictional film titles and ratings. On launch, it creates a fresh SQLite database in a temporary directory and shows recommendations for a demo profile. The original commits above document my contributions to the upstream project.
