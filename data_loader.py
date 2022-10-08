import pandas as pd

class DataLoader():

    def preprocess_df(self, df, name):
        df.columns.values[1] = "Usage"
        df['bldg_name'] = name
        df['co2_emissions'] = df['Usage']*0.85
        df[['date', 'time']] = df['Date & Time'].str.split(' ', expand=True)
        df.drop(columns=['Date & Time'], inplace=True)
        return df

    def process_date(self, combined_df):
        combined_df.rename(columns={'date': 'full_date'}, inplace=True)
        combined_df[['month', 'date', 'year']] = combined_df["full_date"].str.split('/', expand=True)
        return combined_df

    def load_data(self):
        cowell_data = pd.read_csv('Cowell FY18-19.csv')
        combined_df = self.preprocess_df(cowell_data, "Cowell")
        csi = pd.read_csv('CSI FY18-19.csv')
        gillson = pd.read_csv('Gillson FY18-19.csv')
        gleeson = pd.read_csv('Gleeson FY18-19.csv')
        harney = pd.read_csv('Harney FY18-19.csv')
        hayes = pd.read_csv('Hayes Healy FY18-19.csv')
        uc = pd.read_csv('UC FY18-19.csv')


        df_list = [csi, gillson, gleeson, harney, hayes, uc]
        df_names = ['CSI', "Gillson", "Gleeson", "Harney", "Hayes", "UC"]

        for df, name in zip(df_list, df_names):
            combined_df = pd.concat([combined_df, self.preprocess_df(df, name)], ignore_index=True)
        return self.process_date(combined_df)
