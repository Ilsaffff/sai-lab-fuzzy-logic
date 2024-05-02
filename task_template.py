import dataclasses
import math
from math import log2

from typing import List
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
    R = "r"


class OSEnum(str, Enum):
    MACOS = "macos"
    LINUX = "linux"
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

    Если хотите спросить про уровень (level), верните QuestionEnum.ASK_LEVEL
    Если хотите спросить про язык (lang), верните QuestionEnum.ASK_LANGUAGE
    Если хотите спросить про высшее образование (degree), верните QuestionEnum.ASK_DEGREE
    Если хотите спросить про ОС (OS), верните QuestionEnum.ASK_OS

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
                elif c.os == OSEnum.MACOS:
                    return QuestionEnum.HIRE

        # elif c.lang == LanguageEnum.CPP: ...

    # elif c.level == LevelEnum.MIDDLE: ...

    # do not hire
    return QuestionEnum.DECLINE


def entropy(class_probabilities: List[float]) -> float:
    """
    Вычислите энтропию как сумму следующих величин: -p_i*log2(p_i)

    Договоримся, что, если p_i == 0, то -p_i*log2(p_i) = 0

    Длина списка: len(class_probabilities)
    """
