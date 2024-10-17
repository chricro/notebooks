# JPMorgan Forage Program: Quantitative Research Task Instructions

## Overview of JPMorgan Forage

JPMorgan Forage is a virtual program that offers participants an opportunity to engage in real-world tasks that quantitative researchers perform throughout their careers. This program provides insights into quantitative analysis, data modeling, and forecasting techniques critical in the finance and commodity trading sectors.



## Task Instructions

### Task Description

You are a quantitative researcher working with a commodity trading desk. Alex, a VP on the desk, wants to start trading natural gas storage contracts. However, the available market data must be of higher quality to enable the instrument to be priced accurately. They have sent you an email asking you to help extrapolate the data available from external feeds to provide more granularity, considering seasonal trends in the price as it relates to months in the year. To price the contract, we will need historical data and an estimate of the future gas price at any date.

Commodity storage contracts represent deals between warehouse (storage) owners and participants in the supply chain (refineries, transporters, distributors, etc.). The deal is typically an agreement to store an agreed quantity of any physical commodity (oil, natural gas, agriculture) in a warehouse for a specified amount of time. The key terms of such contracts (e.g., periodic fees for storage, limits on withdrawals/injections of a commodity) are agreed upon at the inception of the contract between the warehouse owner and the client. The injection date is when the commodity is purchased and stored, and the withdrawal date is when the commodity is withdrawn from storage and sold.

A client could be anyone who would fall within the commodities supply chain, such as producers, refiners, transporters, and distributors. This group would also include firms (commodities trading, hedge funds, etc.) whose primary aim is to take advantage of seasonal or intra-day price differentials in physical commodities. For example, if a firm is looking to buy physical natural gas during summer and sell it in winter, it would take advantage of the seasonal price differential mentioned above. The firm would need to leverage the services of an underground storage facility to store the purchased inventory to realize any profits from this strategy. After asking around for the source of the existing data, you learn that the current process is to take a monthly snapshot of prices from a market data provider, which represents the market price of natural gas delivered at the end of each calendar month. This data is available for roughly the next 18 months and is combined with historical prices in a time series database. After gaining access, you are able to download the data in a CSV file.

You should use this monthly snapshot to produce a varying picture of the existing price data, as well as an extrapolation for an extra year, in case the client needs an indicative price for a longer-term storage contract.

Download the monthly natural gas price data. Each point in the data set corresponds to the purchase price of natural gas at the end of a month, from **October 31, 2020, to September 30, 2024**. Analyze the data to estimate the purchase price of gas at any date in the past and extrapolate it for one year into the future. Your code should take a date as input and return a price estimate.

### My Approach

To address the task, I chose to implement the SARIMA (Seasonal Autoregressive Integrated Moving Average) model for the following reasons:

1. **Seasonal Trends**: The SARIMA model is particularly effective for time series data with seasonal components, making it suitable for analyzing natural gas prices that typically exhibit seasonal fluctuations.

2. **Historical Data Utilization**: By leveraging historical monthly price data, the SARIMA model can identify underlying trends and patterns that can inform future price estimates.

3. **Forecasting Capability**: The model enables the estimation of natural gas prices for any date in the past as well as for future projections, which aligns with the task requirements for both historical and future price analysis.

4. **Granularity and Precision**: Implementing this model allows for more granular insights into price behavior, which is crucial for accurate pricing of natural gas storage contracts.

### Results

The forecasted values from the SARIMA model appear to align well with the historical data trends. Nevertheless, several factors should be considered to enhance forecast reliability:

1. **Model Parameter Dependency**: The accuracy of these forecasts is highly dependent on the appropriateness of the model parameters to the data characteristics, necessitating regular reassessments and updates as new data become available.

2. **External Influences**: The model currently relies solely on historical price data. However, natural gas prices are influenced by various factors, including geopolitical events, regulatory changes, technological progress, and shifts in demand and supply, which are not accounted for in this model. This exclusion could potentially diminish the forecast's accuracy.

3. **Market Volatility**: The natural gas market is notoriously volatile, with prices susceptible to abrupt changes due to unforeseen market dynamics, which may not be adequately predicted by a model based solely on historical data.

4. **Alternative Approaches**: While the SARIMA model serves as a robust baseline for forecasting, enhancing it with updated data, considering a combination of models, or integrating external variables would likely improve its accuracy and robustness.

5. **Advanced Modeling Considerations**: Given the dataset currently only includes time-series data on natural gas prices, using advanced machine learning or deep learning models might not fully capture the complexity or add significant value beyond simpler models due to the limited feature set. Simple models, such as linear regression or bi-regression with sinusoidal components, might be more appropriate in this context.

6. **Exploration of Other Models**: For more intricate scenarios where additional data attributes are available, other models could be explored, including:
   - **Machine Learning Models**: Techniques like regression analysis, support vector machines, or ensemble methods (e.g., random forests and gradient boosting machines) could be beneficial. These models can incorporate auxiliary variables (like economic indicators or weather conditions) that influence natural gas prices.
   - **Deep Learning Models**: LSTM networks or other RNN variants are well-suited for sequence prediction tasks and can model the complex nonlinear relationships often present in comprehensive datasets.

7. **Dataset Limitations**: Furthermore, after verifying that the provided dataset of natural gas prices did not accurately reflect reality, I have concluded that the dataset is unrealistic and designed for academic purposes. In practice, the signal-to-noise ratio in such datasets is very low, making it challenging to forecast the price of a volatile commodity like natural gas. Additionally, relying solely on price data is insufficient for making robust estimations.
