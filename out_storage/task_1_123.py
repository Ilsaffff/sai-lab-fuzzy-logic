import dataclasses
from enum import IntEnum, Enum
from typing import Literal, Optional


# ===== READ-ONLY ===== SCROLL TO DOWN =====

class LevelEnum(str, Enum):
    JUNIOR = "junior"
    MIDDLE = "middle"
    SENIOR = "senior"


class LanguageEnum(str, Enum):
    PYTHON = "python"
    JAVA = "java"
    CPP = "cpp"
    GO = "go"


class OSEnum(str, Enum):
    UNIX = "unix"
    WINDOWS = "windows"


class DegreeEnum(str, Enum):
    YES = "yes"
    NO = "no"


class QuestionEnum(str, Enum):
    ASK_LEVEL = "ask_level"
    ASK_LANGUAGE = "ask_language"
    ASK_OS = "ask_os"
    ASK_GRADE = "ask_grade"
    ASK_DEGREE = "ask_degree"
    HIRE = "hire"
    DECLINE = "decline"


class Candidate:
    def __init__(self,
                 level=None,
                 lang=None,
                 os=None,
                 degree=None):
        self.level: Optional[LevelEnum] = level
        self.lang: Optional[LanguageEnum] = lang
        self.degree: Optional[DegreeEnum] = degree
        self.os: Optional[OSEnum] = os


# ==== EDIT =====

def select(c: Candidate) -> QuestionEnum:
    """
    Функция реализует стратегию управления

    Параметры:
        с (Candidate): текущее состояние кандидата. Все поля Candidate представляют собой строки из маленьких букв
                       не меняйте состояние кандидата!

    Возвращаемое значение:
        (QuestionEnum) - элемент из енама

    Возвращайте код QuestionEnum согласно желаемому вопросу или принятому решению

    Если хотите спросить про уровень (level), верните QuestionEnum.LVL
    Если хотите спросить про язык (lang), верните QuestionEnum.LANG
    Если хотите спросить про высшее образование (degree), верните QuestionEnum.DEGREE
    Если хотите спросить про ОС (OS), верните QuestionEnum.OS

    Если хотите принять человека на работу, верните QuestionEnum.HIRE
    Если хотите отказать человеку, верните QuestionEnum.DECLINE

    В программе уже реализована часть функциональности для большего понимания
    """
    if c.level is None:
        return QuestionEnum.ASK_LEVEL
    elif c.lang is None:
        return QuestionEnum.ASK_LANGUAGE

    if c.level == LevelEnum.JUNIOR:
        if c.lang == LanguageEnum.PYTHON:
            if c.degree is None:
                return QuestionEnum.ASK_DEGREE
            elif c.degree == DegreeEnum.YES:
                return QuestionEnum.HIRE
            else:
                if c.os is None:
                    return QuestionEnum.ASK_OS
                elif c.os == OSEnum.UNIX:
                    return QuestionEnum.HIRE

        # elif c.lang == LanguageEnum.CPP: ...

    # elif c.level == LevelEnum.MIDDLE: ...

    # do not hire
    return QuestionEnum.DECLINE
