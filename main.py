# main.py
import sys
sys.path.append('./data_analysis_module')
sys.path.append('./data_collection_module')
sys.path.append('./data_processing_module')
sys.path.append('./machine_learning_module')
sys.path.append('./evaluation_module')
sys.path.append('./user_interface_module')

from run_data_analysis import data_analysis_function
from run_data_collection import data_collection_function
from run_data_processing import data_processing_function
from run_machine_learning import machine_learning_function
from run_evaluation import evaluation_function
from run_user_interface import user_interface_function

def main():
    # Запуск функций каждого модуля с уведомлениями
    print("Запуск модуля сбора данных...")
    data_collection_function()
    print("Модуль сбора данных успешно завершен.\n")

    print("Запуск модуля обработки данных...")
    data_processing_function()
    print("Модуль обработки данных успешно завершен.\n")

    print("Запуск модуля анализа данных...")
    data_analysis_function()
    print("Модуль анализа данных успешно завершен.\n")

    print("Запуск модуля машинного обучения...")
    machine_learning_function()
    print("Модуль машинного обучения успешно завершен.\n")

    print("Запуск модуля оценки...")
    evaluation_function()
    print("Модуль оценки успешно завершен.\n")

    print("Запуск модуля интерфейса пользователя...")
    user_interface_function()
    print("Модуль интерфейса пользователя успешно завершен.\n")

if __name__ == "__main__":
    main()
