def user_register(self):
        try:
            user_name=input("Enter your full name : ")
            phone_no=int(input("Enter your 10 digit phone number : "))
            email=input("Enter your email id : ")
            password=input("Enter your password : ")
            address=input("Enter your address with area PIN code ")
            self.user_details={"User Name":user_name,"Phone No.":phone_no,"Email_ID":email,"Password":password,"Address":address}
            print("\n!! Your Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restro_name} Restaurant\n")
            print("User Details : ")
            for i in self.user_details:
                print(i, ":", self.user_details[i])        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")      
            
               
def user_login(self):
        try:
            print(f"Welcome TO {self.restro_name} Restaurant\n\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.user_details.values())!=0:                                                            #we can same as admin by using self.email..etc
                if email==self.user_details["Email_ID"] and pas==self.user_details["Password"]:      # we can make it either object level or local level inside def fun
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit")
                        z=input()
                        if z=="1":
                            self.place_order()
                        elif z=="2":
                            self.ordered_history()
                        elif z=="3":
                            self.update_details()
                        elif z=="4":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no User Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")  
            
            
def place_order(self):
        try:
            if len(self.food)!=0:
                print("list of Availabe Food Items :\n")
                menu=[]
                for items in self.food:
                    menu.append([self.food[items]["Name"], self.food[items]["Quantity"],self.food[items]["Price"]]) 
                for i in range(len(menu)):
                    print(i+1,".",menu[i])
                while True:
                    print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                    x=input()
                    if x=="1":
                        print("Enter the Food number You want to ordered separated by comma")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                self.ordered_item.append(menu[z-1])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                        print("\nList of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x=="2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
            else:
                print("\n!! Sorry! No Food Items are available Now !!\n")
                        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")     
                
                
def ordered_history(self):
        print("\nList of Previous ordered : \n")
        for i in self.ordered_item:
            print(i)
            
            
def update_details(self):
        try:
            while True:
                print("Select Below Options to Update Your Profile Details\n")
                print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\n")
                x=input()
                if x=="1":
                    self.user_details["User Name"]=input("Enter your updated full name : ")
                    print("\n!! Detail Updated Successfully !!\n")
                elif x=="2":
                    self.user_details["Phone No."]=int(input("Enter your updated 10 digit phone number : "))
                    print("\n!! Detail Updated Successfully !!\n")      
                elif x=="3":
                    self.user_details["Email_ID"]=input("Enter your updated email id : ")
                    print("\n!! Detail Updated Successfully !!")
                    
                elif x=="4":
                    self.user_details["Password"]=input("Enter your updated password : ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="5":
                    self.user_details["Address"]=input("Enter your updated address with area PIN code ")
                    print("\n!! Detail Updated Successfully !!\n")
                    
                elif x=="6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")
                    
                if x in ["1","2","3",'4',"5"]:
                    for i in self.user_details:
                        print(i, ":",self.user_details[i])
                else:
                    print("\nPlease Enter correct Input\n")      
        except Exception as e:
         print("\n!! Please Provide Valid Inputs !!\n ")