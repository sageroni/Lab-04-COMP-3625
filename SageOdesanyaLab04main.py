#TASK 2: compute perceived values of investments
# Each client currently owns 2 investments. Each has a specified probability of paying off, and an amount 
# that the client will make if it does pay off (assume the client gets $0 if the investment doesn’t pay off). 
# This data is provided in a csv file.

# Using the utility curves from part 1:
# Compute each client’s perceived utility of each investment. 
# Compute the amount that you could offer each client now (in dollars), such that they would be indifferent 
# between the payment and the investment/lottery.

# Hint: you’ll need the inverse of the utility function above (i.e. so you can compute the $ amount as a function of the utility)


import numpy as np

# Define Utility Functions
def utility_ClientA(x): return 0.2 * np.log(x / 1000 + 1)
def utility_ClientB(x): return 0.14 * np.log(x / 200 + 1)
def utility_ClientC(x): return 1.43 * np.log(x / 100000 + 1)

constant_e = np.e
# Define Inverse Utility Functions (cert equiv) 
def inverse_ClientA(u): return 1000 * (constant_e**(u / 0.2) - 1)
def inverse_ClientB(u): return 200 * (np.exp(u / 0.14) - 1)
def inverse_ClientC(u): return 100000 * (constant_e**(u / 1.43) - 1)

# i was worried that np was lying to me (i know, it sounds ridiculous as i'm typing it out)
# so what i did was i changed the inverse for ClientB to use np.exp and left ClientA and 
# ClientC's inverse functions the same. I then compared the data from two solutions I got, and
# what would you know, the algorithm was right! does this mean I will trust it in the future?
# only time will tell. 

# payoff probability, payout i made these as a 2d array
# that way it is easier to use the values in them for table purposes
investments = {
    "A owns Inv 1": [0.6, 80000],
    "A owns Inv 2": [0.5, 20000],
    "B owns Inv 3": [0.9, 100000],
    "B owns Inv 4": [0.4, 40000],
    "C owns Inv 5": [0.1, 10000],
    "C owns Inv 6": [0.05, 90000]
}

print(f"{'Investment':<12} | {'Utility for ClientA':<21} | {'Value for Client A($)':<20} | {'Utility for ClientB':<21} | {'Value for ClientB($)':<20} | {'Utility for ClientC':<21} | {'Value for ClientC($)':<20}")
# the numbers that come after the :< are to ensure that each column is wide enough to properly fit the text. 
print("-" * 140)
# this makes the dotted line so it is easier to differentiate between the column titles and their values.

for name, (probability, payout) in investments.items():
    # Expected Utility = probability * utility(payoff) + (1-probability) * U(0)
    # their expected utility is basically what is the sum of their chances of getting it * how much use they would get out of the payout
    # and then we subtract 1 from the probability and ask ourselves how much utility they would get from NOT getting the payout. 
    eu_A = probability * utility_ClientA(payout)
    eu_B = probability * utility_ClientB(payout)
    eu_C = probability * utility_ClientC(payout)
    
    # now this is how we calculate the certainty equivalence (however you spell that word)
    ce_A = inverse_ClientA(eu_A)
    ce_B = inverse_ClientB(eu_B)
    ce_C = inverse_ClientC(eu_C)
    
    print(
        f"{name:<12} | {eu_A:<21f} | {ce_A:<20f} | "
        f"{eu_B:<21f} | {ce_B:<20f} | "
        f"{eu_C:<21f} | {ce_C:<20f}"
    )


# Task 3: Reflect 🤔
# Answer these questions:

# To whom should each of the 6 investments be sold? Why?
# All six investment should be sold to ClientC. Since they have the most linear investment curve,
# they would be impacted the least by losing out on their investment. They value these lotteries 
# closest to their actual mathematical expected value. The assets should be going from ClientA and 
# ClientB (people who do not value them as much) to ClientC. 

# Pick one investment that should be sold. Who should it be sold to, and what is the maximum price it 
# could be sold for? What utility gain is provided to each party at that price?

# If we look at Investment 4, ClientC values the investment of 40000 at $14,407. ClientB, the original seller,
# values the investment at $1,468. ClientA values the investment of $40,000 at $3,417. The absolute maximum that
# ClientC will pay is $14,407. 

# If we use ClientC's maximum price to perform the transaction:
# ClientC has a utility gain of 0, since they pay their subjective value. 

# ClientB will have a utility gain higher than 0. it will be 0.296985 (their perceived utility) 
# and then subtract the perceived utility gain that ClientC has from this transaction , which is 0.192462. 

# ClientB will have a utility gain of 0.104523. 