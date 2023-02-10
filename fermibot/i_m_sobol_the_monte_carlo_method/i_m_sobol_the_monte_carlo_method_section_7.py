from functions.random_functions import *
from functions.monitoring import *
import csv


def run():
    for t in range(0, 1000):
        _filePath = "D:\Mathematica Files 4K\probability_problems\i_m_sobol_the_monte_carlo_method" \
                    "\i_m_sobol_the_monte_carlo_method_section_7"
        _exportFileName = _filePath + "\\i_m_sobol_the_monte_carlo_method_section_7_temp_" + str(t) + ".csv"

        TimeTagMessage('Opening file ' + _exportFileName)
        __file = open(_exportFileName, 'w')
        TimeTagMessage('Opening writer object')
        __writer = writer = csv.writer(__file, delimiter=',')
        TimeTagMessage('Writing rows to the file')

        for i in range(0, 1000):
            _seed = RandomReal(0, 1)
            _seedList = [_seed]
            while 0 <= _seed <= 2 and _seedList.__len__() <= 10:
                _seed += RandomReal(-1, 1)
                _seedList.append(_seed)
            writer.writerow(_seedList)
            if (i + 1) % 1000 == 0:
                TimeTagMessage("\t\tWriting row # " + str(i + 1) + " to the file")

        TimeTagMessage('Closing the file ' + _exportFileName)
        __file.close()


if __name__ == '__main__':
    run()
