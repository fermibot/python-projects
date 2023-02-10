import glob
import sys
import re
import datetime
import csv


def yearReplace(dateString: str) -> str:
    if dateString.split('\t')[0].__len__() != 10:
        time = re.findall('..:..:..', dateString)[0]
        year = ('20' + re.findall('/.. ', dateString)[0][1:]).strip(' ') + '-'
        return year + dateString.replace('/18 ', ' ').replace('/19 ', ' ').replace('/', '-').replace(time, time + '')


tsvDirectory = "D:\\Programming\\_databases\\fitbitDateReformatting\\"


def reformatAllFiles():
    fileTrack = 1
    for file in glob.glob(tsvDirectory + "main_*.csv"):
        if True:
            with open(file, newline='') as csvInFile, \
                    open(file.replace('main', 'reformatted'), mode='w', newline='') as csvOutFile:
                csvReader = csv.reader(csvInFile, delimiter=',')
                csvWriter = csv.writer(csvOutFile)
                rowTrack = 1
                for row in csvReader:
                    row[0] = parseDate(row[0])
                    if row[0] is not None:
                        csvWriter.writerow(row)
                    rowTrack += 1
                    sys.stdout.write(f"\rNow formatting {file}:: File# {fileTrack} :: Row# {rowTrack}")
        fileTrack += 1


def parseDate(dateString: str) -> str:
    try:
        return datetime.datetime.strptime(dateString, '%m/%d/%y %H:%M:%S')
    except ValueError:
        return None


if __name__ == '__main__':
    # print(parseDate('09/21/18 00:00:00'))
    reformatAllFiles()
