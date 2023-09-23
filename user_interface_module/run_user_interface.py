from flask import Flask, request, jsonify

app = Flask(__name__)

class UserInterfaceModule:

    def __init__(self, evaluation_module):
        self.evaluation_module = evaluation_module

    def format_evaluation_results(self, evaluation_results):
        if evaluation_results is None:
            return "Не удалось получить результаты оценки"

        formatted_results = f"""
        Результаты оценки модели:
        - Средняя абсолютная ошибка (MAE): {evaluation_results['MAE']}
        - Среднеквадратическая ошибка (MSE): {evaluation_results['MSE']}
        - Коэффициент детерминации (R2): {evaluation_results['R2']}
        """
        return formatted_results

    def get_evaluation_results(self):
        # Здесь можно добавить логику для получения X_test и y_test
        # и передачи их в модуль оценки для получения результатов оценки

        # Пример (предполагается, что model, X_test и y_test уже определены):
        # evaluation_results = self.evaluation_module.evaluate_model(model, X_test, y_test)
        # return self.format_evaluation_results(evaluation_results)

        # Временный ответ, пока не будет настроена интеграция с другими модулями
        return "Функционал в разработке"

# Создание экземпляра класса EvaluationModule (предполагается, что класс уже определен)
# eval_module = EvaluationModule()

# Создание экземпляра класса UserInterfaceModule
# ui_module = UserInterfaceModule(eval_module)

@app.route('/get_evaluation_results', methods=['GET'])
def get_evaluation_results():
    # Предполагается, что ui_module уже определен и инициализирован
    # response = ui_module.get_evaluation_results()
    
    # Временный ответ, пока не будет настроена интеграция с другими модулями
    response = "Функционал в разработке"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
