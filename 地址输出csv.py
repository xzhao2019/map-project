#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:21:35 2019

@author: apple
"""

import requests
from numpy import *
import pandas as pd
data=[]
df=pd.read_csv('/Users/apple/Desktop/1531 address for python.csv')
alt=array(df[['poi_address']])
  
def geocode(address):

    parameters = {'address': address, 'key': 'UEFBZ-FEE6W-DU5RE-RKFAM-XXZE7-R4F2F'}
    base = 'https://apis.map.qq.com/ws/geocoder/v1/?'
    response = requests.get(base, parameters)
    answer = response.json()
            
    if answer['status']==0:
        data.append([answer['result']['location']['lat'],answer['result']['location']['lng'],answer['result']['address_components']['province'],answer['result']['address_components']['city'],answer['result']['address_components']['district']])
    else:
        data.append(['/','/','/','/','/'])

            
if __name__=='__main__':
    list=['lat','lng','province','city','district']
    cols=pd.DataFrame(columns=list)
    for i in range(0,1532): 
        address = alt[i]
        geocode(address)
        cols.loc[i]=data[i]
        cols.to_csv('/Users/apple/Desktop/results2.csv',index=False,sep=',',encoding='utf_8_sig')