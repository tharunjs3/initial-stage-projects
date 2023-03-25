from time import time
start=time()


#now we are creating a program to find acronym of a given name


words="Artificial Engineer specialist"
spliting_process=words.split()


a=" "
for i in spliting_process:
    a=a+str(i[0]).upper()
print(a)


end=time()
execution_time=end-start
print(execution_time)

 