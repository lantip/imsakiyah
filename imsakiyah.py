#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__     =   "0.0.1"
__author__      =   "@lantip"
__date__        =   "2021/04/31"
__description__ =   "Imsakiyah ics file generator"
""" 

from praytimes import PrayTimes 
from datetime import datetime, timedelta
from ics import Calendar, Event
import argparse
from argparse import RawTextHelpFormatter

def generate(lat, lon, startdate, days):
    PT = PrayTimes('Makkah')
    PT.adjust({'imsak':'10 min', 'fajr':17.8, 'dhuhr':'2 min', 'asr':'1.03', 'maghrib':1.5,'isha':18.7})
    #result = []

    c = Calendar() 
    
    dte = datetime.strptime(startdate, '%Y-%m-%d')    
    for i in range(days):
        today = dte + timedelta(days=i)
        times = PT.getTimes(today.date(), [float(lat),float(lon)],+7)
        '''
        result.append({
            'imsak': times['imsak'],
            'subuh': times['fajr'],
            'dzuhur': times['dhuhr'],
            'asar': times['asr'],
            'maghrib': times['maghrib'],
            'isya': times['isha']
        })
        '''
        
        e = Event()
        e.name = 'Imsak'
        wkt = datetime.strptime(today.strftime('%Y-%m-%d')+' '+times['imsak']+':00', '%Y-%m-%d %H:%M:%S')
        wkt = wkt - timedelta(hours=7)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Subuh'
        wkt = datetime.strptime(today.strftime('%Y-%m-%d')+' '+times['fajr']+':00', '%Y-%m-%d %H:%M:%S')
        wkt = wkt - timedelta(hours=7)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Dzuhur'
        wkt = datetime.strptime(today.strftime('%Y-%m-%d')+' '+times['dhuhr']+':00', '%Y-%m-%d %H:%M:%S')
        wkt = wkt - timedelta(hours=7)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Asar'
        wkt = datetime.strptime(today.strftime('%Y-%m-%d')+' '+times['asr']+':00', '%Y-%m-%d %H:%M:%S')
        wkt = wkt - timedelta(hours=7)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Maghrib'
        wkt = datetime.strptime(today.strftime('%Y-%m-%d')+' '+times['maghrib']+':00', '%Y-%m-%d %H:%M:%S')
        wkt = wkt - timedelta(hours=7)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Isya'
        wkt = datetime.strptime(today.strftime('%Y-%m-%d')+' '+times['isha']+':00', '%Y-%m-%d %H:%M:%S')
        wkt = wkt - timedelta(hours=7)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        


    with open('jadwal_imsakiyah_%s_%s.ics' % (lat, lon), 'w') as f:
        f.write(str(c))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generator wktiyah ics/iCal. \r\nUsage: python imsakiyah.py <lat> <lon> <yyyy-mm-dd> <days>', formatter_class=RawTextHelpFormatter)
    parser.add_argument('lat', type=str, 
                        help='Latitude')
    parser.add_argument('lon', type=str, 
                        help='Longitude')
    parser.add_argument('date', type=str, 
                        help='Date format YYYY-MM-DD')
    parser.add_argument('days', type=int, default=30,
                        help='Periode. Default 30 days')
    args = parser.parse_args()
    
    generate(args.lat, args.lon, args.date, args.days)