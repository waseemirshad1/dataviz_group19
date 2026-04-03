# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A data visualization course project analyzing ecological/agricultural research data on coffee production and plant biodiversity across 60 sites. The goal is to create meaningful visualizations from multi-dimensional datasets.

## Data

All raw data is in `data/`. No extraction needed — files are ready to use.

| File | Format | Contents |
|------|--------|----------|
| `Coffee_yield.xlsx` | Excel | 3-year average clean coffee yield per site |
| `Coffee_structure_index_variables.xlsx` | Excel | 5 variables on 16 coffee shrubs per site + cluster assignments |
| `Environmental_and_management_variables.xlsx` | Excel | Site-level coffee structure index, density, dominance |
| `Plant_species_richness.xlsx` | Excel | Species richness per plant group and total, for 60 sites |
| `Plant_species_and_average_coffee_yield_in_sites_where_the_species_occurs.xlsx` | Excel | Per-species: site count + average coffee yield |
| `Total_species_composition.xlsx` | Excel | Combined presence/absence species-by-site matrices |
| `Woody_species_abundance.xlsx` | Excel | Woody species abundance matrices |
| `Herbaceous_vegetation_Abundance.txt` | TSV | Herbaceous plant group abundance by site |
| `Bryophyte_frequency.txt` | TSV | Bryophyte frequency of occurrence by site |

## Research Directories

The `research/` subdirectories are the working space:

- `summaries/` — data summaries and notes
- `data_visualisations/` — output visualizations
- `ideas_creative_combined_visualisations/` — design explorations
- `cv/` — curriculum vitae (unrelated to the data project)

## Course Materials

- `course/Data Visualization + assignment.pdf` — assignment brief and requirements
- `course/project_scoresheet_designs.pdf` — grading rubric for visualization designs
- `course/report of assigment template.pdf` — report template
- `course/example_reports/` — sample reports for reference
- `books/Visualization Analysis and Design (AK Peters Visualization Series).pdf` — primary reference textbook (Tamara Munzner)
