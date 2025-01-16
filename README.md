# CryptoLiveData

## Overview

CryptoLiveData is a Python-based application designed to fetch and analyze live cryptocurrency data. It retrieves information for the top 50 cryptocurrencies by market capitalization, providing real-time insights into market trends, price movements, and trading volumes. The data is continuously updated, stored in QuestDB for efficient handling, and visualized using Grafana. 

## Features

- **Live Data Fetching**: Utilizes the CoinMarketCap API to retrieve up-to-date information on the top 50 cryptocurrencies, including:
  - Name
  - Symbol
  - Current Price (USD)
  - Market Capitalization
  - 24-hour Trading Volume
- **Data Storage**: 
  - Leverages QuestDB for high-performance time-series data storage, enabling efficient real-time data handling and querying.
- **Visualization**: 
  - Integrated with Grafana to provide interactive dashboards and visual representations of market trends and price fluctuations.
- **Data Export**: 
  - Automated export of live data to an Excel sheet for offline analysis and reporting.

## Tools and Technologies

- **Programming Language**: Python
- **Data API**: CoinMarketCap API
- **Database**: QuestDB (time-series database)
- **Visualization**: Grafana
- **Additional Libraries**: pandas, openpyxl, requests

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ganeshmahadev/CryptoLiveData.git
   cd CryptoLiveData
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.7 or later installed. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up QuestDB**:
   - Download and run QuestDB ([official website](https://questdb.io/)).
   - Configure the application to connect to the QuestDB instance.

4. **Run the Application**:
   ```bash
   python main.py
   ```

5. **Visualize in Grafana**:
   - Import the pre-configured Grafana dashboards (provided in the repository).
   - Connect Grafana to the QuestDB instance.
