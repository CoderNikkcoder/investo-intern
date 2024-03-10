# Simple Moving Average (SMA) Crossover Strategy Implementation

This project implements a Simple Moving Average (SMA) crossover strategy to generate trading signals based on historical stock data.


Steps

    Data Cleaning and Database Insertion:
        Reads data from Data.xlsx using pandas
        Connects to the MySQL database
        Inserts data into the HINDALCO_DATA table

    Data Retrieval and Preparation:
        Retrieves data from the HINDALCO_DATA table
        Sorts data chronologically
        Resets the index

    SMA Calculation:
        Defines a function SMA to calculate simple moving averages for a given period
        Calculates 50-day and 200-day SMAs

    Signal Generation:
        Creates a Signal column indicating a buy signal (1) when SMA50 > SMA200, otherwise a sell signal (0)
        Calculates a Position column to capture changes in signals (buy/sell)
        Determines buy and sell prices based on close price when the position changes

    Visualization:
        Plots closing price, SMA50, and SMA200 lines
        Indicates buy and sell signals with markers

Usage

    ```pip install -r requirements.txt``` 

#Testing

Test data file for valid data types:

      python3 -m unittest

Result:
![SMA_output](https://github.com/CoderNikkcoder/investo-intern/assets/159905764/46b140c8-123e-47f1-956b-0560a1ce390b)

