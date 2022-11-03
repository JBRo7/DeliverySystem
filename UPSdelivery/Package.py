

class Package:


    def __init__(self, ID, address, city, state, zip, deadline, weight, special_inst, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_inst = special_inst
        self.status = status
        self.deliveryTime = None
        self.mileage = 0

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.special_inst, self.status, self.deliveryTime)

    #prints the status for the truck.
    #O(1)
    def PkgStatusUpdate(self, requestedTime, truckStartTime):
        calculatedStatus = "At Hub"

        #calculated status based on delivery time and requested time.

        #user input time is greater than the delivery time
        if requestedTime >= self.deliveryTime:
            pkgStatus = "Delivered"
            calculatedStatus = "Delivered"


        # user input time is greater than the truck start time
        # and the user input time is less than the delivery time
        elif self.deliveryTime > requestedTime > truckStartTime:
            pkgStatus = "In Route"
            #calculatedStatus ="In Route"
            # user input time is less than or equal to the truck start time
        elif requestedTime < truckStartTime:
            pkgStatus = calculatedStatus
            #calculatedStatus =calculatedStatus

        if pkgStatus == "In Route":
            print("Package ID:", self.ID, ", Package status:", pkgStatus, ", ETA:", self.deliveryTime, ", Deadline:", self.deadline, ", Address:", self.address, "\nCity:", self.city, ", State:", self.state, ", ZipCode:", self.zip, ", Weight:", self.weight, ", Special instructions:", self.special_inst)
        elif pkgStatus == "Delivered":
            print("Package ID:", self.ID, ", Package status:", pkgStatus, ", Delivery time:", self.deliveryTime, ", Deadline:", self.deadline, ", Address:", self.address, "\nCity:", self.city, ", State:", self.state, ", ZipCode:", self.zip, ", Weight:", self.weight, ", Special instructions:", self.special_inst)
        else:
            print("Package ID:", self.ID, ", Package status:", pkgStatus, ", ETA:", self.deliveryTime, ", Deadline:", self.deadline, ", Address:", self.address, "\nCity:", self.city, ", State:", self.state, ", ZipCode:", self.zip, ", Weight:", self.weight, ", Special instructions:", self.special_inst)


        #return "%d, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.special_inst, calculatedStatus, self.deliveryTime)
        #return "%d, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.special_inst, self.deliveryTime)

    def isDelivered(self):

        #need to add the delivery status change.
        return self.deliveryTime is not None

    def isNotDelivered(self):
        return not self.isDelivered()
