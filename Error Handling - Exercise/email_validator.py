from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


class InvalidName(Exception):
    pass


def validator(current_email):
    domains = [".com", ".bg", ".net", ".org"]

    if "@" not in current_email:
        raise MustContainAtSymbolError("Email must contain @")

    if current_email.count("@") > 1:
        raise TooManyAtSymbols("@ symbol must be only one")

    if len(current_email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 letters")

    if findall(r'[\w+\\.]+', current_email)[0] != current_email.split("@")[0]:
        raise InvalidName("Name cannot contain special symbols")

    find_domain = findall(r'\.+[a-z]+', current_email)

    if not find_domain or find_domain[-1] not in domains:
        raise InvalidDomainError("you must enter valid domains - .com, .bg, .org, .net")

    print("Email is valid")


email = input()

while email:

    validator(email)

    email = input()
