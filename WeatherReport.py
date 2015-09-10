/*
sample input:
03/09/2015,Bangalore,37,22
03/09/2015,Chennai,37,20
03/09/2015,Chennai,37,20
03/09/2015,Hyderabad,35,27
03/09/2015,Ooty,30,20
03/09/2015,Bangalore,37,22
05/09/2015,Ooty,29,21
03/09/2015,Chennai,37,20
03/09/2015,Chennai,37,20
04/09/2015,madurai,39,21
03/09/2014,Hyderabad,35,27
03/09/2015,Ooty,30,20
05/09/2015,Kodai,30,22
04/09/2015,Ooty,29,21
04/09/2015,Rajapalayam,34,24
*/
import time
FILE_PATH = "C:\Users\PV02594\Desktop\weathersample.txt"
display_list = []
class Weather(object):
 def __init__(self):
  self.readFile()
  self.sortdate()
  return
  
 def readFile(self):
  with open(FILE_PATH) as data_file:
   for line in data_file:
      display_list.append(line.strip().split(','))
  return
 
 def sortdate(self):
  date = [row[0] for row in display_list]
  date.sort(key=lambda x: time.mktime(time.strptime(x,"%d/%m/%Y")))
  date = set(date)
  date = sorted(date)
  map_details = self.mapDetailsWithDate();
  for d in date:
   if d in map_details:
	self.weatheranlysis(map_details[d], d) 
   else: 
    print "some error occured"   
  return  
  
 def mapDetailsWithDate(self):
  map = {}
  for x in display_list:
   if x[0] not in map:
    map[x[0]] = [x[:]]
   else:
    map[x[0]].append(x[:])
  return map
  
 def weatheranlysis(self , weatherlist, weatherdate):
   high_temp = 0
   low_temp = 100
   high_temp_city = ""
   low_temp_city = ""
   print str(weatherdate)+":\n"
   for row in weatherlist:
    if int(row[2]) == high_temp  and  int(row[3]) == low_temp:
	 if high_temp_city.find(str(row[1])) == -1:high_temp_city += ","+row[1]
	 if low_temp_city.find(str(row[1])) == -1:low_temp_city += ","+row[1]
    elif int(row[2]) == high_temp:
	 if high_temp_city.find(str(row[1])) == -1:high_temp_city += ","+row[1]
	 if int(row[3]) < low_temp:
	  low_temp_city=row[1]
	  low_temp=int(row[3])
    elif int(row[3]) == low_temp:
	 if low_temp_city.find(str(row[1])) == -1:low_temp_city += ","+row[1]
	 if int(row[2]) > high_temp:
	  high_temp_city=row[1]
	  high_temp=int(row[2])
    elif int(row[2]) > high_temp and int(row[3]) < low_temp:
	 high_temp_city=row[1]
	 high_temp=int(row[2])
	 low_temp_city=row[1]
	 low_temp=int(row[3])	
    elif int(row[2]) > high_temp:
	 high_temp_city=row[1]
	 high_temp=int(row[2])
    elif int(row[3]) < low_temp:
	 low_temp_city=row[1]
	 low_temp=int(row[3])
   result = "\t\t"+high_temp_city+"\t"+str(high_temp)+"  High\n\t\t"+low_temp_city+"\t"+str(low_temp)+"  Low\n"
   print result
   return 
 
if __name__ == '__main__':
 w = Weather()
