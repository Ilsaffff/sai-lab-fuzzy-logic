import json
import math
import os.path
from collections import Counter
from enum import Enum
import random
from typing import Optional, List, Any

from utils import load_module

OUT_STORAGE = "out_storage"
INPUT_STORAGE = "in_storage"
TEMPLATE_FILES_DIR = "task_templates"

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
    R = "r"


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


def get_text_task_1():
    return "Отправляем тебе задание 1, вот инструкция:"


def get_template_file_task_1():
    return f"{TEMPLATE_FILES_DIR}/task_1.py"


def test_task_1(user_id: int):
    message = None
    success = True
    error = None
    points = 5
    candidate_no_attributes = Candidate()
    try:
        user_file = os.path.join(OUT_STORAGE,
                                 f"task_1_{user_id}.py")
        module = load_module(user_file)
        func = module.select

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

    RESULTS["task_1"].append({
        "user_id": user_id,
        "success": success,
        "points": points,
        "error": error,
    })
    return message


def get_text_task_2():
    return "Отправляем тебе задание 2, вот инструкция:"


def get_photo_file_task_2() -> str:
    return f"{INPUT_STORAGE}/task_2.png"


def get_template_file_task_2() -> str:
    return f"{TEMPLATE_FILES_DIR}/task_2.py"


def test_task_2(user_id: int):
    success = True
    error = None

    def valid_entropy(class_probabilities: List[float]) -> float:
        return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)

    random_class_probabilities = [random.randint(0, 10) / 10 for i in range(10)]
    try:
        user_file = os.path.join(OUT_STORAGE,
                                 f"task_2_{user_id}.py")
        module = load_module(user_file)
        func = module.entropy

        if valid_entropy(random_class_probabilities) == func(
                random_class_probabilities):
            message = "Твой код отлично сработал, держи баллллы"
            points = 5
        else:
            points = 3
            message = "Ты почти справился, не максимум баллов, конечно, но тоже хорошо справился!"
    except Exception as e:
        message = f"Ууупс, твой код упал с ошибкой: {e}"
        success = False
        error = str(e)
        points = 0
    RESULTS["task_2"].append({
        "user_id": user_id,
        "success": success,
        "points": points,
        "error": error,
    })
    return message


def get_text_task_3():
    return "Отправляем тебе задание 3, вот инструкция:"


def get_template_file_task_3():
    return f"{TEMPLATE_FILES_DIR}/task_3.py"


def test_task_3(user_id: int):
    success = True
    error = None

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
    try:
        user_file = os.path.join(OUT_STORAGE,
                                 f"task_3_{user_id}.py")
        module = load_module(user_file)
        func = module.data_entropy
        if valid_data_entropy(random_class_probabilities) == func(
                random_class_probabilities):
            message = "Твой код отлично сработал, держи баллллы"
            points = 5
        else:
            message = "Ты почти справился, не максимум баллов, конечно, но тоже хорошо справился!"
            points = 3
    except Exception as e:
        message = f"Ууупс, твой код упал с ошибкой: {e}"
        success = False
        error = str(e)
        points = 0

    RESULTS["task_3"].append({
        "user_id": user_id,
        "success": success,
        "points": points,
        "error": error,
    })

    return message


def save_results():
    with open("grade.json", "w") as f:
        json.dump(RESULTS, f)



