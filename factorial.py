import datetime
n = int(input("Enter Any Number : "))

#Simple Recursion

# start_time = datetime.datetime.now()

# def fact(n):
#     if n<=1:
#         return 1
#     return n*fact(n-1)

# print(fact(n))
# end_time = datetime.datetime.now()
# print("Execution Time is {} ".format((end_time-start_time).total_seconds()))



#Dynamic Programming

start_time = datetime.datetime.now()

def fact(n, data):
    
    if n<=1:
        
        data[n] = 1
        return 1
    if n in data:
        return data[n]
    data[n] = n*fact(n-1, data)
    
    return data[n]

data={}
print(fact(n, data))
end_time = datetime.datetime.now()
print("Execution Time is {} ".format((end_time-start_time).total_seconds()))