#!/usr/bin/env python

import requests
import datetime
import re


class Dell:
    def __init__(self, credentials):
        self.request = None
        self.key = credentials.key

    def getWarranty(self, tag):

        tag = re.sub('[^A-Za-z0-9]+', '', tag)

        try:
            request = requests.get("https://api.dell.com/support/assetinfo/v4/getassetwarranty/{}?apikey={}".format(tag, self.key))
            self.request = request.json()

        except:
            print("Error Connecting to the Dell API.")
            exit()

        return self.jsonToList(self.request)

    def jsonToList(self, json):

        if len(json["AssetWarrantyResponse"]) == 0:
            return [json["InvalidBILAssets"]['BadAssets'][0], 'invalid', 'invalid', 'invalid', 'invalid', 'invalid', 'invalid']

        list = []
        list.append(json["AssetWarrantyResponse"][0]["AssetHeaderData"]["ServiceTag"])
        list.append(json["AssetWarrantyResponse"][0]["ProductHeaderData"]["SystemDescription"])

        try:
            list.append(json["AssetWarrantyResponse"][0]["AssetHeaderData"]["ShipDate"][:10])
        except:
            list.append("N/A")

        warranty = self.warrantyDate(json["AssetWarrantyResponse"][0]["AssetEntitlementData"])

        # ProSupport
        list.append(str(warranty[0]))
        list.append(self.isExpired(warranty[0]))

        # Complete Care
        list.append(str(warranty[1]))
        list.append(self.isExpired(warranty[1]))

        return list

    # Returns the expiration date for ProSupport and CompleteCare in a list
    def warrantyDate(self, warranties):
        proSupport = []
        completeCare = []

        for warranty in warranties:
            if warranty["ServiceLevelDescription"] == "ProSupport":
                proSupport.append(warranty["EndDate"][:10])
            if warranty["ServiceLevelDescription"] == "Complete Care / Accidental Damage":
                completeCare.append(warranty["EndDate"][:10])

        for idx in range(len(proSupport)):
            proSupport[idx] = datetime.date(int(proSupport[idx][0:4]), int(proSupport[idx][5:7]),
                                                int(proSupport[idx][8:10]))
        if len(proSupport) == 0:
            proSupport.append("N/A")

        for idx in range(len(completeCare)):
            completeCare[idx] = datetime.date(int(completeCare[idx][0:4]), int(completeCare[idx][5:7]),
                                                  int(completeCare[idx][8:10]))
        if len(completeCare) == 0:
            completeCare.append("N/A")

        return [sorted(proSupport)[-1], sorted(completeCare)[-1]]

    def isExpired(self, date):

        if date == "N/A":
            return "N/A"

        today = datetime.date.today()

        if today > date:
            return "Expired"
        else:
            return "Active"
