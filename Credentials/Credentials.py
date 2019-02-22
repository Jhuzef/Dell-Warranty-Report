#!/usr/bin/env python
from dotenv import load_dotenv
import os

class Credentials:
    def __init__(self):
        load_dotenv()
        self.key = None
        self.setCredentials()

    def setCredentials(self):
        self.key = os.getenv("API")
