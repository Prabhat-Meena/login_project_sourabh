import json
def login(name,email,pasword):
    with open('userinfo.json', 'r') as g1:
        index = json.load(g1)
        if name in index : 
            if index[name][1] == pasword:
                print("login complete")
            else:
                print("please try again" )           
        else:
            print('name or pasword or you need to singup first')
            singup()
def singup():
    name = input('Enter your name: ')
    emai = input('Enter your email: ')
    pasword = input("Enter your pasword: ")
    with open('userinfo.json', 'r') as g1:
        index = json.load(g1)
        index[name] = [emai,pasword]
        index = json.dumps(index)
        with open('userinfo.json', 'w') as g1:
            g1.write(index)
            print("Singup complete")