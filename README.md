# Age and Soccer Player Performance

A data science project exploring how player age relates to on-pitch performance across Europe's top five soccer leagues (Premier League, La Liga, Serie A, Bundesliga, and Ligue 1) during the 2025–2026 season.

## Research Question
*How does age affect soccer player performance during the 2025–2026 season?*

Specifically, we evaluate goal contributions per 90 minutes ($\frac{\text{Goals} + \text{Assists}}{\text{90s}}$), investigating whether an athlete's offensive production exhibits an age peak and how tactical position influences the apparent age curve.

## Dataset
* **Source:** [Football Players Statistics (2025–2026)](https://www.kaggle.com/datasets/hubertsidorowicz/football-players-stats-2025-2026) by Hubert Sidorowicz on Kaggle (compiled from FBref).
* **Location:** `data/players_data_light-2025_2026.csv`
* **Observations:** 2,839 total player records across Europe's top five domestic competitions.

## Website Structure
Built with [Quarto](https://quarto.org/):
* **Home (`index.qmd`):** Project overview and a scatterplot with LOESS smoothing of 2,783 observations analyzing the broad relationship between age and goal contributions per 90.
* **Explore the Data (`explore.qmd`):** Interactive visualization powered by Plotly and Crosstalk, allowing client-side filtering by league and position with rich hover tooltips.
* **Age and Performance (`story.qmd`):** Evidence-based analysis of 1,999 players with $\ge 450$ minutes, revealing positional differences and explaining why overall age trends are heavily shaped by positional composition.

## How to Render
To build the website locally:
```bash
quarto render
```
The compiled static website is generated in the `docs/` directory for deployment on GitHub Pages.
