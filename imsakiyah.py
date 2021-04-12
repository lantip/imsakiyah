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

def setWaktu(hourStr, todayTimeStr, hourDelta=7, formatTime='%Y-%m-%d %H:%M:%S'):
    wkt = datetime.strptime(todayTimeStr+' '+hourStr+':00', formatTime)
    wkt = wkt - timedelta(hours=hourDelta)

    return wkt

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

        todayTimeStr = today.strftime('%Y-%m-%d')
        
        e = Event()
        e.name = 'Imsak'
        wkt = setWaktu(times['imsak'], todayTimeStr)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Subuh'
        wkt = setWaktu(times['fajr'], todayTimeStr)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Dzuhur'
        wkt = setWaktu(times['dhuhr'], todayTimeStr)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Asar'
        wkt = setWaktu(times['asr'], todayTimeStr)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Maghrib'
        wkt = setWaktu(times['maghrib'], todayTimeStr)
        e.begin = wkt.strftime('%Y-%m-%d %H:%M:%S')
        e.end = (wkt+timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')
        c.events.add(e)
        
        e = Event()
        e.name = 'Isya'
        wkt = setWaktu(times['isha'], todayTimeStr)
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