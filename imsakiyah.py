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

def setEvent(times, name, key, todayTimeStr, hourDelta=7, seconDelta=5, formatDatetime='%Y-%m-%d %H:%M:%S'):
    e = Event()
    e.name = name
    wkt = setWaktu(times[key], todayTimeStr, hourDelta, formatDatetime)
    e.begin = wkt.strftime(formatDatetime)
    e.end = (wkt+timedelta(seconds=seconDelta)).strftime(formatDatetime)

    return e


def generate(lat, lon, startdate, days, method, option):
    PT = PrayTimes(method)
    if option == '+8':
        PT.adjust({'imsak':'10 min', 'fajr':17.8, 'dhuhr':'2 min', 'asr':'1.03', 'maghrib':1.5,'isha':18.7})
    else:
        PT.adjust({'imsak':'10 min', 'fajr':19.4, 'dhuhr':'2 min', 'asr':'1.03', 'maghrib':1.8,'isha':18.7})
    #result = []

    c = Calendar() 

    formatDate = '%Y-%m-%d'
    formatDatetime = '%Y-%m-%d %H:%M:%S'
    hourDelta = 7
    secondDelta = 5

    mapTime = {
        'Imsak': 'imsak',
        'Subuh': 'fajr',
        'Dzuhur': 'dhuhr',
        'Asar': 'asr',
        'Maghrib': 'maghrib',
        'Isya': 'isha',
    }
    
    dte = datetime.strptime(startdate, formatDate)    
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

        todayTimeStr = today.strftime(formatDate)

        for name, key in mapTime.items():
            e = setEvent(times, name, key, todayTimeStr, hourDelta, secondDelta, formatDatetime)
            c.events.add(e)
        
        


    with open('jadwal_imsakiyah_%s_%s.ics' % (lat, lon), 'w') as f:
        f.write(str(c))
    #print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generator wktiyah ics/iCal. \r\nUsage: python imsakiyah.py <lat> <lon> <yyyy-mm-dd> <days> <method> --option=+8', formatter_class=RawTextHelpFormatter)
    parser.add_argument('lat', type=str, 
                        help='Latitude')
    parser.add_argument('lon', type=str, 
                        help='Longitude')
    parser.add_argument('date', type=str, 
                        help='Date format YYYY-MM-DD')
    parser.add_argument('days', type=int, default=30,
                        help='Periode. Default 30 days')
    parser.add_argument('method', type=str, default='Makkah',
                        help='Method. Default: Makkah')
    parser.add_argument('--option', type=str, default='-',
                        help='Option. type `+8` for Muhammadiyah version')
    args = parser.parse_args()
    
    generate(args.lat, args.lon, args.date, args.days, args.method, args.option)
