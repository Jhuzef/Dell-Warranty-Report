#!/usr/bin/env python
import json

from Dell.Dell import Dell
from Credentials.Credentials import Credentials

__author__ = "Joseph L. Gonzales"
__email__ = "joseph.gonzales@konicaminolta.com"


def main():
    credentials = Credentials()
    dell = Dell(credentials)

    data = dell.getWarranty("HC2QM12")

    print(json.dumps(data))


if __name__ == "__main__":
    main()