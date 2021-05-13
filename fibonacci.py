import datetime
n = int(input("Enter ANy Value"))

#Dynamic Programming

start_time = datetime.datetime.now()
def fib(n, data):
    
    if n==0 or n==1:
        data[n] = n
        
        return n
    else:
        if n in data:
            
            return data[n]
        
        data[n] = fib(n-1, data) + fib(n-2, data)
        
        return data[n]
data = {}
print(fib(n, data))
print(data)
end_time = datetime.datetime.now()
delta = end_time - start_time
print("Total Execution Time is {}".format(delta.total_seconds()))

# Simple Recursion

# start_time = datetime.datetime.now()
# def fib(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(n))

# end_time = datetime.datetime.now()
# delta = end_time - start_time
# print("Total Execution Time is {}".format(delta.total_seconds()))