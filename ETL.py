# import libraries
import numpy as np
import datetime as dt
import pandas as pd

# define class
class etl():
    def __init__(self, date_interval=['2019-03-20', '2020-12-31'], home_dir='/home/gopherguy14/datasets'):
        self.date_interval = [dt.datetime.strptime(d, '%Y-%m-%d') for d in date_interval] 
        self.home_dir = home_dir

    def load_crash_data(self):
        # load crash data
        self.crashes_df = pd.read_csv(self.home_dir + '/US_Accidents_Dec20.csv')
        # filter
        self.crashes_df['Start_Time'] = self.crashes_df.Start_Time.astype('datetime64[ns]')
        self.crashes_df['Start_Date'] = self.crashes_df.Start_Time.dt.date
        self.crashes_df = self.crashes_df[ (self.crashes_df['Start_Time'] >= self.date_interval[0]) & (self.crashes_df['Start_Time'] < self.date_interval[1]) ] 
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

    def load_covid(self):


    def pivot_data(self, index_list, target_col, date_interval=['2019-03-01','2020-06-30']):
        # optional subset, I guess
        date_interval = [dt.datetime.strptime(d, '%Y-%m-%d') for d in date_interval] 
        self.crashes_df = self.crashes_df[ (self.crashes_df['Start_Time'] >= date_interval[0]) & (self.crashes_df['Start_Time'] < date_interval[1]) ] 
        # aggregate
        self.data_cluster = self.data_cluster.groupby(index_list + target_col).agg({'ID':'count'})
        # pivot
        self.data_cluster = self.data_cluster.pivot(index=index_list, columns=target_col, values='ID')
        # reset index
        self.data_cluster = self.data_cluster.reset_index()
        # fill missing with 0
        self.data_cluster = self.data_cluster.fillna(0)

    def cluster_data(self, ):
        
    def plot_embedding(self, ):

    def write_cluster(self, ):

    def join_pop(self, ):

    def join_covid(self, ):

    def create_features(self, ):

    def write_database(self, ):

# to allow things to import
if __name__ == '__main__':
    main()  
