def varArgFunc(*var_arg):
    print(*var_arg)
varArgFunc() # 0 argument
varArgFunc('Sokan','Academy') # 2 arguments
varArgFunc(1,2,3,4,5) # 5 arguments
varArgFunc(9, 'Nine') # 2 arguments 
varArgFunc ('\n','***','\n','* *','\n','***' ,'\n') # 7 arguments
