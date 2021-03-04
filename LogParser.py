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

    #Open month log files
    janFile = open('Jan.txt', 'w')
    febFile = open('Feb.txt', 'w')
    marFile = open('Mar.txt', 'w')
    aprFile = open('Apr.txt', 'w')
    mayFile = open('May.txt', 'w')
    junFile = open('Jun.txt', 'w')
    julFile = open('Jul.txt', 'w')
    augFile = open('Aug.txt', 'w')
    sepFile = open('Sep.txt', 'w')
    octFile = open('Oct.txt', 'w')
    novFile = open('Nov.txt', 'w')
    decFile = open('Dec.txt', 'w')

    janCount = 0
    febCount = 0
    marCount = 0
    aprCount = 0
    mayCount = 0
    junCount = 0
    julCount = 0
    augCount = 0
    sepCount = 0
    octCount = 0
    novCount = 0
    decCount = 0

    # Determine total requests from the last year
    # Determine total requests from the entire time period of the log
    last_year_requests = 0
    total_number_requests = 0
    four_hundred_codes = 0
    three_hundred_codes = 0

    # Create things list
    things = {}

    for line in logFile:
        total_number_requests += 1
        if "/1995:" in line:
            last_year_requests += 1

        # Finds file name line by line
        if re.search('GET (.*) HTTP', line) != None:
            filename = re.search('GET (.*) HTTP', line).group(1)
            if filename in things:
                things[filename] += 1
            else:
                things[filename] = 1

        # finds & counts 4xx status codes
        if re.search('\" 4[0-9]{2}', line) != None:
            four_hundred_codes += 1
        # finds & 3xx status codes
        elif re.search('\" 3[0-9]{2}', line) != None:
            three_hundred_codes += 1          
            
        #Get month
        if re.search('\d\d\/(.*)\/\d\d\d\d', line) != None:
            month = re.search('\d\d\/(.*)\/\d\d\d\d', line).group(1)
            if month == 'Jan':
                janFile.write(line)
                janCount += 1
            elif month == 'Feb':
                febFile.write(line)
                febCount += 1
            elif month == 'Mar':
                marFile.write(line)
                marCount += 1
            elif month == 'Apr':
                aprFile.write(line)
                aprCount += 1
            elif month == 'May':
                mayFile.write(line)
                mayCount += 1
            elif month == 'Jun':
                junFile.write(line)
                junCount += 1
            elif month == 'Jul':
                julFile.write(line)
                julCount += 1
            elif month == 'Aug':
                augFile.write(line)
                augCount += 1
            elif month == 'Sep':
                sepFile.write(line)
                sepCount += 1
            elif month == 'Oct':
                octFile.write(line)
                octCount += 1
            elif month == 'Nov':
                novFile.write(line)
                novCount += 1
            elif month == 'Dec':
                decFile.write(line)
                decCount += 1  
                
         #get day
            if weekday == 0:
	            mon += 1

            elif weekday == 1:
	            tue += 1
	
            elif weekday == 2:
            	wed += 1
	
            elif weekday == 3:
	            thur += 1
	
            elif weekday == 4:
	            fri += 1
	
            elif weekday == 5:
	            sat += 1
	
            elif weekday == 6:
	            sun += 1
 

    # Close the log file when we are done with it
    logFile.close()
    
    # calculates percentage of 3xx and 4xx codes 
    four_hundred_code_percent = (four_hundred_codes / total_number_requests) * 100
    three_hundred_code_percent = (three_hundred_codes / total_number_requests) * 100
    
    # Display the statitics determined above to the console
    print("Total number of requests made last year: {0}".format(last_year_requests))
    print("Total number of requests made in the whole time period: {0}".format(total_number_requests))

    print("Percentage of requests not successful (4xx codes): {0:.3f}%".format(four_hundred_code_percent))
    print("Percentage of requests redirected elsewhere (3xx codes): {0:.3f}%".format(three_hundred_code_percent))

    print("\n\n")
    print("Number of requests in January: {0}".format(janCount))
    print("Number of requests in February: {0}".format(febCount))
    print("Number of requests in March: {0}".format(marCount))
    print("Number of requests in April: {0}".format(aprCount))
    print("Number of requests in May: {0}".format(mayCount))
    print("Number of requests in June: {0}".format(junCount))
    print("Number of requests in July: {0}".format(julCount))
    print("Number of requests in August: {0}".format(augCount))
    print("Number of requests in September: {0}".format(sepCount))
    print("Number of requests in October: {0}".format(octCount))
    print("Number of requests in November: {0}".format(novCount))
    print("Number of requests in December: {0}".format(decCount))

    #prints weekday
    print("Number of requests on a Monday: {0}".format(monCount)
    print("Number of requests on a Tuesday: {0}".format(tueCount)
    print("Number of requests on a Wednesday: {0}".format(wedCount)
    print("Number of requests on a Thursday: {0}".format(thuCount)
    print("Number of requests on a Friday: {0}".format(friCount)
    print("Number of requests on a Saturday: {0}".format(satCount)
    print("Number of requests on a Sunday: {0}".format(sunCount)
    
   #Prints most and least requested file
    print("Most requested file:", max(things, key=things.get))
    print("Least requested file:", min(things, key=things.get))


    
if __name__ == "__main__":
    main()
