price = float(input("Enter car price: "))

tax_rate = 0.10         
reg_rate = 0.05 
agent_fee = 50000        
del_fee = 30000    

tax = price * tax_rate
reg = price * reg_rate
final_price = price + tax + reg + agent_fee + del_fee

print("total cost: ", final_price)
