import json
def login(name,email,pasword):
    with open('userinfo.json', 'r') as g1:
        index = json.load(g1)
        if name in index :
            "login complete" if index[name][1] == pasword else "please tyr again"         
        else:
            print('name or pasword or you need to singup first')
            signup()
def signup():
    name, email, pasword = input('Enter your name:') ,input('Enter your email: '), input('Enter your pasword: ')
    with open('userinfo.json', 'r') as g1:
        index = json.load(g1)
        index[name] = [email,pasword]
        index = json.dumps(index,indent=4)
        with open('userinfo.json', 'w') as g1:
            g1.write(index)
            print("Signup complete")