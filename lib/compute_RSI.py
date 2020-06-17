def computeRSI(data, rsi_period):
    chg = data.diff(1).dropna()

    gain = chg.mask(chg < 0, 0)
    loss = chg.mask(chg > 0, 0)

    avg_gain = gain.ewm(com=rsi_period - 1, min_periods=rsi_period).mean()
    avg_loss = loss.ewm(com=rsi_period - 1, min_periods=rsi_period).mean()

    rs = abs(avg_gain / avg_loss)
    rsi = 100 - (100 / (1 + rs))
    rsi = list(rsi)[-1]
    return rsi
