



def add_user(credentials_list, login, password):
    
    for user in credentials_list:
        if user['login'] == login:
            print("Логин уже существует")
            return credentials_list
    
    
    if len(password) < 8:
        print("Пароль должен быть не менее 8 символов")
        return credentials_list
    
    
    new_user = {'login': login, 'password': password}
    
    
    credentials_list.append(new_user)
    
   
    return credentials_list
dctlst = [{'login':'mertvyDead','password':'qwerty12345'}]
print(add_user(dctlst, input('login: '), input('password: ')))
