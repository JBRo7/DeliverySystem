
#Author Justin Brown
# ID: 000950513

import csv
import datetime


from HashTable import HashTable
from Package import Package
from Truck import Truck

#pull the hash
myHash = HashTable()

distanceList =[]

#load the trucks
truck1 = Truck(1, [37, 13, 39, 16, 19, 15, 14, 34, 20, 21, 29, 30, 8, 7])
truck2 = Truck(2, [6, 3, 25, 26, 5, 18, 36, 38, 4, 40, 31, 32, 1])
truck3 = Truck(3, [10, 11, 12, 17, 22, 23, 24, 27, 35, 2, 33, 9, 28])





#Run time complexity O(n^3) and Space complexity O(n^2)


#loads the distances from the distance.csv file
# Run time complexity O(n)
def loadDistanceFile(filename):
    distance_Array = []
    with open(filename, 'r') as Dist:
        csvReader = csv.reader(Dist)
        for row in csvReader:
            distance_Array.append(row)
    return distance_Array

#loads the addresses from the address.csv file
# Run time complexity O(n)
def loadAddressFile(filename):
    address_Array = []
    with open(filename, 'r') as Addr:
        csvReader = csv.reader(Addr)
        for row in csvReader:
            address_Array.append(row)
    return address_Array

#assignes values to the columns
# Run time complexity O(n)
def readPackageInfo(filename, myHash):
   with open(filename) as pkgData:
       packageInfo = csv.reader(pkgData, delimiter=',')
       for row in packageInfo:
           pID = int(row[0])
           pAddress = row[1]
           pCity = row[2]
           pState = row[3]
           pZip = row[4]
           pDeadline = row[5]
           pWeight = row[6]
           pSpecial_inst = row[7]
           pStatus = "Loaded"

           pkg = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pSpecial_inst, pStatus)

           myHash.insert(pID, pkg)

#relates the distance and address csv rows.
# Major Block O(n)
def correlateAddressDist(Address):
    for row in addressList:
        if Address in row[1]:
            return int(row[0])
    return -1

#Determines the distance between the addresses
# Major Block O(n)
def distanceBetweenAddresses(startAddress,endAddress):
    startIndex = correlateAddressDist(startAddress)
    endIndex = correlateAddressDist(endAddress)
    if startIndex == -1 or endIndex == -1:

        raise Exception()
        return -1
    dist= distanceList[startIndex][endIndex]
    if dist == '':
        dist = distanceList[endIndex][startIndex]

    return float(dist)


#finds the nearest neighbor algorithm
# Major Block O(n^2)
def getNextNearestPackage(truck, currentAddress):
    pkgID = -1
    shortestDistance = 100.0
    for package1 in truck.packageList:
        packageObject = myHash.search(package1)

        if packageObject.isNotDelivered():
            distance = distanceBetweenAddresses(currentAddress, packageObject.address)

            if distance != -1 and distance < shortestDistance:
                shortestDistance = distance
                pkgID = packageObject.ID
    return shortestDistance, pkgID


#delivers package using the nearest neighbor
# Major Block O(n^3)
def deliverPackagesForTruck(truck, currentTime):
    pkgID = 0
    currentAddress = addressList[0][1]
    currentMile = distanceList[0]
    avgSpeed = 18

    while pkgID != -1:
        distance, pkgID = getNextNearestPackage(truck, currentAddress)

        #update Package 9 address
        if pkgID == 9:
            myHash.updatePkg9(key= 0)

        # This marks the Package as delivered and collects the delivery distance
        if pkgID != -1:
            packageObject = myHash.search(pkgID)
            currentAddress = packageObject.address
            timeTraveled = distance/avgSpeed
            currentTime = currentTime + datetime.timedelta(hours=timeTraveled)
            packageObject.deliveryTime = currentTime
            packageObject.mileage = distance

#get total miles for each package delivered.
# Major Block O(n)
def getTotalMileage(truck):
    pkgID = 0
    currentMile = float(distanceList[0][0])

    for pkgID in truck.packageList:
        packageObject = myHash.search(pkgID)
        currentMile = currentMile + packageObject.mileage
    return currentMile

#loads the package, address, and distance
readPackageInfo('CSV_Files/Package.csv', myHash)
addressList = loadAddressFile('CSV_Files/Address.csv')
distanceList = loadDistanceFile('CSV_Files/Distance.csv')


#Pass the trucks and Times to start.
deliverPackagesForTruck(truck1, datetime.datetime(2022, 4, 4, 8, 0, 0))
deliverPackagesForTruck(truck2, datetime.datetime(2022, 4, 4, 9, 5, 0))
deliverPackagesForTruck(truck3, datetime.datetime(2022, 4, 4, 10, 20, 0))

#get total mileage
TruckMileage = getTotalMileage(truck1) + getTotalMileage(truck2) + getTotalMileage(truck3)

#user Interface:
# Major Block O(n)
isExit = True
while (isExit):
    print("Tracking App\n1. Get package information for a single package\n2. Get all package data information at a certain time\n3. Total Truck mileage\n4. Exit")

    userOption = input("Make a selection from the above choices (1, 2, 3, or 4): ")
    if userOption == "1":
        userPkgID = input("Enter a package ID (1-40): ")
        print(myHash.search(int(userPkgID)))

    #get user input for time. turn it into time.
    #return package status for each package.
    elif userOption == "2":
        inputTime = input("Enter time (example: HH:MM): ")
        timeTokens = inputTime.split(":")
        userInputTime = datetime.datetime(2022, 4, 4, int(timeTokens[0]), int(timeTokens[1]), 0)

        #trying to get the start time and pass start time,
        truck1StartTime = datetime.datetime(2022, 4, 4, 8, 0, 0)
        #truck2StartTime = datetime.datetime(2022, 4, 4, 9, 5, 0)
        #truck3StartTime = datetime.datetime(2022, 4, 4, 10, 20, 0)

        for i in range(1, 41):
            pkg = myHash.search(i)
            #print(pkg.PkgStatusUpdate(userInputTime, truck1StartTime))
            pkg.PkgStatusUpdate(userInputTime, truck1StartTime)
        # Print the total distance of the trucks
        print("Round trip distance for all trucks:", TruckMileage, "\n")
    #Print the total distance of the trucks
    elif userOption == "3":
        print("Round trip distance for all trucks:", TruckMileage, "\n")
    elif userOption == "4":
        isExit = False
    else:
        print("Please make a valid selection")

