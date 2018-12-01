
class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        self.address[0]
        self.address[1]
        self.address[2]
        self.address[3]
        
        
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount):
        self.balance+=amount
        
    def withdraw(self, amount):
        #ToDo
        self.balance-=amount
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Account No: %s" %self.account_no)
        print("Address: %s" %self.address[0])
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3])
        print(" ")
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                amount=float(input("\n Please enter amount to be deposited: "))
                self.deposit(amount)
                self.print_balance()
            
            elif choice == 2:
                #ToDo
                amount  = float(input("\n how much do you wish to withdraw: "))
                self.withdraw(amount)
                self.print_balance()
            elif choice == 3:
                #STEP A.4.4
                self.print_balance()
                
            elif choice == 4:
                #STEP A.4.2
                choice = input('current forname %s. Change? (Y/N) >>' %self.fname)
                if choice == 'Y':
                    new_name = input('Enter New Forename >> ')
                    self.update_first_name(new_name)
                    if choice == 'N' :
                        return self.fname
                choice == input('current surname %s. Change? (Y/N) >>' %self.lname)
                if choice == 'Y':
                    new_name = input('Enter new Surname >> ')
                    self.update_last_name(new_name)
                    print('Name changed! New name on system: %s %s' %(self.fname, self.lname ))
                    if choice == 'N' :
                        return self.lname
                  
            elif choice == 5:  #problem starts here
                #ToDo
        
                choice = input('Current address Line 1: %s. Change? (Y/N) >> ' %self.address[0])
                if choice == 'Y':
                    line_0 = input('Please enter new Line 1 >> ')
                    self.update_address(line_0)
                    if choice == 'N' :
                        return self.addr
                    
                    
                    
                    
             
                else:
                    tempadd =[] 
                    tempadd.append(self.address[1])
                choice = input('Current address Line 2: %s. Change? (Y/N) >> ' %self.address[1])
                if choice == 'Y':
                    new_line = input('Please enter new Line 2 >> ')
                    tempadd.append(new_line)
                else:
                    tempadd.append(self.address[2])
                choice = input('Current address Line 3: %s. Change? (Y/N) >> ' %self.address[2])
                if choice == 'Y':
                    new_line = input('Please enter new Line 3 >> ')
                    tempadd.append(new_line)
                else:
                    tempadd.append(self.address[3])
                    self.update_address(new_line)
                    
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")
