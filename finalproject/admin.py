class Restaurant:
    
    def _init_(self, name):
        self.restro_name=name
        self.food={}
        self.food_ID=len(self.food)+1
        self.admin_details={}
        self.user_details={}
        self.ordered_item=[]

    def admin_register(self):
        try:
            self.admin_email=input("Enter your email id : ")
            self.admin_pass=input("Enter your password : ")
            self.admin_details={"Email_ID":self.admin_email,"Password":self.admin_pass}
            print("\n!! Admin Account is Created Successfully !!\n")
            print(f"Welcome TO {self.restro_name} Restaurant\n")
            print("Admin Details : ")
            for i in self.admin_details:
                print(i, ":", self.admin_details[i])
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n ")
            
            
    def admin_login(self):
        try:
            print(f"Welcome TO {self.restro_name} Restaurant\n\n")
            email=input("Enter Your Email ID : ")
            pas=input("Enter Your Password : ")
            if len(self.admin_details.values())!=0:
                if email==self.admin_email and pas==self.admin_pass:
                    print("\n!! Login successfully !!")
                    while True:
                        print("\nEnter the Below Options\n")
                        print("1. Add Food Item \n2. Edit Food Item\n3. View Food Item\n4. Delete Food Item\n5. Exit")
                        z=input()
                        if z=="1":
                            self.add_food_item()
                        elif z=="2":
                            self.edit_food_item()
                        elif z=="3":
                            self.view_food_item()
                        elif z=="4":
                            self.delete_food_item()
                        elif z=="5":
                            break
                        else:
                            print("invalid Number")
                else:
                    print("\n!! Incorrect Email or Password!!\n")
            else:
                print("\n! There is no Admin Account with this Email ID !\n\n!! Please Creat Your Account First!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")
            
        
    def add_food_item(self):
        try:
            name=input("Enter the food name : ")
            quantity=float(input("Enter the quantity in values only : "))
            price=float(input("Enter the price in Rs only : "))
            discount=float(input("Enter the discount in Rs only : "))
            stock=float(input("Enter the available stock in values only : "))
            food_item={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
            self.food_ID=len(self.food)+1
            self.food[self.food_ID]=food_item
            print("\n!! Food Item added successfully !!\n")
            print("Newly Added items :", self.food,"\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")
        
        
    def edit_food_item(self):
        try:
            x=int(input("Enter the Food ID you want to update : \n"))
            if x in self.food.keys():
                print("1. Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock \n")
                y= input("Enter the number only : ")
                if y=="1":
                    self.food[x]["Name"]=input("Updated Food name : ")
                    print("\n!! Successfully Updated !!\n")
                elif y=="2":
                    self.food[x]["Quantity"]=float(input("Updated Quantity in values only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="3":
                    self.food[x]["Price"]=float(input("Updated Price in Rs only : "))
                    print("\n!! Successfully Updated !!\n")
                elif y=="4":
                    self.food[x]["Discount"]=float(input("Updated Discount in Rs only : "))
                    print("\n!! successfully Updated !!\n")
                elif y=="5":
                    self.food[x]["Stock"]=float(input("Updated Stock in values only : "))
                    print("\n!! Successfully Updated !!\n")
                else:
                    print("!! Sorry Invalid Number !!\n")
            else:
                print("\n!! Incorrect Food ID !!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")  
            
            
    def view_food_item(self):
        print("List of Food Items : \n")
        if len(self.food)!=0:    
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("!! Sorry No Food Items is Added !!\n")
            

    def delete_food_item(self):
        try:
            print("!! Warning !!\nFood Item will Delete Permanently\n")
            print("Enter the Food ID ")
            x=int(input())
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List\n",self.food)
            else:
                print("!! Incorrect Food ID!!\n")
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")    
try:
    def main():
        obj=Restaurant("NIROB")
        print(f"!!  Welcome To {obj.restro_name} Restaurant  !!\n")
        print("!!----------------------------------------------------------")
        print("\nHellow Pratyush sir and Ritesh Sir Thank you for the Support\
        \nI have made 'My First Project @ PYTHON in my Life' :) yeeee woohhh\
        \nSir ! What you want to eat in my Restro ? Its a treat from my side :)")
        print("\n-----------------------------------------------------------!!\n")
        
        while True:
            print("1. Admin\n2. User\n3. Exit\n")
            x=input()
            if x=="1":
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.admin_register()
                    elif y=="2":
                        obj.admin_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")
                    
            elif x=="2":
                while True:
                    print("\nEnter the Below Options\n")
                    print("1. Register\n2. Login\n3. Exit\n")
                    y=input()
                    if y=="1":
                        obj.user_register()
                    elif y=="2":
                        obj.user_login()           
                    elif y=="3":
                        break
                    else:
                        print("\nInvalid Number ")        
            elif x=="3":
                break
            else:
                print("Invalid Number")
except Exception as e:
    print("Something went wrong please give input carefully")
            
        
        # calling the main function 
        
if __name__=='main_':
    main()

print("THANK YOU SIR")