import vk_api


def auth_handler():
    key = input('Введи код: ')
    remember_device = True
    return key, remember_device


def main():
    login, password = 'тут логин', 'тут пароль'

    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    response = vk.wall.get(count=1)
    if response['items']:
        for i in response['items']:
            print(i['text'])  # что тут писать надо?


if __name__ == '__main__':
    main()
