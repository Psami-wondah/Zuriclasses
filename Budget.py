Samuel = False
class Budget:
    def __init__(self, cat1, cat2, cat3):
        self.cat1 = cat1
        self.cat2 = cat2
        self.cat3 = cat3
        self.balance = {
            self.cat1: 0,
            self.cat2: 0,
            self.cat3: 0,
        }

    def depositFunction(self, category):
        error = True
        while error == True:
            try:
                depositAmount = int(input('How much would you like to deposit? \n'))
                error = False
                self.balance[category] += depositAmount
                print(f'%d Naira has Been added to {self.cat1} and now the balance is: %dN' % (depositAmount, self.balance[category]))
                isvalopt = False
                while isvalopt== False:
                    selectedOption = input('Would you like to deposit into any other account? (1) Yes (2) No \n')
                    if selectedOption == '1':
                        isvalopt = True
                        self.deposit()
                    elif selectedOption== '2':
                        isvalopt = True
                        init()
                    else:
                        isvalopt = False
                        print('Wrong input, Try again')

            except ValueError:
                error = True
                print('Please enter integers only')

    def withdrawalFunction(self, category):
        error = True
        while error == True:
            try:
                withdrawalAmount = int(input('How much would you like to withdraw? \n'))
                if withdrawalAmount <= self.balance[category]:
                    print('Currently dispensing', withdrawalAmount, 'Naira')
                    print('Please take your cash')
                    self.balance[category] -= withdrawalAmount
                else:
                    print('Sorry, you do not have enough funds')
                isvalopt = False
                while isvalopt == False:
                    selectedOption = input('Would you like to withdraw from any other account? (1) Yes (2) No \n')
                    if selectedOption == '1':
                        isvalopt = True
                        self.withdraw()
                    elif selectedOption == '2':
                        isvalopt = True
                        init()
                    else:
                        isvalopt = False
                        print('Wrong input, Try again')
            except ValueError:
                error = True
                print('Please enter integers only')

    def tranferOperation(self, first, second):
        error = True
        while error == True:
            try:
                transferAmount=int(input('Enter the amount you wish to transfer \n'))

                if transferAmount <= self.balance[first]:
                    self.balance[first] -= transferAmount
                    self.balance[second] += transferAmount
                    print(f'Transfer done and now the balance of {first} is: {self.balance[first]}N and \n {second} is '
                          f'{self.balance[second]}N')
                else:
                    print('Sorry, you do not have enough funds.')
                isvalopt = False
                while isvalopt == False:
                    selectedOption = input('Would you like to make any other transfer? ? (1) Yes (2) No \n')
                    if selectedOption == '1':
                        isvalopt = True
                        self.transfer()
                    elif selectedOption == '2':
                        isvalopt = True
                        init()
                    else:
                        isvalopt = False
                        print('Wrong input, Try again')
            except ValueError:
                error = True
                print('Please enter integers only')


    def deposit(self):
        print('Which category do you wish to deposit into?')
        print(f'1. {self.cat1}')
        print(f'2. {self.cat2}')
        print(f'3. {self.cat3}')
        selectedOption = input('Please select an option \n')
        if selectedOption == '1':
            self.depositFunction(self.cat1)
        elif selectedOption == '2':
            self.depositFunction(self.cat2)
        elif selectedOption == '3':
            self.depositFunction(self.cat3)
        else:
            print('Wrong input')
            self.deposit()

    def withdraw(self):
        print('Which category do you wish to withdraw from?')
        print(f'1. {self.cat1}')
        print(f'2. {self.cat2}')
        print(f'3. {self.cat3}')
        selectedOption = input('Please select an option \n')
        if selectedOption == '1':
            self.withdrawalFunction(self.cat1)
        elif selectedOption == '2':
            self.withdrawalFunction(self.cat2)
        elif selectedOption == '3':
            self.withdrawalFunction(self.cat3)
        else:
            print('Wrong input')
            self.withdraw()

    def computeBalance(self):
        print('Which balance do you wish to check?')
        print(f'1. {self.cat1}')
        print(f'2. {self.cat2}')
        print(f'3. {self.cat3}')
        # print(f'4. {self.food} + {self.clothing}')
        # print(f'5. {self.food} + {self.entertainment}')
        # print(f'6. {self.clothing} + {self.entertainment}')
        print(f'4. Total Balance')
        selectedOption = input('Please select an option \n')
        if selectedOption == '1':
            print(f'The balance is: {self.balance[self.cat1]}')
        elif selectedOption == '2':
            print(f'The balance is: {self.balance[self.cat2]}')
        elif selectedOption == '3':
            print(f'The balance is: {self.balance[self.cat3]}')
        # elif selectedOption == 4:
        #     print('The balance is: ', self.balance[self.food] + self.balance[self.clothing])
        # elif selectedOption == 5:
        #     print('The balance is: ', self.balance[self.food] + self.balance[self.entertainment])
        # elif selectedOption == 6:
        #     print('The balance is: ', self.balance[self.entertainment] + self.balance[self.clothing])
        elif selectedOption == '4':
            print('The balance is: ', self.balance[self.cat3] + self.balance[self.cat2] + self.balance[self.cat1])
        else:
            print('Wrong input, please try again')
            self.computeBalance()
        isvalopt = False
        while isvalopt == False:
            option = input('Would you like to check any other balance? (1) Yes (2) No \n')
            if option == '1':
                isvalopt = True
                self.computeBalance()
            elif option == '2':
                isvalopt = True
                init()
            else:
                isvalopt = False
                print('Wrong input, Try again')

    def transfer(self):
        selectedOption1= input(f'Please enter the category you wish to transfer from ({self.cat1} or {self.cat2}'
                               f' or {self.cat3}) \n')
        selectedOption2= input(f'Please enter the category you wish to transfer to ({self.cat1} or {self.cat2}'
                               f' or {self.cat3}) \n')
        if selectedOption1 in self.balance and selectedOption2 in self.balance:
            self.tranferOperation(selectedOption1, selectedOption2)
        else:
            print('One of the categories you entered does not exist, please try again')
            self.transfer()



def init1():
    print('Welcome to MyPreciousThreeBudgets')
    error = False
    Name = input('What is your name? e.g Samuel \n')
    print(f'Mr/Mrs {Name} Please enter the three budgets you wish to manage, one space each e.g.'
          f' food entertainment clothing')
    while error == False:
        try:
            error= True
            Budgets = list(map(str, input().rstrip().split()))
            if len(Budgets) > 3:
                print('Enter again, three budgets only')
                error = False
            else:
                global Samuel
                Samuel = Budget(Budgets[0], Budgets[1], Budgets[2])
                init()
        except IndexError:
            error=False
            print('Please enter again in this format: food entertainment clothing ')


def init():
    print('Please what you like to do? ')
    print('1. Deposit to a Budget')
    print('2. Withdraw from a Budget')
    print('3. Check balances of your Budget categories')
    print('4. Transfer between Budget categories')
    print('5. Exit')


    isValidOption = False
    while isValidOption == False:
        selectedOption = input('Please select an option \n')
        if selectedOption == '1':
            isValidOption = True
            Samuel.deposit()
        elif selectedOption == '2':
            isValidOption = True
            Samuel.withdraw()
        elif selectedOption == '3':
            isValidOption = True
            Samuel.computeBalance()
        elif selectedOption == '4':
            isValidOption = True
            Samuel.transfer()
        elif selectedOption == '5':
            exit()
        else:
            print('Wrong input, please try again')


init1()
