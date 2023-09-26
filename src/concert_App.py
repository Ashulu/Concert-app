from mimetypes import init
import json

class concert_App():

    def __init__(self) -> None:
         self.n_row = 20
         self.n_col = 26
         self.seating = []
    def prettyJson(self, jsonString):
        """
        Func: preattyJson
        Desc: turns json into pretty printed json
        """

        parsed = json.loads(jsonString)
        result = json.dumps(parsed,indent = 4, sort_keys=True)

        return result
    

    def write_json(self, data, filename = r"/Users/ashis/Documents/GitHub/Concert-app/.vscode/customers.json"):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data.append(data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)



    def menu(self):
        print("[b] buy")
        print("[v] view seating")
        print("[s] Search for a customer by name and display the tickets purchased")
        print("[d] Display all purchases made and total amount of income")
        print("[q] to quit")

    def create_Seating(self):
        # available seat
        available_seat = '.'
        # create some available seating
        for r in range(self.n_row):
            row = []
            for c in range(self.n_col):
                row.append(available_seat)
            self.seating.append(row)

            
    
    def print_Seating(self):
        print("\t" + "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
        for r in range(0,self.n_row):
            print(r+1, end="\t")
            for c in range(0,self.n_col):
                print(self.seating[r][c], end=" ")
            if(r<5):
                    print(" Front   $80")
            elif(r<11):
                    print(" Middle   $50")
            else:
                    print(" Back   $25")
        print()


    def buy(self):
        seat_list = []
        num_Tickets = int(input("How many in your party?: "))
        start = input("First seat:")
        split_word = list(start)
        row = int(split_word[0])-1
        if(len(split_word) == 3):
            row = int(split_word[0]+split_word[1])-1
        col = ord(split_word[1])-97
        seat_Type = "Front"
        if(row > 4):
            seat_Type = "Middle"
        elif(row > 11):
            seat_Type = "Back"

        #checks if seats are available
        if(self.seating[row][col] == '.' and self.seating[row][col+num_Tickets] != 'e' and self.seating[row][col+num_Tickets] != 'X'):
            print(str(num_Tickets)+" are available to buy starting from ("+str(row+1)+","+chr(col+97)+")")
            for i in range(col, col+num_Tickets):
                seat_list.append(str(row+1)+chr(i+97))
            #print(seat_list)
            for i in range(0,num_Tickets):
                self.seating[row][col+i] = "X"
            if(row >0 and row<19):
                if(col>1 and col<25):
                    for i in range(-2,num_Tickets+2):
                        self.seating[row-1][col+i] = "e"
                        self.seating[row+1][col+i] = "e"
                    for i in range(1,3):
                        self.seating[row][col-i] = "e"
                        self.seating[row][col+num_Tickets+i-1] = "e"
        #if seats arent availble asks user again to check seats
        else:
            print("Not all seats are available")
            self.buy()
        
        name = input("Enter your name: ")
        email = input("Enter you email: ")

        print(seat_Type)

        #calculates all cost values
        initial = 0
        total = 0
        if(seat_Type == "Front"):
            initial = num_Tickets * 80
        elif(seat_Type == "Middle"):
            initial = num_Tickets * 50
        elif(seat_Type == "Back"):
            initial = num_Tickets * 25
        print (initial)
        mask_Fee = 5*num_Tickets
        subtotal= mask_Fee+initial
        print (subtotal)
        tax = 0.0725*(subtotal)
        print(tax)
        total = tax+mask_Fee+initial
        

        dictionary = {
            "Name":name,
            "Email":email,
            "Number of tickets": num_Tickets,
            "Seat Type": seat_Type,
            "Seats":seat_list,
            "Tickets": initial,
            "Mask fee": mask_Fee,
            "Subtotal": subtotal,
            "tax": tax,
            "total": total
        }

        self.write_json(dictionary)

        seat_string = ""
        for i in seat_list:
            seat_string+= str(i)

        print("Here is your receipt: ")
        print("Name: \t"+ name)
        print("Email: \t"+ email)
        print("Number of tickets: \t"+str(num_Tickets))
        print("Seat Type: \t"+seat_Type)
        print("Seats: \t"+seat_string)
        print("Ticket Cost: \t"+str(initial))
        print("Mask fee: \t"+str(mask_Fee))
        print("Subtotal: \t"+str(subtotal))
        print("Tax: \t"+str(tax))
        print("Total: \t"+str(total))

        return
    
    def search_person(self, person):
        pathToFile = r"C:\Users\ashis\OneDrive\Documents\GitHub\Concert-app\.vscode\customers.json"
        try:
            jsonFile = open(pathToFile, 'r')
        except OSError:
            print("ERROR: Unable to open the file %s" % pathToFile)
            exit(-1)
        # read the whole json file into a variable
        concertList = json.load(jsonFile)
       
        # create an empty dictionary
        concertDictionary = {}
        # loop json list of data and put each name and birthday into a dictionary
        for elem in concertList:
            name = elem["Name"]
            email = elem["Email"]
            num_tickets = elem["Number of tickets"]
            seat_type = elem["Seat Type"]
            seat_list = elem["Seats"]
            initial = elem["Tickets"]
            mask_fee = elem["Mask fee"]
            subtotal = elem["Subtotal"]
            tax = elem["tax"]
            total = elem["total"]
            attribute_list = [email,num_tickets, seat_type, seat_list, initial, mask_fee, subtotal, tax, total]
            concertDictionary[name] = attribute_list
        
        purchase_list = []
        check = False
        for pair in concertDictionary:
            if(pair.find(person) >= 0):
                check = True
                purchase_list = concertDictionary[pair]
        print(purchase_list)

        seat_string = ""
        for i in seat_list:
            seat_string+= str(i)

        if(check):
            for thing in purchase_list:
                print(thing)
                
        return 

    def display_people(self):
        pathToFile = r"C:\Users\ashis\OneDrive\Documents\GitHub\Concert-app\.vscode\customers.json"
        try:
            jsonFile = open(pathToFile, 'r')
        except OSError:
            print("ERROR: Unable to open the file %s" % pathToFile)
            exit(-1)
        # read the whole json file into a variable
        concertList = json.load(jsonFile)
       
        # create an empty dictionary
        concertDictionary = {}
        # loop json list of data and put each name and birthday into a dictionary
        for elem in concertList:
            name = elem["Name"]
            email = elem["Email"]
            num_tickets = elem["Number of tickets"]
            seat_type = elem["Seat Type"]
            seat_list = elem["Seats"]
            initial = elem["Tickets"]
            mask_fee = elem["Mask fee"]
            subtotal = elem["Subtotal"]
            tax = elem["tax"]
            total = elem["total"]
            attribute_list = [email,num_tickets, seat_type, seat_list, initial, mask_fee, subtotal, tax, total]
            concertDictionary[name] = attribute_list

        for person in concertDictionary:
            print(person)
            for thing in concertDictionary[person]:
                print(thing)
            
            print()



    def main(self):
        self.menu()
        self.create_Seating()
        command = input("Enter a command: ")
        while(command != 'q'):
            if(command == "v"):
                self.print_Seating()
            elif(command == "b"):
                self.buy()
            elif(command == "s"):
                person = input("Who are you looking for?")
                self.search_person(person)
            elif(command == "d"):
                self.display_people()
            else:
                print("not valid command")
            self.menu()
            command = input("Enter a command: ")
        

Concert = concert_App()

Concert.main()


