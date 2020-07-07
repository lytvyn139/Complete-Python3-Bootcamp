import pdb  #python debuger

x = [1,2,3]
y = 2
z = 3

result_one = y + z
#set trace before error line
pdb.set_trace() #q for exit
result_two = y + x
