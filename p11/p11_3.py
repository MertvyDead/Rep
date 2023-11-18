



def add_user(credentials_list, login, password):
    # Проверяем, что логин не повторяется в списке словарей
    for user in credentials_list:
        if user['login'] == login:
            print("Логин уже существует")
            return credentials_list
    
    # Проверяем, что пароль длиной не менее 8 символов
    if len(password) < 8:
        print("Пароль должен быть не менее 8 символов")
        return credentials_list
    
    # Создаем новый словарь с переданным логином и паролем
    new_user = {'login': login, 'password': password}
    
    # Добавляем новый словарь в список
    credentials_list.append(new_user)
    
    # Возвращаем обновленный список
    return credentials_list
dctlst = [{'login':'mertvyDead','password':'qwerty12345'}]
print(add_user(dctlst, input('login: '), input('password: ')))
