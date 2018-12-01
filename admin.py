
class Admin:
    
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
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
    
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights
    
    def account_menu(self):
        print ("\n Admin Options:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Update Admin Name")
        print ("2) Update Admin Address")
        print ("3) Update Admin Login ID")
        print ("4) Update Admin Login Password")
        print ("5) View Admin Details" )
        print ("6) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Admin account ID %s" %self.user_name)
        print("Admin Account Password %s" %self.password)
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
                    if choice == 'N, n' :
                        return self.lname
                
            elif choice == 2:
                #ToDo
                uname=input("\n Enter new Login ID for Admin: ")
                self.set_username(uname)
                
            elif choice == 3:
                #STEP A.4.4......
                uname=input("\n Enter new Login ID for Admin: ")
                self.set_username(uname)
                
            elif choice == 4:
                #STEP A.4.2
                password=input("\n Enter new Admin Login Password: ")
                self.update_password(password)
                
            elif choice == 5:
                self.print_details()
                
            elif choice == 6:
                loop = 0
        print ("\n Exit account operations")