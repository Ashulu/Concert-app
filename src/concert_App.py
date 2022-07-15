import jsonpickle
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
            if(r<6):
                    print(" Front   $80")
            elif(r<12):
                    print(" Middle   $50")
            else:
                    print(" Back   $25")
        print()


    def buy(self):
        seat_list = []
        cost = 0
        num_Tickets = int(input("How many in your party?: "))
        start = input("First seat:")
        split_word = list(start)
        row = int(split_word[0])-1
        col = ord(split_word[1])-97
        
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

        else:
            print("Not all seats are available")
            self.buy()
        name = input("Enter your name: ")
        email = input("Enter you email: ")

        customers = "customers.json"
        try:
            customersFile = open(customers,"w")
        except IOError:
            print("Error: file "+ customers +" does not appear to exist")  
            return -1
        
        customerJson = jsonpickle.encode(customers)

        customersFile.write(self.prettyJson(customerJson))

        print("Here is your receipt")
        return

        


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
                print("complete")
            elif(command == "d"):
                print("complete")
            else:
                print("not valid command")
            self.menu()
            command = input("Enter a command: ")
        

Concert = concert_App()

Concert.main()
#print(ord("a"))

