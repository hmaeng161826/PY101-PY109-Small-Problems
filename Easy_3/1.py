#function(string, positive integer):
#print 'positive integer' times of string (= iterate/print n times)

def repeat(string, n):
    for _ in range(n):
        print(string)

repeat('Hello', 3)
