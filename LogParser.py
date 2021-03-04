import urllib.request
import os.path
import re

def main():
    # Check if logfile already exists locally
    if not os.path.exists("http_access_log"):
        try:
            # Download file from URL and save in current working directory
            urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "http_access_log")
        except:
            print("Error downloading http_access_log file")
            return 1
    try:
        # Open log file locally if already it already exists or if just downloaded
        logFile = open("http_access_log", "r")
    except:
        print("Error opening http_access_log file")
        return 1
        
    # Determine total requests from the last year
    # Determine total requests from the entire time period of the log
    last_year_requests = 0
    total_number_requests = 0
    four_hundred_codes = 0
    three_hundred_codes = 0
    
    for line in logFile:
        total_number_requests += 1
        if "/1995:" in line:
            last_year_requests += 1
        # finds & counts 4xx status codes
        elif re.search('\" 4[0-9]{2}', line) != None:
            four_hundred_codes += 1
        # finds & 3xx status codes
        elif re.search('\" 3[0-9]{2}', line) != None:
            three_hundred_codes += 1
     
    # calculates percentage of 3xx and 4xx codes 
    four_hundred_code_percent = (four_hundred_codes / total_number_requests) * 100
    three_hundred_code_percent = (three_hundred_codes / total_number_requests) * 100
    
    # Close the log file when we are done with it
    logFile.close()
    
    # Display the statitics determined above to the console
    print("Total number of requests made last year: {0}".format(last_year_requests))
    print("Total number of requests made in the whole time period: {0}".format(total_number_requests))
    print("Percentage of requests not successful (4xx codes): {0:.3f}%".format(four_hundred_code_percent))
    print("Percentage of requests redirected elsewhere (3xx codes): {0:.3f}%".format(three_hundred_code_percent))
    
if __name__ == "__main__":
    main()
