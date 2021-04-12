class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        self.balance = {
            self.food: 0,
            self.clothing: 0,
            self.entertainment: 0,
        }

    def depositFunction(self, category):
        depositAmount = int(input('How much would you like to deposit? \n'))
        self.balance[category] += depositAmount
        print('%d Naira has Been added to Food and now the balance is: %d' % (depositAmount, self.balance[category]))
        selectedOption = int(input('Would you like to deposit into any other account? (1) Yes (2) No \n'))
        if selectedOption == 1:
            self.deposit()
        else:
            pass

    def withdrawalFunction(self, category):
        withdrawalAmount = int(input('How much would you like to withdraw? \n'))
        if withdrawalAmount <= self.balance[category]:
            print('Currently dispensing', withdrawalAmount, 'Naira')
            print('Please take your cash')
            self.balance[category] -= withdrawalAmount
        else:
            print('Sorry, you do not have enough funds')
        selectedOption = int(input('Would you like to withdraw from any other account? (1) Yes (2) No \n'))
        if selectedOption == 1:
            self.withdraw()
        else:
            pass

    def tranferOperation(self, first, second):
        selectedOption=int(input('Enter the amount you wish to transfer \n'))
        self.balance[first] -= selectedOption
        self.balance[second] += selectedOption
        if selectedOption <= self.balance[first]:
            print(f'Transfer done and now {first} is: {self.balance[first]} and \n {second} is {self.balance[second]}')
        else:
            print('Sorry, you do not have enough funds.')

    def deposit(self):
        print('Which category do you wish to deposit into?')
        print(f'1. {self.food}')
        print(f'2. {self.clothing}')
        print(f'3. {self.entertainment}')
        selectedOption = int(input('Please select an option \n'))
        if selectedOption == 1:
            self.depositFunction(self.food)
        elif selectedOption == 2:
            self.depositFunction(self.clothing)
        elif selectedOption == 3:
            self.depositFunction(self.entertainment)
        else:
            self.deposit()

    def withdraw(self):
        print('Which category do you wish to withdraw from?')
        print(f'1. {self.food}')
        print(f'2. {self.clothing}')
        print(f'3. {self.entertainment}')
        selectedOption = int(input('Please select an option \n'))
        if selectedOption == 1:
            self.withdrawalFunction(self.food)
        elif selectedOption == 2:
            self.withdrawalFunction(self.clothing)
        elif selectedOption == 3:
            self.withdrawalFunction(self.entertainment)
        else:
            self.withdraw()

    def computeBalance(self):
        print('Which balance do you wish to check?')
        print(f'1. {self.food}')
        print(f'2. {self.clothing}')
        print(f'3. {self.entertainment}')
        print(f'4. {self.food} + {self.clothing}')
        print(f'5. {self.food} + {self.entertainment}')
        print(f'6. {self.clothing} + {self.entertainment}')
        print(f'7. Total Balance')
        selectedOption = int(input('Please select an option \n'))
        if selectedOption == 1:
            print(f'The balance is: {self.balance[self.food]}')
        elif selectedOption == 2:
            print(f'The balance is: {self.balance[self.clothing]}')
        elif selectedOption == 3:
            print(f'The balance is: {self.balance[self.entertainment]}')
        elif selectedOption == 4:
            print('The balance is: ', self.balance[self.food] + self.balance[self.clothing])
        elif selectedOption == 5:
            print('The balance is: ', self.balance[self.food] + self.balance[self.entertainment])
        elif selectedOption == 6:
            print('The balance is: ', self.balance[self.entertainment] + self.balance[self.clothing])
        elif selectedOption == 7:
            print('The balance is: ', self.balance[self.entertainment] + self.balance[self.clothing] + self.balance[self.food])
        else:
            print('Wrong input, please try again')
            self.computeBalance()

    def transfer(self):
        selectedOption1= input(f'Please enter the category you wish to transfer from ({self.food} or {self.clothing}'
                               f' or {self.entertainment}) \n')
        selectedOption2= input(f'Please enter the category you wish to transfer to ({self.food} or {self.clothing}'
                               f' or {self.entertainment}) \n')
        self.tranferOperation(selectedOption1, selectedOption2)







Samuel = Budget('Garri', 'Shirt', 'Football')
Samuel.deposit()
# Samuel.withdraw()
#Samuel.computeBalance()
Samuel.transfer()
