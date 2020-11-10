import unittest
from datetime import datetime
from simple_dwd_weatherforecast import dwdforecast
from test_data import parsed_data


class Weather_get_day_values(unittest.TestCase):

    def setUp(self):
        self.dwd_weather = dwdforecast.Weather("H889")
        self.dwd_weather.forecast_data = parsed_data
        self.dwd_weather.station_name = "BAD HOMBURG"

    def test_day_not_current_day(self):
        test_time = datetime(2020, 11, 7, 10, 0)
        test_data = [
            {
                'TTT': 275.05, 'Td': 273.25, 'condition': '45', 'PPPP': 103040.0, 'DD': 55.0, 'FF': 1.54, 'FX1': 2.57, 'RR1c': 7.65, 'wwP': 2.0, 'DRR1': 0.0, 'N': 23.0, 'VV': 13300.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                'TTT': 274.55, 'Td': 273.15, 'condition': '75', 'PPPP': 103030.0, 'DD': 52.0, 'FF': 1.54, 'FX1': 2.57, 'RR1c': 6.54, 'wwP': 3.0, 'DRR1': 0.0, 'N': 24.0, 'VV': 12900.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                'TTT': 274.35, 'Td': 273.15, 'condition': '0', 'PPPP': 103010.0, 'DD': 52.0, 'FF': 1.54, 'FX1': 2.57, 'RR1c': 5.43, 'wwP': 1.0, 'DRR1': 0.0, 'N': 28.0, 'VV': 12200.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 3.0}, {
                    'TTT': 274.35, 'Td': 273.25, 'condition': '0', 'PPPP': 103000.0, 'DD': 53.0, 'FF': 1.54, 'FX1': 2.57, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 31.0, 'VV': 10900.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 5.0}, {
                        'TTT': 274.35, 'Td': 273.35, 'condition': '0', 'PPPP': 102970.0, 'DD': 51.0, 'FF': 1.54, 'FX1': 3.09, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 35.0, 'VV': 9600.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 6.0}, {
                            'TTT': 274.55, 'Td': 273.45, 'condition': '0', 'PPPP': 102950.0, 'DD': 53.0, 'FF': 1.54, 'FX1': 3.09, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 40.0, 'VV': 8700.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 6.0}, {
                                'TTT': 274.85, 'Td': 273.55, 'condition': '0', 'PPPP': 102950.0, 'DD': 64.0, 'FF': 1.54, 'FX1': 3.09, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 41.0, 'VV': 8000.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 6.0}, {
                                    'TTT': 275.75, 'Td': 273.85, 'condition': '1', 'PPPP': 102930.0, 'DD': 65.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 45.0, 'VV': 8300.0, 'SunD1': 660.0, 'Rad1h': None, 'wwM': 7.0}, {
                                        'TTT': 276.95, 'Td': 274.35, 'condition': '1', 'PPPP': 102920.0, 'DD': 69.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 45.0, 'VV': 8100.0, 'SunD1': 1260.0, 'Rad1h': None, 'wwM': 7.0}, {
                                            'TTT': 278.05, 'Td': 274.75, 'condition': '1', 'PPPP': 102900.0, 'DD': 72.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 43.0, 'VV': 9400.0, 'SunD1': 1920.0, 'Rad1h': None, 'wwM': 7.0}, {
                                                'TTT': 279.25, 'Td': 275.15, 'condition': '1', 'PPPP': 102860.0, 'DD': 85.0, 'FF': 1.54, 'FX1': 4.12, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 42.0, 'VV': 10200.0, 'SunD1': 2340.0, 'Rad1h': None, 'wwM': 5.0}, {
                                                    'TTT': 280.55, 'Td': 275.35, 'condition': '1', 'PPPP': 102800.0, 'DD': 96.0, 'FF': 1.54, 'FX1': 4.63, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 40.0, 'VV': 12400.0, 'SunD1': 2580.0, 'Rad1h': None, 'wwM': 3.0}, {
                                                        'TTT': 281.65, 'Td': 275.85, 'condition': '1', 'PPPP': 102720.0, 'DD': 87.0, 'FF': 1.54, 'FX1': 4.12, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 38.0, 'VV': 14700.0, 'SunD1': 2880.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                            'TTT': 282.45, 'Td': 275.95, 'condition': '1', 'PPPP': 102670.0, 'DD': 90.0, 'FF': 1.54, 'FX1': 4.12, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 37.0, 'VV': 16200.0, 'SunD1': 2880.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                                'TTT': 282.95, 'Td': 276.15, 'condition': '1', 'PPPP': 102620.0, 'DD': 87.0, 'FF': 1.54, 'FX1': 4.12, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 35.0, 'VV': 17400.0, 'SunD1': 2760.0, 'Rad1h': None, 'wwM': 0.0}, {
                                                                    'TTT': 282.25, 'Td': 276.25, 'condition': '1', 'PPPP': 102590.0, 'DD': 99.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 34.0, 'VV': 17600.0, 'SunD1': 2220.0, 'Rad1h': None, 'wwM': 0.0}, {
                                                                        'TTT': 281.65, 'Td': 276.55, 'condition': '1', 'PPPP': 102600.0, 'DD': 99.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 36.0, 'VV': 16100.0, 'SunD1': 1500.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                                            'TTT': 280.65, 'Td': 276.55, 'condition': '1', 'PPPP': 102600.0, 'DD': 105.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 37.0, 'VV': 14400.0, 'SunD1': 480.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                                                'TTT': 279.35, 'Td': 276.85, 'condition': '1', 'PPPP': 102640.0, 'DD': 89.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 34.0, 'VV': 11400.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                                                    'TTT': 278.35, 'Td': 276.65, 'condition': '0', 'PPPP': 102640.0, 'DD': 81.0, 'FF': 1.54, 'FX1': 3.09, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 31.0, 'VV': 10000.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                                                                                        'TTT': 277.75, 'Td': 276.65, 'condition': '0', 'PPPP': 102630.0, 'DD': 65.0, 'FF': 1.54, 'FX1': 3.09, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 30.0, 'VV': 8700.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                                                                                            'TTT': 277.35, 'Td': 276.25, 'condition': '0', 'PPPP': 102630.0, 'DD': 57.0, 'FF': 1.03, 'FX1': 2.57, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 29.0, 'VV': 7400.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                                                                                                'TTT': 276.85, 'Td': 275.85, 'condition': '0', 'PPPP': 102600.0, 'DD': 55.0, 'FF': 1.03, 'FX1': 2.57, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 30.0, 'VV': 7100.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                                                                                                    'TTT': 276.65, 'Td': 275.75, 'condition': '0', 'PPPP': 102590.0, 'DD': 58.0, 'FF': 1.54, 'FX1': 2.57, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 32.0, 'VV': 6500.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 3.0}]

        self.assertEqual(
            self.dwd_weather.get_day_values(test_time), test_data,)

    def test_day_not_last_day(self):
        test_time = datetime(2020, 11, 16, 1, 0)
        test_data = [{'TTT': 279.05,
                      'Td': 277.85,
                      'condition': '3',
                      'PPPP': 101960.0,
                      'DD': 153.0,
                      'FF': 2.06,
                      'FX1': 4.63,
                      'RR1c': 0.0,
                      'wwP': 24.0,
                      'DRR1': 0.0,
                      'N': 75.0,
                      'VV': 11600.0,
                      'SunD1': 0.0,
                      'Rad1h': None,
                      'wwM': 2.0},
                     {'TTT': 278.95,
                      'Td': 277.85,
                      'condition': '3',
                      'PPPP': 101950.0,
                      'DD': 155.0,
                      'FF': 2.06,
                      'FX1': 4.63,
                      'RR1c': 0.0,
                      'wwP': 24.0,
                      'DRR1': 0.0,
                      'N': 76.0,
                      'VV': 10900.0,
                      'SunD1': 0.0,
                      'Rad1h': None,
                      'wwM': 2.0},
                     {'TTT': 278.85,
                      'Td': 277.75,
                      'condition': '3',
                      'PPPP': 101930.0,
                      'DD': 159.0,
                      'FF': 2.06,
                      'FX1': 4.12,
                      'RR1c': 0.0,
                      'wwP': 24.0,
                      'DRR1': 0.0,
                      'N': 77.0,
                      'VV': 10000.0,
                      'SunD1': 0.0,
                      'Rad1h': None,
                      'wwM': 3.0},
                     {'TTT': 278.75,
                      'Td': 277.75,
                      'condition': '3',
                      'PPPP': 101910.0,
                      'DD': 155.0,
                      'FF': 2.06,
                      'FX1': 4.63,
                      'RR1c': 0.0,
                      'wwP': 24.0,
                      'DRR1': 0.0,
                      'N': 78.0,
                      'VV': 9200.0,
                      'SunD1': 0.0,
                      'Rad1h': None,
                      'wwM': 6.0},
                     {'TTT': 278.75,
                      'Td': 277.95,
                      'condition': '3',
                      'PPPP': 101900.0,
                      'DD': 161.0,
                      'FF': 2.06,
                      'FX1': 4.63,
                      'RR1c': 0.0,
                      'wwP': 25.0,
                      'DRR1': 0.0,
                      'N': 79.0,
                      'VV': 8800.0,
                      'SunD1': 0.0,
                      'Rad1h': None,
                      'wwM': 6.0},
                     {'TTT': 277.75,
                      'Td': 276.55,
                      'condition': '3',
                      'PPPP': 101700.0,
                      'DD': 163.0,
                      'FF': 2.57,
                      'FX1': 5.66,
                      'RR1c': 0.0,
                      'wwP': 28.0,
                      'DRR1': 0.0,
                      'N': 81.0,
                      'VV': 8900.0,
                      'SunD1': 0.0,
                      'Rad1h': None,
                      'wwM': 5.0},
                     {'TTT': 277.85,
                      'Td': 276.65,
                      'condition': '3',
                      'PPPP': 101700.0,
                      'DD': 164.0,
                      'FF': 3.09,
                      'FX1': 5.66,
                      'RR1c': 0.0,
                      'wwP': 28.0,
                      'DRR1': 0.0,
                      'N': 82.0,
                      'VV': 8300.0,
                      'SunD1': 0.0,
                      'Rad1h': None,
                      'wwM': 5.0},
                     {'TTT': 277.95,
                      'Td': 276.65,
                      'condition': '3',
                      'PPPP': 101720.0,
                      'DD': 165.0,
                      'FF': 3.09,
                      'FX1': 6.17,
                      'RR1c': 0.0,
                      'wwP': 29.0,
                      'DRR1': 0.0,
                      'N': 84.0,
                      'VV': 8200.0,
                      'SunD1': 60.0,
                      'Rad1h': None,
                      'wwM': 7.0},
                     {'TTT': 278.25,
                      'Td': 276.85,
                      'condition': '3',
                      'PPPP': 101740.0,
                      'DD': 169.0,
                      'FF': 3.09,
                      'FX1': 6.17,
                      'RR1c': 0.0,
                      'wwP': 29.0,
                      'DRR1': 0.0,
                      'N': 84.0,
                      'VV': 8800.0,
                      'SunD1': 240.0,
                      'Rad1h': None,
                      'wwM': 6.0},
                     {'TTT': 278.85,
                      'Td': 277.05,
                      'condition': '3',
                      'PPPP': 101750.0,
                      'DD': 172.0,
                      'FF': 3.09,
                      'FX1': 6.17,
                      'RR1c': 0.0,
                      'wwP': 29.0,
                      'DRR1': 0.0,
                      'N': 84.0,
                      'VV': 9400.0,
                      'SunD1': 480.0,
                      'Rad1h': None,
                      'wwM': 5.0},
                     {'TTT': 279.45,
                      'Td': 277.25,
                      'condition': '-',
                      'PPPP': 101750.0,
                      'DD': 178.0,
                      'FF': 3.09,
                      'FX1': 6.69,
                      'RR1c': 0.0,
                      'wwP': 31.0,
                      'DRR1': 0.0,
                      'N': 83.0,
                      'VV': 11000.0,
                      'SunD1': 600.0,
                      'Rad1h': None,
                      'wwM': 4.0}]
        self.assertEqual(
            self.dwd_weather.get_day_values(test_time), test_data,)

    def test_day_first_day(self):
        test_time = datetime(2020, 11, 6, 6, 0)
        test_data = [
            {
                'TTT': 272.95, 'Td': 272.65, 'condition': '2', 'PPPP': 103640.0, 'DD': 50.0, 'FF': 1.54, 'FX1': 3.09, 'RR1c': 0.01, 'wwP': 2.0, 'DRR1': 0.0, 'N': 35.0, 'VV': 8000.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 8.0}, {
                'TTT': 273.05, 'Td': 272.45, 'condition': '3', 'PPPP': 103620.0, 'DD': 52.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.12, 'wwP': 3.0, 'DRR1': 0.0, 'N': 36.0, 'VV': 6400.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 9.0}, {
                'TTT': 273.65, 'Td': 272.55, 'condition': '1', 'PPPP': 103610.0, 'DD': 51.0, 'FF': 2.06, 'FX1': 3.6, 'RR1c': 1.23, 'wwP': 2.0, 'DRR1': 0.0, 'N': 38.0, 'VV': 5300.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 10.0}, {
                    'TTT': 274.55, 'Td': 272.85, 'condition': '45', 'PPPP': 103610.0, 'DD': 52.0, 'FF': 2.06, 'FX1': 3.6, 'RR1c': 2.34, 'wwP': 2.0, 'DRR1': 0.0, 'N': 41.0, 'VV': 5200.0, 'SunD1': 780.0, 'Rad1h': None, 'wwM': 9.0}, {
                        'TTT': 275.95, 'Td': 273.55, 'condition': '49', 'PPPP': 103610.0, 'DD': 52.0, 'FF': 2.06, 'FX1': 4.12, 'RR1c': 3.45, 'wwP': 1.0, 'DRR1': 0.0, 'N': 42.0, 'VV': 6200.0, 'SunD1': 1500.0, 'Rad1h': None, 'wwM': 8.0}, {
                            'TTT': 277.65, 'Td': 273.85, 'condition': '1', 'PPPP': 103590.0, 'DD': 55.0, 'FF': 2.06, 'FX1': 4.63, 'RR1c': 4.56, 'wwP': 1.0, 'DRR1': 0.0, 'N': 38.0, 'VV': 9700.0, 'SunD1': 2160.0, 'Rad1h': None, 'wwM': 7.0}, {
                                'TTT': 279.15, 'Td': 273.85, 'condition': '1', 'PPPP': 103540.0, 'DD': 55.0, 'FF': 2.06, 'FX1': 5.14, 'RR1c': 5.67, 'wwP': 1.0, 'DRR1': 0.0, 'N': 35.0, 'VV': 12000.0, 'SunD1': 2700.0, 'Rad1h': None, 'wwM': 5.0}, {
                                    'TTT': 280.85, 'Td': 273.55, 'condition': '1', 'PPPP': 103500.0, 'DD': 62.0, 'FF': 2.06, 'FX1': 5.14, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 33.0, 'VV': 15900.0, 'SunD1': 3120.0, 'Rad1h': None, 'wwM': 3.0}, {
                                        'TTT': 281.85, 'Td': 273.35, 'condition': '1', 'PPPP': 103420.0, 'DD': 66.0, 'FF': 2.57, 'FX1': 5.66, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 31.0, 'VV': 21300.0, 'SunD1': 3180.0, 'Rad1h': None, 'wwM': 2.0}, {
                                            'TTT': 282.65, 'Td': 273.25, 'condition': '1', 'PPPP': 103350.0, 'DD': 73.0, 'FF': 2.57, 'FX1': 5.66, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 30.0, 'VV': 22700.0, 'SunD1': 3180.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                'TTT': 283.05, 'Td': 273.35, 'condition': '1', 'PPPP': 103280.0, 'DD': 74.0, 'FF': 2.06, 'FX1': 5.14, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 30.0, 'VV': 24500.0, 'SunD1': 3120.0, 'Rad1h': None, 'wwM': 0.0}, {
                                                    'TTT': 282.35, 'Td': 273.35, 'condition': '0', 'PPPP': 103240.0, 'DD': 76.0, 'FF': 2.06, 'FX1': 5.14, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 29.0, 'VV': 26800.0, 'SunD1': 2640.0, 'Rad1h': None, 'wwM': 0.0}, {
                                                        'TTT': 281.35, 'Td': 273.25, 'condition': '0', 'PPPP': 103190.0, 'DD': 78.0, 'FF': 2.06, 'FX1': 4.63, 'RR1c': 0.0, 'wwP': 2.0, 'DRR1': 0.0, 'N': 28.0, 'VV': 25300.0, 'SunD1': 1740.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                            'TTT': 280.25, 'Td': 273.15, 'condition': '0', 'PPPP': 103170.0, 'DD': 76.0, 'FF': 1.54, 'FX1': 4.63, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 28.0, 'VV': 23200.0, 'SunD1': 540.0, 'Rad1h': None, 'wwM': 1.0}, {
                                                                'TTT': 278.95, 'Td': 273.65, 'condition': '0', 'PPPP': 103150.0, 'DD': 70.0, 'FF': 1.54, 'FX1': 4.12, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 28.0, 'VV': 21900.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                                                                    'TTT': 277.85, 'Td': 273.55, 'condition': '0', 'PPPP': 103140.0, 'DD': 65.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 25.0, 'VV': 20300.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                                                                        'TTT': 277.15, 'Td': 273.55, 'condition': '0', 'PPPP': 103120.0, 'DD': 52.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 22.0, 'VV': 18500.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 2.0}, {
                                                                            'TTT': 276.75, 'Td': 273.65, 'condition': '0', 'PPPP': 103100.0, 'DD': 54.0, 'FF': 1.54, 'FX1': 3.6, 'RR1c': 0.0, 'wwP': 1.0, 'DRR1': 0.0, 'N': 22.0, 'VV': 17000.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 3.0}, {
                                                                                'TTT': 276.25, 'Td': 273.35, 'condition': '0', 'PPPP': 103070.0, 'DD': 49.0, 'FF': 1.54, 'FX1': 3.09, 'RR1c': 9.87, 'wwP': 2.0, 'DRR1': 0.0, 'N': 21.0, 'VV': 16600.0, 'SunD1': 0.0, 'Rad1h': None, 'wwM': 3.0}]
        self.assertEqual(
            self.dwd_weather.get_day_values(test_time), test_data,)