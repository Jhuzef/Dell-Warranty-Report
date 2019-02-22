#!/usr/bin/env python

import requests


class Dell:
    def __init__(self, credentials):
        self.request = None
        self.key = credentials.key

    def getWarranty(self, tag):

        try:
            request = requests.get("https://api.dell.com/support/assetinfo/v4/getassetwarranty/{}?apikey={}".format(tag, self.key))
            self.request = request.json()

        except:
            print("Error Connecting to the Dell API.")
            exit()

        return self.request
