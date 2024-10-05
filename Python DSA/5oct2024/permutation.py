user_in = str(input("Enter a string: "))

print("Your initial string is ", user_in)
result = []

def permute(data,i,length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i,length):
            data[i],data[j] = data[j],data[i]
            permute(data,i+1,length)
            data[i],data[j] = data[j],data[i]

permute(list(user_in),0,len(user_in))
print("Resulting permutations are following: ",result)