# Analysis & Modeling Buffett’s Equity Selection Using 13F Data

## Overview
This project uses Berkshire Hathaway’s 13F filings to learn and model Warren Buffett’s equity selection patterns.
The goal is not to predict short term trades, but to understand what kinds of companies Buffett tends to own and use that learned pattern to identify other stocks with similar characteristics.
The model is trained on historical data where stocks are labeled as:
- Owned by Buffett
- Not owned by Buffett
Using financial, fundamental, and quality related features, the model learns to distinguish between the two.

---
## Data & Setup

Since there is no publicly available dataset that directly captures Warren Buffett’s investment decisions from 13F filings, the dataset used in this project was **created from scratch**.

### 1. Extracting Buffett’s Holdings (13F Data)

- Collected Berkshire Hathaway 13F filings in **XML format**
- Parsed the XML files to:
  - Identify individual stock holdings
  - Extract stock tickers and reporting dates
- Created small intermediate datasets for each filing date
- Combined all filings into a single dataset
- Grouped the data by **reporting date and stock ticker**

This forms the core **Buffett owned stocks dataset**, representing companies actually held by Berkshire over time.

---

### 2. Expanding the Stock Universe

To give the model more context and negative examples:

- Retrieved **S&P 500 stock data** using `yfinance`
- Included all 500 tickers as potential non owned stocks
- Aligned their data with the same reporting dates as the 13F filings

This builds a realistic investment universe similar to what Buffett could select from.

---

### 3. Building the Final Dataset

- Combined:
  - Buffett owned stocks from 13F filings
  - Non owned stocks from the S&P 500 universe
- Framed the task as **binary classification**:
  - `1` → Stock owned by Buffett
  - `0` → Stock not owned by Buffett
- The resulting dataset naturally shows **class imbalance**, reflecting real world investing behavior

---

### 4. Feature Engineering

Using the available financial data:

- Started with standard financial and fundamental features
- Engineered additional **more informative and valuable features**, focusing on:
  - Business quality
  - Capital efficiency
  - Stability
  - Long term value characteristics
- Added these engineered features to the dataset

This step improves the model’s ability to learn Buffett style investment patterns.

---

### 5. Custom Dataset Creation

In summary:

- The entire dataset was **custom built**
- No external labeled dataset was used
- All labels, features, and structure were derived from:
  - 13F filings
  - Market data
  - Feature engineering

This makes the dataset purpose built for modeling **Buffett’s historical investment behavior**.

---

## Model Performance
*Cross Validation (time aware)*

- ROC AUC: 0.97 ± 0.08
- Recall: 0.79 ± 0.21
- F1 Score: 0.80 ± 0.25

This shows strong performance, with some variability across periods, indicating that Buffett’s behavior changes slightly over time.

---

## Test Set Results

Confusion Matrix (Base Model)
- Correctly identified 28 out of 30 Buffett owned stocks
- Only 2 false positives and 2 false negatives
Classification Report
- Precision (Buffett stocks): 0.93
- Recall (Buffett stocks): 0.93
- ROC AUC: 0.998

This indicates excellent separation between Buffett owned and non owned stocks.

---

## Calibration Analysis

Both calibrated and uncalibrated models were evaluated.
- Uncalibrated ROC AUC: 0.998
- Calibrated ROC AUC: 0.948
- Brier score slightly worsened after calibration

---

## What This Model Is and Is Not
This model is good for
- Shortlisting Buffett like stocks
- Ranking companies by similarity to Buffett’s historical picks
- Studying long term investment patterns

This model is not meant for
- Trade timing
- Predicting exact future Berkshire trades
- Short term market decisions
