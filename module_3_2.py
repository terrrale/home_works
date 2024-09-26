
check = False

def email_check(email):
    global check
    if '@mail' in email or '@gmail' in email:
        for i in ['.com', '.ru', '.net']:
            if i in email:
                check = True
                break
            else:
                check = False
    else:
        check = False

def sender_check(sender, recipient):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

def send_email(message, recipient, *,sender = "university.help@gmail.com"):
    for i in [sender, recipient]:
        email_check(i)
        if not check:
            break
    if not check :
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        sender_check(sender, recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print("______________________")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print("______________________")
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print("______________________")
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')