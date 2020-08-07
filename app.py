import pandas as pd
import yfinance as yf
import datetime
from yahoo_fin import stock_info as si
import pandas as pd
import schedule
import time
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import os


from lib.stock_screenr import scanner
from lib.email import Email

load_dotenv(".env")
yf.pdr_override()
envs = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))

template = envs.get_template('child.html')
stock_list = si.tickers_sp500()

#schedule.every(1).minutes.do(stock_scanner)
results = scanner(stock_list)


email = Email.send_email(results, envs)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
