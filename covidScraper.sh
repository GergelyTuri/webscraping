#!/bin/sh
source /home/ubuntu/.virtualenvs/webscraping/bin/activate
cd /home/ubuntu/code/webscraping/
./covidScraper.py
deactivate
