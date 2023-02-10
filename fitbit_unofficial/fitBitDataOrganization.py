import os
import json
from functions.databaseLink import OpenSQLConnection
import sys
import time
import datetime

startTime = time.time()

directory = 'D:\\Mathematica Files 4K\\fitBitDataImport\\MyFitbitData\\AshwiniKumarKounduri\\user-site-export'
_sqlConnection = OpenSQLConnection('D:\\Programming\\_databases\\fitbitData.db')
_sqlCursor = _sqlConnection.cursor()

_sqlCursor.execute("DELETE FROM lightlyActiveMinutes")
_sqlConnection.commit()
_sqlCursor.execute("DELETE FROM moderatelyActiveMinutes")
_sqlConnection.commit()
_sqlCursor.execute("DELETE FROM sedentaryMinutes")
_sqlConnection.commit()
_sqlCursor.execute("DELETE FROM veryActiveMinutes")
_sqlConnection.commit()


def _dateValueExtractor(data: dict) -> list:
    return [data['dateTime'], data['value']]


def yearReformat(date_time_id: str) -> str:
    return date_time_id.replace('/18 ', '/2018 ').replace('/19 ', '/2019 ')


def parseDate(date_string: str) -> str or None:
    try:
        return_date = datetime.datetime.strptime(date_string, '%m/%d/%y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        return return_date
    except ValueError:
        return None


def timeDelta(start_time):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))


def tableCheckGeneral(table_name, date_min, date_max):
    return f"SELECT * FROM {table_name} WHERE dateTimeID IN ('{parseDate(date_min)}','{parseDate(date_max)}')"


def recordCheckGeneral(table_name, date_time):
    return f"SELECT * FROM {table_name} WHERE dateTimeID = '{parseDate(date_time)}'"


class AltitudeClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('altitude', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('altitude', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO altitude VALUES ('" + parseDate(data['dateTime']) + "', " + str(data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


class CaloriesClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('calories', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('calories', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO calories VALUES ('" + parseDate(data['dateTime']) + "', " + str(data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


class DistanceClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('distance', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('distance', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO distance VALUES ('" + parseDate(data['dateTime']) + "', " + str(data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


class HeartRateClass:

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO heartRate VALUES ('" + parseDate(data['dateTime']) + "', " + str(
            data['value']['bpm']) + ", " + str(data['value']['confidence']) + ")"

    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('heartRate', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('heartRate', data['dateTime'])

    @staticmethod
    def extractor(data: dict):
        return [data['dateTime'], data['value']['bpm'], data['value']['confidence']]


def timeInHRZonesSupport(data: dict):
    _vIZones = data['value']['valuesInZones']
    return [parseDate(data['dateTime']), _vIZones['IN_DEFAULT_ZONE_1'], _vIZones['IN_DEFAULT_ZONE_2'],
            _vIZones['IN_DEFAULT_ZONE_3'], _vIZones['BELOW_DEFAULT_ZONE_1']]


class TimeInHRZonesClass:
    @staticmethod
    def inserter(data: dict):
        _extract = timeInHRZonesSupport(data)
        return "INSERT INTO timeInHRZones VALUES ('" + _extract[0] + "', " \
               + str(_extract[1]) + ", " \
               + str(_extract[2]) + ", " \
               + str(_extract[3]) + ", " \
               + str(_extract[4]) + ")"

    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('timeInHRZones', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('timeInHRZones', data['dateTime'])

    @staticmethod
    def extractor(data: dict):
        return timeInHRZonesSupport(data)


class StepsClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('steps', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('steps', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return f"INSERT INTO steps VALUES ('" + parseDate(data['dateTime']) + "', " + str(data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


class LAMinutesClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('lightlyActiveMinutes', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('lightlyActiveMinutes', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO lightlyActiveMinutes VALUES ('" + parseDate(data['dateTime']) + "', " + str(
            data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


class MAMinutesClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('moderatelyActiveMinutes', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('moderatelyActiveMinutes', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO moderatelyActiveMinutes VALUES ('" + parseDate(data['dateTime']) + "', " + str(
            data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


class SMinutesClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('sedentaryMinutes', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('sedentaryMinutes', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO sedentaryMinutes VALUES ('" + parseDate(data['dateTime']) + "', " + str(data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


class VAMinutesClass:
    @staticmethod
    def tableCheck(date_min, date_max):
        return tableCheckGeneral('veryActiveMinutes', date_min, date_max)

    @staticmethod
    def recordCheck(data: dict):
        return recordCheckGeneral('veryActiveMinutes', data['dateTime'])

    @staticmethod
    def inserter(data: dict):
        return "INSERT INTO veryActiveMinutes VALUES ('" + parseDate(data['dateTime']) + "', " + str(
            data['value']) + ")"

    @staticmethod
    def extractor(data: dict):
        return _dateValueExtractor(data)


def databaseRecorder(fileName, _inJsonData, _class, _logFile):
    [_dtMin, _dtMax] = [_inJsonData[0]['dateTime'], _inJsonData[-1]['dateTime']]
    _tableCheck = _sqlConnection.execute(_class.tableCheck(_dtMin, _dtMax)).fetchall()
    _timeDelta = timeDelta(startTime)
    if len(_tableCheck) == 2:
        sys.stdout.write(f"\r{_timeDelta}::FileCount {_fileTrack}::{mD['m8']}::{fileName}")
        time.sleep(0)
    if len(_tableCheck) < 2:
        _rowTrack = 0
        for record in _inJsonData:
            line = _class.extractor(record)
            _timeDelta = timeDelta(startTime)
            _sqlResults = _sqlConnection.execute(_class.recordCheck(record)).fetchall()
            _messagePrefix = f"{mD['m0']} {_timeDelta}::FileCount {_fileTrack}::{mD['m2']} {_rowTrack}"
            if len(_sqlResults) == 0:
                sys.stdout.write(f"\r{_messagePrefix}::{mD['m3']}::{fileName}")
                _sqlConnection.cursor().execute(_class.inserter(record))
            elif len(_sqlResults) == 1:
                sys.stdout.write(f"\r{_messagePrefix}::{mD['m5']}::file {fileName}")
            elif len(_sqlResults) > 1:
                sys.stdout.write(f"\r{_messagePrefix}::{mD['m4']}")
                _logFile.write(f"{mD['m4']}:: {line[0]}.")
            _rowTrack += 1
        _sqlConnection.commit()
        inJsonFile.close()
    if len(_tableCheck) > 2:
        sys.stdout.write(f"\rSeems like there is an issue with this file. {mD['m6']}")
        _logFile.write(f"{mD['m7']}::{fileName}")


mD = {'m0': 'TimeElapsed', 'm1': 'Processing file#', 'm2': 'Processing line number',
      'm3': 'record not found in the database, now inserting',
      'm4': 'suspicious record found, ',
      'm5': 'record found in the database, moving on',
      'm6': 'printing info to a logfile',
      'm7': 'Duplicate records found',
      'm8': 'This file has already been processed, moving on'
      }

_fileTrack = 1

metricType = {'altitude-': 9, 'calories-': 9, 'distance-': 9, 'heart_rate-': 11}
exportDirectory = "D:\\Programming\\_databases\\"

with open(f"{exportDirectory}{'altitude'}.txt", 'w+') as altitudeLF, \
        open(f"{exportDirectory}{'heart_rate'}.txt", 'w+') as heartRateLF, \
        open(f"{exportDirectory}{'distance'}.txt", 'w+') as distanceLF, \
        open(f"{exportDirectory}{'calories'}.txt", 'w+') as caloriesLF, \
        open(f"{exportDirectory}{'sleep'}.txt", 'w+') as stepsLF, \
        open(f"{exportDirectory}{'lightlyActiveMinutes'}.txt", 'w+') as lAMinutesLF, \
        open(f"{exportDirectory}{'moderatelyActiveMinutes'}.txt", 'w+') as mAMinutesLF, \
        open(f"{exportDirectory}{'moderatelyActiveMinutes'}.txt", 'w+') as sMinutesLF, \
        open(f"{exportDirectory}{'timeInHRZones'}.txt", 'w+') as timeInHRZonesLF, \
        open(f"{exportDirectory}{'veryActiveMinutes'}.txt", 'w+') as vAMLogFile:
    for path, item, files in os.walk(directory):
        for file in files:
            with open(path + "\\" + file) as inJsonFile:
                if len(file) > 9 and file[-4:] == 'json':
                    # if 'minutes' in file:
                    inJsonData = json.load(inJsonFile)
                    if file[:9] == 'altitude-':
                        databaseRecorder(file, inJsonData, AltitudeClass(), altitudeLF)
                    elif file[:9] == 'calories-':
                        databaseRecorder(file, inJsonData, CaloriesClass(), caloriesLF)
                    elif file[:9] == 'distance-':
                        databaseRecorder(file, inJsonData, DistanceClass(), distanceLF)
                    elif file[:11] == 'heart_rate-':
                        databaseRecorder(file, inJsonData, HeartRateClass(), heartRateLF)
                        pass
                    elif file[:25] == 'time_in_heart_rate_zones-':
                        pass
                        databaseRecorder(file, inJsonData, TimeInHRZonesClass(), timeInHRZonesLF)
                    elif file[:6] == 'steps-':
                        databaseRecorder(file, inJsonData, StepsClass(), stepsLF)
                    elif file[:23] == 'lightly_active_minutes-':
                        databaseRecorder(file, inJsonData, LAMinutesClass(), lAMinutesLF)
                    elif file[:26] == 'moderately_active_minutes-':
                        databaseRecorder(file, inJsonData, MAMinutesClass(), mAMinutesLF)
                    elif file[:18] == 'sedentary_minutes-':
                        databaseRecorder(file, inJsonData, SMinutesClass(), sMinutesLF)
                    elif file[:20] == 'very_active_minutes-':
                        databaseRecorder(file, inJsonData, VAMinutesClass(), vAMLogFile)
                    else:
                        pass
                    _fileTrack += 1
                else:
                    pass

print("\nDatabase import complete")
