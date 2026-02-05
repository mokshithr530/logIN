# logIN– CLI Network Traffic Logger

## About

NetLog is a command-line based networking project built using Python.  
It monitors real-time network connections on the system and helps analyze which processes are using the internet.

## Why I Built This

I created this project because I am interested in networking and wanted to understand how network activity works at system level.  
This project helped me learn how Python can be used to track active connections and analyze them in a simple way.

## Features

- View active network connections  
- See which process is using the network  
- Save network activity to text log files  
- Export connection data to CSV  
- Filter connections by process name  
- Live monitoring mode  

## Technologies Used

- Python  
- psutil library  
- CSV module  
- OS and system networking  

## How to Run

1. Install required library:
:import psutil
import time
import datetime
import os
import csv
2. Run the program: python log.py
3. Use the menu to select different options.

## Learning Outcome

- Understood process-level networking  
- Learned how sockets and connections work  
- Practiced Python file handling  
- Built a real-world CLI tool  

## Future Improvements

- Add protocol filtering  
- Show data usage statistics  
