class ExpenseSharing:
    def __init__(self,friends):
        self.friends = friends
        self.expense = {friend : 0 for friend in friends}
        
    def add_expense(self,payer,amount,participents):
        split_amount = amount / len(participents)
        for participent in participents:
            self.expense[participent] -= split_amount
        self.expense[payer] += amount
          
    def calculate_settlement(self):
        creditors = [] #who gives money in creditors list
        debtors =[]  #who return money in debtors list
        for friend, balance in self.expense.items():
            if balance > 0:
                creditors.append((friend, balance))
            elif balance < 0:
                debtors.append((friend, -balance))
        
        while debtors and creditors:
            debtor, debt_amnt = debtors.pop()
            creditor, credit_amnt = creditors.pop()
            
            payment = min(debt_amnt,credit_amnt)
            print(f"{debtor} owes {creditor} : rs.{payment: .2f}")
            
            if debt_amnt > payment:
                debtors.append((debtor, debt_amnt - payment))
            if credit_amnt > payment:
                creditors.append((creditor, credit_amnt - payment))
        
        
        
        
        
if __name__ == "__main__":
    friends = input("enter the names of FRIENDS, seperater by commas ").split(',')
    friends = [friend.strip() for friend in friends]
    
    expense_sharing = ExpenseSharing(friends)
    
    while True:
        payer = input("enter the payer name who paid (and 'done' to finish : )")
        if payer.lower() == 'done':
            break
        
        amount = float(input("enter the amount paid: "))
        
        participents = input("enter the names of friends whose amount has been shared , enter the with ',': ").split(',')
        participents = [participent.strip() for participent in participents]
        
        expense_sharing.add_expense(payer,amount,participents)
    print("\n final sattelment")
    expense_sharing.calculate_settlement() 
            
        