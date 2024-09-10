def_swich = True
def email_check(email):
    global def_swich
    if "@" in email and "mail" in email:
        for i in [".com", ".ru", ".net"]:
            if i in email:
                def_swich = True
                break
            else:
                def_swich = False
    else:
        def_swich = False

def sender_check(sender, recipient):
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

def send_email(message, recipient, sender = "university.help@gmail.com"):
    email_check(sender)
    email_check(recipient)
    if def_swich:
        sender_check(sender, recipient)
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

send_email("Здравствуйте! Поздравляем вас с окончанием курса 'Пайтон разработчик'", "student@mail.com")
print("___________________________")
send_email("Здравствуйте! Поздравляем вас с окончанием курса 'Пайтон разработчик'", "student@mail")
print("___________________________")
send_email("Здравствуйте! Поздравляем вас с окончанием курса 'Пайтон разработчик'", "student@mail.uk")
print("___________________________")
send_email("Здравствуйте! Поздравляем вас с окончанием курса 'Пайтон разработчик'", "student.ru")
print("___________________________")
send_email("Здравствуйте! Поздравляем вас с окончанием курса 'Пайтон разработчик'", "student@mail.ru", "university.help@gmail.ru")