# Car Sales Ads Analysis Dashboard

Web application developed as the Sprint 5 project for TripleTen's Data Science bootcamp, focused on exploratory data analysis of used car listings from the US market.

## Description

This app allows users to visually explore a dataset of used car ads through interactive charts rendered directly in the browser, with no local installation required.

## Features

- **Data viewer**: browse the full dataset with an option to filter out manufacturers with fewer than 1000 listings
- **Vehicle types by manufacturer**: stacked bar chart showing the distribution of vehicle types across manufacturers
- **Condition vs model year histogram**: histogram of vehicle model years broken down by condition
- **Price comparison between manufacturers**: select two manufacturers and compare their price distributions, with an optional histogram normalization toggle

## Tech stack

- Python
- Pandas
- Plotly Express
- Streamlit

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Live app

https://tripleten-sprint5.onrender.com

## Repository

https://github.com/filippoalvim/tripleten-sprint5
