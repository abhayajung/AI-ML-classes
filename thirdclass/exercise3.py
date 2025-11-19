# balance = 1000.00
# deposit = 250.00
# service_fee = 10.50
# interest_rate = 1.05 (5% growth)
# 
# Question: Perform the following operations using assignment operators:
# 1. Apply the deposit using the += operator.
# 2. Subtract the service_fee using the -= operator.
# 3. Apply the interest_rate multiplier (for growth) using the *= operator.
# 4. Initialize a new variable, shares, with the final balance. Then, use the //=
#    operator on shares to determine how many full $100 units (shares) can be 
#    purchased from that amount.
# 
# Output: Print the balance after steps 1, 2, and 3, and the final integer value of
#         shares after step 4.

balance = 1000.00
deposit = 250.00
service_fee = 10.50
interest_rate = 1.05  # (5% growth)

balance += deposit
print(f"Balance after deposit is {balance}")

balance -= service_fee
print(f"Balance after service fee is {balance}")

balance *= interest_rate
print(f"Balance after interest is {balance}")

share = balance
share //= 100
print(f"Total {share} of $100 units can be bought from {balance} amount")
