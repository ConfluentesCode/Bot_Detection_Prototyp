import unittest

import datetime
from DataPreparator.Services.AccessLogReaderService.AccessLogReader import AccessLogReader

import os


class AccessLogReaderTest(unittest.TestCase):
    path = os.getcwd()
    happy_access_log_path = f'{os.path.abspath(os.path.join(path, os.pardir))}/InputFiles/logfiles_test_happy.log'
    sad_access_log_path = f'{os.path.abspath(os.path.join(path, os.pardir))}/InputFiles/logfiles_test_sad.log'

    reader = AccessLogReader()

    def test_if_accesslog_extraction_works_correctly_happy_path(self):
        result_happy = self.reader.read_file(self.happy_access_log_path)

        self.assertEqual(result_happy[0][0], '163.238.192.156')
        self.assertEqual(result_happy[0][1], datetime.datetime(2020, 1, 4, 11, 25, 48,
                                                               tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))))
        self.assertEqual(result_happy[0][2], 'GET')
        self.assertEqual(result_happy[0][3], '/static/images/amp/blog.png')
        self.assertEqual(result_happy[0][4], 'HTTP/1.0')
        self.assertEqual(result_happy[0][5], 200)
        self.assertEqual(result_happy[0][6], 'https://fletcher.com/main.php')
        self.assertEqual(result_happy[0][7],
                         'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749')

    def test_if_accesslog_extraction_works_correctly_sad_path(self):
        result_sad = self.reader.read_file(self.sad_access_log_path)

        self.assertEqual(result_sad[1][0], 'None')
        self.assertEqual(result_sad[1][1],
                         datetime.datetime(1, 1, 1, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))))
        self.assertEqual(result_sad[1][2], 'None')
        self.assertEqual(result_sad[1][3], 'HTTP1.0')
        self.assertEqual(result_sad[1][4], 'None')
        self.assertEqual(result_sad[1][5], 999)
        self.assertEqual(result_sad[1][6], 'None')
        self.assertEqual(result_sad[1][7], '-')
