#!/usr/bin/env python
# coding: utf-8

import yfinance as yf

print('Enter a Tickername from Yahoo')
tickername = input('Enter a Ticker ')

print('Valid Periods: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo, max')
tickerperiod = input('Enter the period ')

print('Valid Intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo')
tickerinterval = input('Enter a the Data interval ')

ticker = yf.download(tickers=tickername, period=tickerperiod, interval=tickerinterval)

ticker.to_csv(tickername+'.csv')



