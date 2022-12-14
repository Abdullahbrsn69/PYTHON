class bank():
  def __init__(self,bank_name):
    self.accounts = {}
    self.passwords = {}
    self.bank_name = str(bank_name)
  
  def add_account(self,account_name,money,password):
    self.accounts[account_name] = int(money)
    self.passwords[account_name] = password
    
    return account_name
    
  #sending money `account1 --> account2`
  def transaction(self,account1,account2,amount): 
    if self.accounts[account1] >= self.accounts[account1]:
        if self.accounts[account1]-amount < 0:
          return "transaction failed"
        
        else:
          self.accounts[account1] -= amount
          self.accounts[account2]+=amount
          return "transaction sucessfull"
        
    else:
        return "transaction failed"
      
  def account_data(self,account,password):
    if password == self.passwords[account]:
      return self.accounts[account]
    else:
      return "Password is incorrect"
    


my_bank = bank("my bank 1") #creates a virtual bank

x = my_bank.add_account("User-1",500,"abcd") #creates a user in the bank
y = my_bank.add_account("User-2",200,"1234")

print("Before transactions:")
print(x,my_bank.account_data(x,"abcd")) #getting the money of the first account
print(y,my_bank.account_data(y,"1234")) #getting the money of the second account

my_bank.transaction(x,y,10) #`x` gives money to `y`

print("After transactions:")
print(x,my_bank.account_data(x,"abcd"))
print(y,my_bank.account_data(y,"1234"))
