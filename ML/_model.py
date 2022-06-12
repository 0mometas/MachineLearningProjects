from typing import Union

import numpy as np
import pandas as pd
from MachineLearningProjects._manipulation import Manipulation
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline


class MyRegression(Manipulation):

    def get_data(self, data):
        return self.read_data(data)

    def find_best_model(self,
                        train_data: Union[str, pd.DataFrame],
                        feature_cols: str,
                        label_col: str,
                        clf1=KNeighborsRegressor(),
                        clf2=RandomForestRegressor()):

        data = self.read_data(train_data)
        X = data[feature_cols]
        y = data[label_col]

        param1 = {"classifier__algorithm": ["auto"],
                  "classifier__leaf_size": np.arange(5, 45, 5),
                  "classifier__n_neighbors": np.arange(2, 22, 2),
                  "classifier__weights": ["uniform", "distance"],
                  "classifier": [clf1]}

        # Needed change to Regression parameters
        param2 = {'classifier__n_estimators': [10, 50, 100, 250],
                  'classifier__max_depth': [5, 10, 20],
                  'classifier': [clf2]}

        pipeline = Pipeline(steps=[("classifier", clf1)])
        params = [param1, param2]

        k_fold = KFold(n_splits=5, shuffle=True, random_state=4)

        grid = GridSearchCV(pipeline,
                            params,
                            cv=k_fold,
                            scoring='r2',
                            n_jobs=-1)
        grid.fit(X, y)

        return grid.best_params_

    def predict_best_result(self,
                            train_data: Union[str, pd.DataFrame],
                            test_data: Union[str, pd.DataFrame],
                            feature_cols: str,
                            label_col: str):

        test_data = self.get_data(data=test_data)

        best_model = self.find_best_model(train_data,
                                          feature_cols,
                                          label_col)

        prediction_result = best_model.predict(test_data[feature_cols])

        result = pd.DataFrame({"test feature": test_data[feature_cols],
                               "prediction_result": prediction_result})

        return result
