def send_email(message, recipient, sender='university.help@gmail.com'):
    line_end = ('.com', '.ru', '.net')
    if not sender.endswith(line_end):
        print(f'Невозможно отправить письмо c адреса {sender} на адрес {recipient}')
    elif '@' not in sender:
        print(f'Невозможно отправить письмо c адреса {sender} на адрес {recipient}')
    elif not recipient.endswith(line_end):
        print(f'Невозможно отправить письмо c адреса {sender} на адрес {recipient}')
    elif '@' not in recipient:
        print(f'Невозможно отправить письмо c адреса {sender} на адрес {recipient}')
    else:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
