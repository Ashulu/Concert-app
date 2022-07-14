class concert_App(object):

    def __init__(self) -> None:
         self.n_row = 20
         self.n_col = 26
         self.seating = []

    def create_Seating(self):
        # available seat
        available_seat = '.'
        # create some available seating
        for r in range(self.n_row):
            row = []
            for c in range(self.n_col):
                row.append(available_seat)
            self.seating.append(row)
        # print available seating and costs
    
    def print_Seating(self):
        print("\t" + "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
        for r in range(self.n_row):
            print(r+1, end="\t")
            for c in range(self.n_col):
                print(self.seating[r][c], end=" ")
            if(r<6):
                    print(" $80")
            elif(r<12):
                    print(" $50")
            else:
                    print(" $25")

    def main(self):
        self.create_Seating()
        self.print_Seating()

Concert = concert_App()

Concert.main()

