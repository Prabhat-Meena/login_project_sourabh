import json

def login(name,email,pasword):

    with open('Index.json', 'r') as f:
        index = json.load(f)
        if (name in index) :
            if index[name][1] == pasword:
                print("login complete")
            else:
                print("Incorect user name or pasword please try again" )           
        else:
            print('Incorect user name or pasword or you need to singup first')
            singup()

   
def singup():
    name = input('Enter your name: ')
    emai = input('Enter your email: ')
    pasword = input("Enter your pasword: ")
    with open('Index.json', 'r') as f:
        index = json.load(f)

        index[name] = [emai,pasword]

        index = json.dumps(index)

        with open('Index.json', 'w') as f:
            f.write(index)
            print("Singup complete")