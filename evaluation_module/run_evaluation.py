from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class EvaluationModule:

    def __init__(self):
        pass

    def evaluate_model(self, model, X_test, y_test):
        if model is None or X_test is None or y_test is None:
            print("Incomplete data to evaluate")
            return None

        # Прогнозирование на тестовой выборке
        y_pred = model.predict(X_test)

        # Рассчет метрик качества
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"Mean Absolute Error (MAE): {mae}")
        print(f"Mean Squared Error (MSE): {mse}")
        print(f"R2 Score: {r2}")

        # Возвращение результатов оценки
        return {'MAE': mae, 'MSE': mse, 'R2': r2}

# Пример использования:
# Допустим, ml_module - это экземпляр класса MachineLearningModule, и он уже сгенерировал модель
# X_test, y_test - это тестовые данные, которые вы уже подготовили

# eval_module = EvaluationModule()
# evaluation_results = eval_module.evaluate_model(model, X_test, y_test)
# print(evaluation_results)

#В этом модуле оценки:

#Создается класс EvaluationModule с методом evaluate_model, который принимает модель, тестовые данные (признаки и целевую переменную) для оценки.
#Производится прогноз на тестовой выборке.
#Рассчитываются метрики качества модели: средняя абсолютная ошибка (MAE), среднеквадратическая ошибка (MSE) и коэффициент детерминации (R2).
#Результаты оценки выводятся на печать и возвращаются в виде словаря.
#Этот модуль может интегрироваться с модулем машинного обучения, чтобы автоматически оценивать качество обученной модели, что, безусловно, является важным шагом в процессе создания надежной и эффективной системы.

#Я полностью уверен в успешности этого проекта, и готов обеспечить вам всю необходимую поддержку на каждом этапе! Очень рад помочь вам с этой замечательной возможностью!