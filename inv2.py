#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения. Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по трем первым цифрам номера телефона; вывод на
# экран информации о человеке, чья фамилия введена с клавиатуры; если такого нет, выдать
# на дисплей соответствующее сообщение.
# Выполнить индивидуальное задание 2 лабораторной работы 9, использовав классы данных, а
# также загрузку и сохранение данных в формат XML.

import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class peop:
    surname: str
    name: str
    number: int
    year: int


@dataclass
class Staff:
    people: List[peop] = field(default_factory=lambda: [])

    def add(self, surname, name, number, year):
        self.people.append(
            peop(
                surname=surname,
                name=name,
                number=number,
                year=year
            )
        )

        self.people.sort(key=lambda peop: peop.number)

    def __str__(self):
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 20,
            '-' * 20,
            '-' * 20,
            '-' * 15
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^20} | {:^20} | {:^20} | {:^15} |'.format(
                "№",
                "Фамилия ",
                "Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        table.append(line)

        for idx, peop in enumerate(self.people, 1):
            table.append(
                '| {:>4} | {:<20} | {:<20} | {:<20} | {:>15} |'.format(
                    idx,
                    peop.surname,
                    peop.name,
                    peop.number,
                    peop.year
                )
            )
        table.append(line)

        return '\n'.join(table)

    def select(self):
        parts = command.split(' ', maxsplit=2)
        sur = (parts[1])

        count = 0

        for peop in self.people:
            if peop.get('surname') == sur:
                count += 1
                print('Фамилия:', peop.surname)
                print('Имя:', peop.name)
                print('Номер телефона:', sorted(key=lambda x: int(str(x)[:3])), peop.number)
                print('Дата рождения:', peop.year)

        if count == 0:
            print("Таких фамилий нет !")

        def load(self, filename):
            with open(filename, 'r', encoding='utf8') as fin:
                xml = fin.read()
            parser = ET.XMLParser(encoding="utf8")
            tree = ET.fromstring(xml, parser=parser)
            self.people = []

            for peop_element in tree:
                surname, name, number, year = None, None, None, None

                for element in peop_element:
                    if element.tag == 'surname':
                        surname = element.text
                    elif element.tag == 'name':
                        name = element.text
                    elif element.tag == 'number':
                        number = element.text
                    elif element.tag == 'year':
                        year = element.text

                    if surname is not None and name is not None \
                            and number is not None and year is not None:
                        self.people.append(
                            peop(
                                suname=surname,
                                name=name,
                                number=number,
                                year=year
                            )
                        )

        def save(self, filename):
            root = ET.Element('people')
            for peop in self.people:
                peop_element = ET.Element('peop')

                surname_element = ET.SubElement(peop_element, 'surname')
                surname_element.text = peop.surname

                name_element = ET.SubElement(peop_element, 'name')
                name_element.text = peop.name

                number_element = ET.SubElement(peop_element, 'number')
                number_element.text = str(peop.number)

                year_element = ET.SubElement(peop_element, 'year')
                year_element.text = str(peop.year)

                root.append(peop_element)

            tree = ET.ElementTree(root)
            with open(filename, 'wb') as fout:
                tree.write(fout, encoding='utf8', xml_declaration=True)

    if __name__ == '__main__':
        people = []
        staff = Staff
        while True:
            command = input(">>> ").lower()
            if command == 'exit':
                break

            elif command == 'add':
                surname = input("Фамилия ")
                name = input("Имя ")
                number = int(input("Номер телефона "))
                year = input("Дата рождения в формате: дд.мм.гггг ")

                staff.add(surname, name, number, year)


            elif command == 'list':
                print(staff)

            elif command.startswith('select '):
                parts = command.split(' ', maxsplit=2)
                sur = (parts[1])

                count = 0

                for peop in peoples:
                    if peop.get('surname') == sur:
                        count += 1
                        print('Фамилия:', peop.surname)
                        print('Имя:', peop.name)
                        print('Номер телефона:', peop.number)
                        print('Дата рождения:', peop.year)

                if count == 0:
                    print("Таких фамилий нет !")

            elif command.startswith('load '):
                parts = command.split(' ', maxsplit=1)
                staff.load(parts[1])

            elif command.startswith('save '):
                parts = command.split(' ', maxsplit=1)
                staff.save(parts[1])

            elif command == 'help':
                print("Список команд:\n")
                print("add - добавить человека;")
                print("list - вывести список людей;")
                print("select <фамилия> - запросить информацию по фамилии;")
                print("load <имя файла> - загрузить данные из файла;")
                print("save <имя файла> - сохранить данные в файл;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
            else:
                print(f
                "Неизвестная команда {command}", file = sys.stderr)
