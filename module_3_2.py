def send_email(mail, recipient, sender="university.help@gmail.com"):
    is_recipient_valid_domain = any([recipient.endswith('.com'), recipient.endswith('.ru'), recipient.endswith('.net')])
    is_sender_valid_domain = any([sender.endswith('.com'), sender.endswith('.ru'), recipient.endswith('.net')])
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        if is_recipient_valid_domain and is_sender_valid_domain and recipient.count('@') and sender.count('@'):
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')