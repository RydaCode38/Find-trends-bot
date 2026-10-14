# Find-trends-bot
English DescriptionThis is a complete, ready-to-run Python script for a simple surface-level trend finder.What the script does:Fetches the current Daily Trending Searches from Google Trends (worldwide + optionally Germany/Austria/Switzerland)
Displays the top trends in a clean list
Optionally shows Related Queries and Rising Searches for any keyword you enter
No API keys required (uses the free pytrends library)
Runs locally on your machine

Installation (one-time)bash

pip install pytrends pandas

How to use itSave the script as trendfinder.py
Open a terminal and run:bash

python trendfinder.py

You immediately get the current top trends
Optionally enter a keyword afterwards to see related and rising searches

CustomizationChange region: set GEO = "AT", GEO = "CH", or GEO = "" (worldwide)
Change number of trends shown: adjust MAX_TRENDS

