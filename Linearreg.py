print("Model fits the data")
subid = ['7377AZ3737377','8838AZ3888383']
for i in subid:
    print(i)
    value = i[4:6]
    if value == 'AZ':
        print("test is pass")
    else:
        print("test fails")