from ..scraper import Scraper
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import os
import requests

class UTSCTimetable:

    host = 'http://www.utsc.utoronto.ca/~registrar/scheduling/timetable'

    @staticmethod
    def scrape(location='.'):
        Scraper.logger.info('UTSCTimetable initialized.')
        Scraper.logger.info('Not implemented.')
        raise NotImplementedError('This scraper has not been implemented yet.')
        Scraper.logger.info('UTSCTimetable completed.')
