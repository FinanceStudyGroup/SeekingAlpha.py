#!/usr/bin/python
# ------------------------------------------------------------------------------
# Seeking Alpha Launcher
# ------------------------------------------------------------------------------

# Import required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ------------------------------------------------------------------------------
Ticker = raw_input("Ticker: ")
# ------------------------------------------------------------------------------

driver = webdriver.Chrome()

# Link to the profile page
SeekingAlphaProfile = ("https://seekingalpha.com/symbol/"+Ticker+"/overview")

# Locate Seeking Alpha company profile page
driver.get(SeekingAlphaProfile)