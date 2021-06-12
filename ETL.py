# import libraries
import numpy as np
import datetime as dt
import pandas as pd
import umap.umap_ as umap
import hdbscan

class etl():
    def __init__(self,date_interval=['2019-03-01','2020-01-01'], home_dir='/home/gopherguy14/datasets'):
        self.dt_inter = date_interval
        self.home_dir = home_dir

    def load_crash_data(self):
        # load crash data
        self.crashes_df = pd.read_csv(self.home_dir + '/US_Accidents_Dec20.csv')
        # filter
        self.crashes_df['Start_Time'] = self.crashes_df.Start_Time.astype('datetime64[ns]')
        self.crashes_df['Start_Date'] = self.crashes_df.Start_Time.dt.date
        self.crashes_df = self.crashes_df[ (self.crashes_df['Start_Time'] >= self.dt_inter[0]) & (self.crashes_df['Start_Time'] < self.dt_inter[1]) ] 
        # drop duplicate ids
        self.crashes_df = self.crashes_df.drop_duplicates(subset='ID')
    
    def load_pop_data(self): 
        # load population data
        self.pop_df = pd.read_csv(self.home_dir + '/covid_county_population.csv')
        # create county variable without the word 'county'
        self.pop_df['County'] = self.pop_df['County Name'].str.split(' ',expand=True)[9]
        # filter out the 'statewide' category
        self.pop_df = pop_df[ pop_df['County'] != 'Statewide']
        # drop old county name column
        self.pop_df = pop_df.drop(columns=['County Name', 'countyFIPS'])
        # drop duplicates just in case
        self.pop_df = pop_df.drop_duplicates()

# to allow things to import
if __name__ == '__main__':
    main()  
