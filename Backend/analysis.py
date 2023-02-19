#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 08:42:26 2023

@author: armsy326
"""
##
##This is malaria.ipynb file converted to .py for ease of use
##
##

import pandas as pd
import numpy as np
import statistics
import math
import matplotlib.pyplot as plt


#read data from the csv file
df = pd.read_csv('data.csv')
#pd.options.display.max_rows = 100

#get top 5 results
#basically shows the data frame
#uncomment to see the data frame
#df.head()

#get the columns
#gives the columns present
def get_columns():
    res = df.columns
    columns = []
    for column in res:
        columns.append(column)
    return f"The columns present are: {columns}"

#get the info and shape
#uncomment to run
def get_info():

    res = df.info()

    return res

def get_shape():

    res = df.shape

    return f"The dataset has {res[0]} columns and {res[1]} rows."

#renaming helps in accessing the data
#rename the columns
new_names  = {"Baringo County": 'baringo', "Bomet County": 'bomet', "Bungoma County": 'bungoma', "Busia County": 'busia', "Elgeyo Marakwet County": 'elgeyo',
               "Embu County": 'embu', "Garissa County": 'garissa', "Homa Bay County": 'homabay', "Isiolo County": 'isiolo', "Kajiado County": 'kajiado',
                "Kakamega County": 'kakamega', "Kericho County": 'kericho', "Kiambu County": 'kiambu', "Kilifi County": 'kilifi', "Kirinyaga County": 'kirinyaga',
                "Kisii County": 'kisii', "Kisumu County": 'kisumu', "Kitui County": 'kitui', "Kwale County": 'kwale', "Laikipia County": 'laikipia', "Lamu County": 'lamu',
                "Machakos County": 'machakos', "Makueni County": 'makueni', "Mandera County": 'mandera', "Marsabit County": 'marsabit', "Meru County": 'meru', "Migori County": 'migori',
                "Mombasa County": 'mombasa', "Muranga County": 'muranga', "Nairobi County": 'nairobi', "Nakuru County": 'nakuru', "Nandi County": 'nandi', "Narok County": 'narok',
                "Nyamira County": 'nyamira', "Nyandarua County": 'nyandarua', "Nyeri County": 'nyeri', "Samburu County": 'samburu', "Siaya County": 'siaya', "Taita Taveta County": 'taita', 
                "Tana River County": 'tanariver', "Tharaka Nithi County": 'tharaka', "Trans Nzoia County": 'transzoia', "Turkana County": 'turkana', "Uasin Gishu County": 'uasingishu',
                "Vihiga County": 'vihiga', "Wajir County": 'wajir', "West Pokot County": 'westpokot'}

df.rename(columns=new_names, inplace=True)

#get all period ids -> so as to get specific data in each county 
#with these ids we can get totals across months 
#1.per month first
period_ids  =  [ period for period in df['periodid']]
period_names = [ periodname for periodname in df['periodname']]

#getting total nulls for each county
def check_null_values(county=None):
    try:
        if county == None:
            null_values = []
            for k,v in new_names.items():
                total_null = df[v].isnull().sum()

                if total_null == 0:
                    pass
                else:
                    null_values.append(f"{k} -> {total_null}")
                #print(f"{k} -> {total_null}")
            return f"Counties with null values include: {null_values}"

        elif county != None:

            total_null = df[county].isnull().sum()
            return f"{county} has {total_null} null values"

    except Exception:
        return "I'm sorry I didn't get county name: Try 'check null for followed by county name'."

#filling null values
#replace null value with 0
null_values = {}
def fillna(county=None):
    if county == None:
        for k,v in new_names.items():
            #get the total of missing values 
            total_null = [df[v] > 202]
            print(f"{k} -> {total_null}")
    elif county != None:

        total_null = df[county].isnull().sum()
        print(f"{county} has {total_null}s")
#fillna()
#not filling anything
#df.fillna(0, inplace=True)


###############################################################
##
## MONTH : BASED ON MONTH   AND PER CERTAIN ID                     
##I.E 202212 DATA COLLECTED ON 2022 , 12TH DEC EACH CPUNTY
###############################################################
#a function to dispaly total items per county 
#each county each period
county_monthly_consumption = []
county_names  = []
def all_items(county=None,periodid=None):
    county_monthly_consumption.clear()
    county_names.clear()
    try:
        if county == None and periodid == None:
            for periodid in period_ids:

                val = df.loc[df['periodid']==periodid].sum()

                for k,v in new_names.items():
                    #print(v)
                    commodity_total = val[v]
                    return f"{v} has {commodity_total} kits in {periodid}"

        elif county == None and periodid != None:
    
            val = df.loc[df['periodid']==periodid].sum()

            for k,v in new_names.items():
                #print(v)
                commodity_total = val[v]
                county_monthly_consumption.append(commodity_total)
                county_names.append(v)#
                
                return f"{v} had {commodity_total} kits in {periodid}"
            #print(county_monthly_consumption)

        elif county != None and periodid != None:

            val = df.loc[df['periodid']==periodid].sum()
        
            commodity_total = val[county]
            
            return f"{county} has {commodity_total} kits in {periodid}"

        elif county != None:

            for periodid in period_ids:

                val = df.loc[df['periodid']==periodid].sum()

                commodity_total = val[county]
                return f"{county} had {commodity_total} kits in {periodid}"

        else:

            return "A grave error, an error that should'nt occur has occurred!"

    except Exception as e:

        if e.__class__.__name__ == 'KeyError':
            return "An error occurred please report it out!"

#all_items(periodid=201801)

###############################################################
#get total, mean and median for every row (each  month begin from 202201 to 201812)
#ie summation across january on 2021 or accross feb
#import numpy to get mean
#get data for each county and  whole year for rows
###############################################################
years = [2018, 2019,2020,2021,2022]
total_items_each_row = []
county_yearly_vals = []
def total_items_per_row(period=None):
    total_items_each_row.clear()
    
    try:
        row_data = df.loc[df['periodid'] == period].sum()
        
        for k,v in new_names.items():
                #print(k,row_data[v],period)
                total_items_each_row.append(row_data[v])
        
        #print(statistics.fmean(total_items_each_row))
        total_items_per_period = np.sum(total_items_each_row)
        mean_total_items = np.mean(total_items_each_row)
        median_total_items = np.median(total_items_each_row)

        return {"sum": total_items_per_period, "mean": math.floor(mean_total_items), "median": median_total_items}

    except Exception as e:
        return "An error that Wasn't supposed to happen!"
        
#total_items_per_row(201804)
###############################################################
#get total, mean and median for every column (each  year begin from 202201 to 201812)
#ie summation from jan to dec each year
#
###############################################################

"""county_yearly_vals = []
def total_items_per_column(period=None,county=None):
    
    county_yearly_vals.clear()
   
    if county == None:
        print("Please select a county for now!")
    else: 
        try:
            #select the column data("county")
            county_values = df[county]
            #print(period)
            column_data = county_values.loc[df['periodid'] == period].sum()
            
            return column_data
           

        except Exception as e:
            print("Wasn't supposed to happen!")

         

