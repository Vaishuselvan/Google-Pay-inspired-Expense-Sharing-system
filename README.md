# Google-Pay-inspired-Expense-Sharing-system
This repositry contains the cod for tracking you and your friends expence sharing in simple tool like gpay. 

Friends want to easily track shared expenses and settle debts using a simple tool similar to google pay. Lets considered friends ['ALICE','BOB','CAROL'] went on a trip now they wants to share their expenses unlike treditional methodes we are going to who owes how. Build a simple python script to find the solution.

STEPS FOLLOWED:
1. Get inputs from the end user.
2. First get friends who went to trip.
3. Store it in a list
4. Then get payer who pays.
5. How much they paid in float
6. For whome all the paid, names in list.


Create class in that give methodes to find who owes who, and how much the friends have to settle down to each others.

## SAMPLE OUTPUT Explaination ##

1. alice : 3000/3 = 1000 
   where as alice share is 1000
   here alice needs to be reimbursed Rs.2000


2. Bo : 600 / 3 200 each
   alice rs : 2000 -200 = 1800
   bob : - 1000  + 400 = rs -600
   carol : -1000 - 200 = -1200


3. carol : 400/2 = 200
   alice : 1800 - 200 = 1600
   bob: rs 600
   carol : -1200 + 200 = -1000



THEREFORE OUTPUT IS:

1. Final Settlement
   Alice owes: rs. 1600.00
   Bob needs to be reimbursed : rs. 600.00
   Carol needs to be reimbursed : rs. 1000.00

