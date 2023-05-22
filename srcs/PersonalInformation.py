#!/usr/bin/python
# -*- coding: utf-8 -*-

class PersonalInformation:
    def __init__(self, name, phoneNumber, sex, email, accountType, id, password):
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__sex = sex
        self.__email = email
        self.__accountType = accountType
        self.__id = id
        self.__password = password

    def getName(self):
        return (self.__name)

    def getPhoneNumber(self):
        return (self.__phoneNumber)

    def getSex(self):
        return (self.__sex)

    def getEmail(self):
        return (self.__email)

    def getAccountType(self):
        return (self.__accountType)

    def getId(self):
        return (self.__id)

    def getPassword(self):
        return (self.__password)

    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        self.__password = password
