#!/usr/bin/env python
# !-*- coding:utf-8 -*-
import smtplib
from bin.until import Logger

L = Logger.getInstance()

class Mail_func(object):
    def __init__(self, data):
        self.from_address = data['from_address']
        self.password = data['password']
        self.to_address = data['to_address']
        self.title = data['title']
        self.content = data['content']
        self.type =data['type']

    def send_mail(self, data):
        if data['to_address'] is None:
            print("not address to send")
        else:
            self.to_address = data['to_address']
        try:
            srv = smtplib.SMTP(**srv_kwargs)
            srv.login(self.from_address, self.password)
            srv.sendmail(self.from_address, self.to_address, self.content)
            srv.quit()
            L.info('send email to user successfully')
        except smtplib.SMTPException as e:
            L.warn('send email to user failed')
            L.exception(e)

def getInstance():
    return Mail_func()


def main():
    Mail_func()

if __name__ == "__main__":
    main()