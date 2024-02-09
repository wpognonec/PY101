get loan amount, APR and loan duration from user
calculate monthly interest rate based on APR
convert loan duration to months
calculate monthly payment with information gathered
print the result rounding to two decimal places

START
PRINT welcome message
WHILE invalid_value
    GET loan_amount
WHILE invalid_value
    GET APR
WHILE invalid value
    GET loan_duration
SET montly_interest_rate = APR / 12
SET loan_duration_months = loan_duration / 12
SET montly_payment = loan_amount * (montly_interest_rate / (1 - (1 + montly_interest_rate) ** (-loan_duration_months)))
SET montly_payment = round(montly_payment, 2)
PRINT montly_payment

input formats:

APR: percent (2.5 => 2.5%)
Loan Duration: years (3 => 3 years => 36 months)