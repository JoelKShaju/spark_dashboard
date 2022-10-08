import pandas as pd

class Aggregator():
    def __init__(self, combined_df):
        self.combined_df = combined_df

    def groupby_day_bldg(self):
        return self.combined_df.groupby(['full_date', 'bldg_name']).sum()
    def groupby_day(self):
        return self.combined_df.groupby(['full_date']).sum()

    def groupby_month(self):
        return self.combined_df.groupby(['month', 'year']).sum()

    def groupby_month_bldg(self):
        return self.combined_df.groupby(['month', 'year', 'bldg_name']).sum()

    def groupby_year(self):
        return self.combined_df.groupby(['year']).sum()

    def groupby_year_bldg(self):
        return self.combined_df.groupby(['year', 'bldg_name']).sum()

    def groupby_week(self):
        self.combined_df['full_date'] = pd.to_datetime(self.combined_df['full_date']) - pd.to_timedelta(7, unit='d')
        
        return self.combined_df.groupby([pd.Grouper(key='full_date', freq='W')]).sum()

    def groupby_week_bldg(self):
        self.combined_df['full_date'] = pd.to_datetime(self.combined_df['full_date']) - pd.to_timedelta(7, unit='d')
        
        return self.combined_df.groupby([pd.Grouper(key='full_date', freq='W'), pd.Grouper(key='bldg_name')]).sum()