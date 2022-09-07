#The AILEA Code Challenge final model

import ftplib
import pandas as pd

def get_symbols():
    #STEP 1: this function retrieves teh symbols of interest from the NASDAQ
    #connection to the server
    #username and passwd required!
    ftp = ftplib.FTP('ftp.nasdaqtrader.com', 'Anonymous', 'guest')
    
    #retrieving the data file into our local directory
    ftp.cwd('/symboldirectory/')
    filename = 'nasdaqlisted.txt'
    ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
    ftplib.FTP.quit(ftp) #polite exit
    
    #extract just 50 first ones into data frame
    df = pd.read_csv(filename, sep='|', usecols=['Symbol'])
    #df.sort_values('Symbol') #actually useless as the list seems to be in order anyways
    return df.head(6)


from alpha_vantage.timeseries import TimeSeries
import time

def get_volumes(companies):
    #STEP 2: here we fetch 5 symbols having highest daily volume
    #by using Alpha Vantage API
    
    API_key = 'TYFN3678G5XYSVMO'
    
    av_data = pd.DataFrame({'symbol': [], 'volume': []})
    ts = TimeSeries(key=API_key, output_format='pandas')
    
    #Alpha Vantage API function get_daily() gives tuple (data, general_info).
    #So here av_data[0] refers to the data only.
    #Hence iloc[0] is its newest date and ['5. volume'] is corresponding trading volume.
    print('Obtaining that trade volume info for you. This may take quite some time... \n Thank you for understanding :) \n')
    for name in companies['Symbol']:
        new_row = pd.DataFrame({'symbol': [name], 'volume': [ts.get_daily(name)[0].iloc[0]['5. volume']]})
        av_data = pd.concat([av_data, new_row], ignore_index = True)
        time.sleep(15) #AV allows max 5 queries per minute
    
    #finally we sort and select 5 most traded ones
    print('(finally) Done!')
    return av_data.sort_values('volume', ascending=False, ignore_index=True).head(5)

import sqlite3 as sql

def write_to_database(volumes):
    #STEP 3: writing the data into a local database
    #Here we use sqlite as it was already familiar.
    #The table is recreated every time.
    db_connection = sql.connect('nasdaq_data.db')
    c = db_connection.cursor()
    c.execute('''DROP TABLE IF EXISTS most_traded''')
    volumes.to_sql('most_traded', db_connection)
    db_connection.close()


def full_model():
    #gathering everything above into a single function
    companies = get_symbols()
    volumes = get_volumes(companies)
    write_to_database(volumes)
    
if __name__ == '__full_model__':
    full_model()