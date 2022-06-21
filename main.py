class Parkinglot: #An instance of this class creates a Parking lot
  def __init__(self,n):
    #Capacity of parkinglot
    self.parkinglot_size=n
    
    #Creating Parking lot space for given size
    self.parkinglotarray = [0 for i in range(n)]  #I have considered 0th index as entry point

    #Dictionary where key is Slot number and value will be its corresponding Vehicle registration number and driver's age.
    self.Data_for_VNRandAGE_by_Slot_number={}
    
    #Dictionary where key is Age and value is list of all Vehicle registration number for drivers of given age
    self.Data_for_VRN_by_Age={}
    
    #Dictionary where key is Age and value is list of all Slot numbers for drivers of given age
    self.Data_for_Slot_numbers_by_Age={}  

    #Dictionary where key is Vehicle registration number and value is a Slot number (a single integer) for which given VNR car is parked.
    self.Data_for_Slot_number_by_VNR={}

    print("Created parking of " + str(n) +" slots")

    
    
    
  def getslotnumbers_by_age(self,age): #Method for finding list of all Slot numbers for drivers of given age
    if(age not in self.Data_for_Slot_numbers_by_Age):
      return ""
    ans=""
    for i in self.Data_for_Slot_numbers_by_Age[age]:
      ans+=str(i)+","
    return ans[:-1]
    
  def getvnr_by_age(self,age): #Method for finding list of all Vehicle registration numbers for drivers of given age
    if(age not in self.Data_for_VRN_by_Age):
      return ""
    ans=""
    for i in self.Data_for_VRN_by_Age[age]:
      ans+=i+","
    return ans[:-1]
    
  def getslotnumbers_by_vnr(self,vnr): #Method for finding Slot number for car of given Vehicle registration number
    if(vnr[:-1] not in self.Data_for_Slot_number_by_VNR):
      return ""
    return self.Data_for_Slot_number_by_VNR[vnr[:-1]]

  
  def availableslot(self): # Method to find nearest available slot from entry as I have considered 0th index as entry point
    for i in range(len(self.parkinglotarray)):
      if(self.parkinglotarray[i]==0):
        return i
    return -1
    
  def Park(self,vnr,age): #Method for Park
    
    available_slotnumber=self.availableslot()
    if(available_slotnumber==-1):
      return "Parking Full. Not Executing this command.....Moving to Next Command"
       
    self.parkinglotarray[available_slotnumber]=1
    
    self.Data_for_VNRandAGE_by_Slot_number[available_slotnumber]=[vnr,age]
    
    if(age in self.Data_for_VRN_by_Age):
      self.Data_for_VRN_by_Age[age].append(vnr)
    else:
      self.Data_for_VRN_by_Age[age]=[]
      self.Data_for_VRN_by_Age[age].append(vnr)

  
    self.Data_for_Slot_number_by_VNR[vnr]=available_slotnumber+1

    
    if(age in self.Data_for_Slot_numbers_by_Age):
      self.Data_for_Slot_numbers_by_Age[age].append(available_slotnumber+1)
    else:
      self.Data_for_Slot_numbers_by_Age[age]=[]
      self.Data_for_Slot_numbers_by_Age[age].append(available_slotnumber+1)
    return 'Car with vehicle registration number "'+vnr+'" has been parked at slot number '+str(available_slotnumber+1)

    
    
    
  def Leave(self,slotnumber): #Method for Leave
    if(self.parkinglotarray[slotnumber-1]==0):
      return 'Already Empty....So not valid situation'
    self.parkinglotarray[slotnumber-1]=0
    
    vnr,age=self.Data_for_VNRandAGE_by_Slot_number[slotnumber-1]
    del self.Data_for_VNRandAGE_by_Slot_number[slotnumber-1]  #as it is a single value..so directly deleting it
    
    del self.Data_for_Slot_number_by_VNR[vnr]

    self.Data_for_VRN_by_Age[age].remove(vnr)
    if(len(self.Data_for_VRN_by_Age[age])==0):
      del self.Data_for_VRN_by_Age[age]   # If there are no vnr with given age then deleting the age entry also
    
    self.Data_for_Slot_numbers_by_Age[age].remove(slotnumber)
    if(len(self.Data_for_Slot_numbers_by_Age[age])==0):
      del self.Data_for_Slot_numbers_by_Age[age]    # If there are no slotnumbers with given age then deleting the age entry also
    return 'Slot number '+str(slotnumber)+' vacated, the car with vehicle registration number "'+vnr+'" left the space, the driver of the car was of age '+str(age)
    

    
    
    

class Commands: # Class for checking which type of command is entered...
  def __init__(self):
    self.InitialCommands={
      "Create_parking_lot":1,
      "Park":2,
      "Slot_numbers_for_driver_of_age":3,
      "Slot_number_for_car_with_number":4,
      "Leave":5,
      "Vehicle_registration_number_for_driver_of_age":6}

  def type(self,command): #returns type of command
    return self.InitialCommands[command[0]]


  
  # def check_firstword_of_command(split_command):
  #   while(command_length_check(split_command)!=True or split_command[0] not in self.InitialCommands):
  #     print("This Command is incorrect. Please re-enter the command from command line Now....")
  #     command=input()
  #     split_command=command.split(" ")  
  #   return split_command
    
  # def command_length_check(split_command):
  #   if(len(split_command)==0 or len(split_command)==1 or len(split_command)==3 or len(split_command)>=5):
  #     print("Either No command provided or invalid command length on this line....")
  #     return False
  #   else:
  #     return True

      
  # def check(self,command):
  #   split_command=command.split(" ")
  #   split_command=check_command_length_and_firstword(split_command)
  #   #Now After this, we have command length either 2 or 4 with correct 1st word in that command....................Now we have to check for 3rd word if length of command is 4...else we are returning true
  #   if(len(split_command)==4):
  #     if(split_command[2]="driver_age"):
  #       return True
  #     else:
  #       print("Rewrite the command in command line as the third word in that command is wrong")
  #       command=input()
  #       self.check(command)
  #   return True
  
   
        
        
        
      
      
    
    
    


Commands=Commands()

file1 = open('input.txt', 'r')
Lines = file1.readlines()

for line in Lines:
  cc=line.split(" ")
  
  type=Commands.type(cc)
  
  if(type==1):
    Parking=Parkinglot(int(cc[1]))
  elif(type==2):
    print(Parking.Park(cc[1],int(cc[3])))
  elif(type==3):
    print(Parking.getslotnumbers_by_age(int(cc[1])))
  elif(type==4):
    print(Parking.getslotnumbers_by_vnr(str(cc[1])))
  elif(type==5):
    print(Parking.Leave(int(cc[1])))
  elif(type==6):
    print(Parking.getvnr_by_age(int(cc[1])))
  else:
    print("Error in Command")

