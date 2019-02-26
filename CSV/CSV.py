#!/usr/bin/env python

import csv
import os


class CSV:

    def __init__(self):
        pass

    def parseCSV(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        return data

    def writeRecord(self, record, filename):

        headers = ['Service Tag', 'Model', 'Shipped Date', 'ProSupport Expiration Date', 'ProSupport Status',
                   'Complete Care Expiration Date', 'Complete Care Status']

        if os.path.exists(filename):
            with open(filename, 'a', newline='') as file:
                wr = csv.writer(file, dialect='excel')
                wr.writerow(record)
        else:
            with open(filename, 'w', newline='') as file:
                wr = csv.writer(file, dialect='excel')
                wr.writerow(headers)

            with open(filename, 'a', newline='') as file:
                wr = csv.writer(file, dialect='excel')
                wr.writerow(record)