#total_items_per_row(202201)

#get data for each county and  whole year
###########################################################################################
## EACH COUNTY GETS TOTAL DATA FOR A PARTICULAR YEAR                                    ###  
##I.E TAKES A PARTICULAR YEAR AND COUNTY, GETS THE DATA BY LOOPING THROUGH EACH MONTH  ###
#########################################################################################
county_yearly_report = {}
def county_yearly_reports():
    
    #2022,2021,2020,2019,2018

    for year in years:
            #print(year)
            #locate all rows with specific years
            #total_mean = []
            total_sum = {}
            total_per_column = []
            #total_median = []

            for period in period_ids:
                
                if str(period)[:4] == str(year):
                    values = total_items_per_column(period=period,county='baringo')
                    total_per_column.append(values)
# 
county_yearly_reports() """
    
#get total sum, mean and median per year
#the dict takes in a specific year and the total
###############################################################
##
## MONTH : BASED ON YEARS AND SUMS ACROSS ALL COUNTIES                    
##I.E TAKES A PARTICULAR YEAR AND GETS THE DATA ACROSS AND SUMS ALL FOR THAT YEAR LOOPING THROUGH EACH
###############################################################
yearly_report = {}
def yearly_reports(year=None):
    yearly_report.clear()
    #2022,2021,2020,2019,2018

    for year in years:
            #locate all rows with specific years
            total_mean = []
            total_sum = []
            total_median = []
            for period in period_ids:
                if str(period)[:4] == str(year):
                    values = total_items_per_row(period)
                    #print(values, period)
                    total_sum.append(values['sum'])
                    total_mean.append(values['mean'])
                    total_median.append(values['median'])
            #print(monthly_totals)
            sums = np.sum(total_sum)
            mean = np.sum(total_mean)
            median = np.sum(total_median)
           
            yearly_report[year] = {"sum": sums, "mean": mean, "median": median}
    return yearly_report
    #print(yearly_report)

#yearly_reports()
    