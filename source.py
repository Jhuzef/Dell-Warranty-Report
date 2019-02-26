#!/usr/bin/env python

from Dell.Dell import Dell
from Credentials.Credentials import Credentials
from CSV.CSV import CSV

__author__ = "Joseph L. Gonzales"
__email__ = "joseph.gonzales@konicaminolta.com"


def main():
    credentials = Credentials()
    dell = Dell(credentials)
    csv = CSV()
    tagList = csv.parseCSV('test2.csv')

    for record in tagList:
        if record == "":
            continue

        data = dell.getWarranty(record[0])
        csv.writeRecord(data, 'output.csv')


if __name__ == "__main__":
    main()
