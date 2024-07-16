def send_email(message, recipient, *, sender = "university.help@gmail.com"):
	if (recipient.find("@") + sender.find("@") == -2) or (
			recipient.find(".com") + sender.find(".com") + recipient.find(".ru") + sender.find(".ru")
			+ recipient.find(".net") + sender.find(".net") == -6):
		print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
	elif recipient == sender:
		print("Нельзя отправить письмо самому себе!")
	elif sender == "university.help@gmail.com":
		print("Письмо успешно отправлено с адреса", sender, "на адрес ", recipient, ".")
	else:
		print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")


send_email(input(), input())
send_email(input(), input(), sender = input())
send_email(input(), input(), sender = input())
send_email(input(), input(), sender = input())
