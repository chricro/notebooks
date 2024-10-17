# Natural Gas Price Extrapolation and Analysis

## Project Overview

This project aims to analyze historical natural gas price data and extrapolate future prices to aid in trading natural gas storage contracts. The primary focus is on providing a granular understanding of price movements influenced by seasonal trends and potential future price scenarios.

## Dataset

The dataset consists of monthly snapshots of natural gas prices, covering the period from **October 31, 2020, to September 30, 2024**. Each entry represents the market price of natural gas at the end of the respective month. The data is crucial for pricing natural gas storage contracts, allowing participants in the supply chain to make informed decisions.

## Methodology

1. **Data Collection**: 
   - Monthly natural gas price data is downloaded in CSV format from the existing time series database.

2. **Data Analysis**:
   - The historical price data is analyzed using the SARIMA (Seasonal Autoregressive Integrated Moving Average) model to identify trends and seasonal patterns.
   - The model's parameters are evaluated to ensure they align with the characteristics of the data.

3. **Forecasting**:
   - The SARIMA model is employed to produce price forecasts for both historical dates and an additional year into the future.
   - A function is created that takes a specific date as input and returns an estimated price for natural gas.

## Key Findings

- The SARIMA model's forecasted values align well with historical trends.
- Several factors affect the accuracy of these forecasts:
  - **Model Parameter Appropriateness**: Regular updates and reassessments of model parameters are necessary as new data becomes available.
  - **Exclusion of External Variables**: The current model relies solely on historical price data. Natural gas prices are influenced by various factors, including geopolitical events, regulatory changes, technological advancements, and demand-supply dynamics.
  - **Market Volatility**: The natural gas market is highly volatile, and prices can change abruptly due to unforeseen circumstances.

## Recommendations for Enhanced Forecasting

1. **Data Enrichment**: 
   - Incorporating additional variables, such as economic indicators or weather data, can improve the model's robustness.

2. **Model Exploration**: 
   - For scenarios with more data attributes, consider advanced techniques:
     - **Machine Learning Models**: Regression analysis, support vector machines, and ensemble methods like random forests.
     - **Deep Learning Models**: LSTM networks or RNN variants for sequence prediction.

3. **Regular Model Updates**: 
   - Continuous updates to the model based on new data and market changes will enhance reliability.

## Limitations

- The current dataset may not accurately reflect real-world conditions, as it is primarily designed for academic purposes.
- The low signal-to-noise ratio in price datasets poses challenges in forecasting volatile commodities like natural gas.
- Relying solely on price data is insufficient for robust estimations; external factors must also be considered.

## Conclusion

While the SARIMA model serves as a foundational tool for forecasting natural gas prices, integrating additional data and models will likely yield improved accuracy. Future work should focus on data enrichment and exploring diverse modeling techniques to enhance predictions.

## Usage Instructions

To use the price forecasting function, specify the target date in the required format, and the estimated price will be returned. Ensure that the model is regularly updated with the latest data for optimal performance.

