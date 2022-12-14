from dataclasses import dataclass


@dataclass
class PropertiesForInformation:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    mobile_number: int = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class Subject:
    subject: list = None


@dataclass
class Color:
    color: list = None


@dataclass
class Book:
    book: list = None
