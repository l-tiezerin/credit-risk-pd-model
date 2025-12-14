# Credit Risk – Probability of Default (PD) Model

## Project Status

**Work in progress**. This project is actively being developed and refined. The current version focuses on data ingestion, environment setup, and initial exploration. Modeling and evaluation steps will be added incrementally.

---

## Overview

This repository contains a personal data science project focused on building a **Probability of Default (PD)** model using a public credit dataset from the UCI Machine Learning Repository.

The goal of the project is to simulate, in a simplified and transparent way, how credit risk models are developed in financial institutions, with emphasis on:

* data preparation and feature understanding,
* statistical modeling for credit risk,
* reproducibility and professional project structure.

Although simplified, the project is inspired by real-world credit risk practices commonly used in banks and credit cooperatives.

---

## Objectives

* Load and prepare a real-world credit dataset
* Build a baseline Probability of Default (PD) model
* Perform exploratory data analysis focused on credit risk
* Evaluate model performance using standard risk metrics
* Document assumptions, limitations, and results clearly

---

## Dataset

The dataset used is:

**Default of Credit Card Clients Dataset**
UCI Machine Learning Repository

It contains information about credit card clients, including demographic variables, credit limits, payment history, billed amounts, and payment amounts, along with a binary target indicating default in the following month.

The raw dataset is loaded programmatically using the `ucimlrepo` library and stored locally for reproducibility.

---

## Project Structure

```
credit-risk-pd-model/
│
├── data/
│   ├── raw/                # Raw dataset (as obtained from source)
│   └── processed/          # Cleaned and feature-engineered data
│
├── notebooks/
│   └── 01_exploratory_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   └── data_ingestion.py   # Dataset loading logic
│
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## Environment and Dependencies

This project uses **uv** for dependency and environment management.

### Requirements

* Python >= 3.13, < 3.14
* uv

### Setup

```bash
uv sync
```

For notebook usage, a Jupyter kernel can be registered with:

```bash
uv run python -m ipykernel install --user --name credit-risk-pd-model
```

---

## Current Progress

* Project structure defined
* Environment configured with uv
* Dataset ingestion implemented
* Initial notebook created

---

## Next Steps

* Create a data dictionary and rename features for clarity
* Perform exploratory data analysis (EDA)
* Implement baseline PD model (logistic regression)
* Evaluate model performance (AUC, confusion matrix)
* Add documentation and modeling assumptions

---

## Disclaimer

This project is for **educational and portfolio purposes only**. It does not represent a production-ready credit risk model and should not be used for real credit decision-making.