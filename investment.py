# Version 1: Calculate Investment Cost
shares = 10
share_price = 150
investment_cost = shares * share_price

print("STOCK INVESTMENT CALCULATOR")
print(f"Shares Purchased: {shares}")
print(f"Price per Share: ${share_price}")
print(f"Total Investment Cost: ${investment_cost}")

# Version 2: Calculate Profit and Return
new_share_price = 175
current_value = new_share_price * shares
profit_loss = current_value - investment_cost
return_pct = (profit_loss / investment_cost) * 100

print(f"New Price per Share: ${new_share_price}")
print(f"Current Investment Value: ${current_value}")
print(f"Profit/Loss: ${profit_loss}")
print(f"Percentage Return: {return_pct:.2f}%")
