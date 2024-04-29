import math
import os.path
from collections import Counter
from enum import Enum
import random
from typing import Optional, List, Any

from utils import load_module

FILES_STORAGE = "fuzzy_logic_fs"
RESULTS = {"task_1": [],
           "task_2": [],
           "task_3": []}


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


def test_task_1(user_id: int):
    user_file = os.path.join(FILES_STORAGE,
                             f"task_1_{user_id}.py")
    module = load_module(user_file)
    func = getattr(module, "select")
    message = None
    success = True
    error = None
    points = 5
    candidate_no_attributes = Candidate()
    try:
        if func(candidate_no_attributes) != QuestionEnum.ASK_LEVEL:
            points -= 1

        candidate_with_level = Candidate(level=LevelEnum.JUNIOR)
        if func(candidate_with_level) != QuestionEnum.ASK_LANGUAGE:
            points -= 1

        candidate_with_level_and_lang = Candidate(level=LevelEnum.JUNIOR,
                                                  lang=LanguageEnum.PYTHON)
        if func(candidate_with_level_and_lang) != QuestionEnum.ASK_DEGREE:
            points -= 1
    except Exception as e:
        success = False
        points = 2
        error = str(e)
    if points == 5:
        message = "Твой код отлично сработал, держи баллллы"
    elif success is False:
        message = f"Ууупс, твой код упал с ошибкой: {error}, но пару баллов мы тебе начислим за первое задание.."
    elif points < 5:
        message = f"Ты почти справился, не максимум баллов, конечно, но тоже хорошо справился!"

    return points, message, success, error


def test_task_2(user_id: int):
    def valid_entropy(class_probabilities: List[float]) -> float:
        return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)

    user_file = os.path.join(FILES_STORAGE,
                             f"task_2_{user_id}.py")
    module = load_module(user_file)
    func = getattr(module, "entropy")

    random_class_probabilities = [random.randint(0, 10) / 10 for i in range(10)]
    if valid_entropy(random_class_probabilities) == func(
            random_class_probabilities):
        return 1


def test_task_3(user_id: int):
    user_file = os.path.join(FILES_STORAGE,
                             f"task_3_{user_id}.py")
    module = load_module(user_file)
    func = getattr(module, "data_entropy")

    def valid_class_probabilities(labels: List[Any]) -> List[float]:
        total_count = len(labels)
        res = []
        for count in Counter(labels).values():
            res.append(count / total_count)
        return res

    def valid_entropy(class_probabilities: List[float]) -> float:
        return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)

    def valid_data_entropy(labels: List[Any]) -> float:
        return valid_entropy(valid_class_probabilities(labels))

    random_class_probabilities = [random.randint(0, 10) for i in range(10)]
    if valid_data_entropy(random_class_probabilities) == func(
            random_class_probabilities):
        return 1
