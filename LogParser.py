import urllib.request
import os.path

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
    
    # Close the log file when we are done with it
    logFile.close()
    
    # Display the statitics determined above to the console
    print(f"Total number of requests made last year: {last_year_requests}")
    print(f"Total number of requests made in the whole time period: {total_number_requests}")
    
    
if __name__ == "__main__":
    main()
