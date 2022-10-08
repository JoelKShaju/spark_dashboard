import pandas as pd

def per_hour_consumption(combined_df, date, type):

    if type == "electricity":
        return combined_df[combined_df['day'=date]['bldg_name', 'date', 'time', 'Usage']]
    return combined_df[['bldg_name', 'date', 'time', 'co2_emissions']]
