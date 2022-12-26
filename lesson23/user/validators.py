from datetime import date
from rest_framework import serializers


class DomainValidator():
    def __init__(self, mail):
        if not isinstance(mail, list):
            mail = [mail]

        self.mail = mail

    def __call__(self, value):
        values = value.split('@')
        if values[1] in self.mail:
            raise serializers.ValidationError('Домен недоступен!')


class BirthDayValidator():
    def __call__(self, value: date):
        delta = date.today() - value
        if delta.days/365 < 9:
            raise serializers.ValidationError('Регистрация пользователя младше 9 лет запрещена!')
