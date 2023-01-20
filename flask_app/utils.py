import pickle
import pandas as pd
import datetime

class Predictions:
    def __init__(self, model_name: str) -> None:
        """
        Iitializes model with name and loads with pickle
        """
        with open(
            rf"./models/{model_name}.pckl",
            "rb",
        ) as model:
            try:
                self.model = pickle.load(model)
            except OSError:
                print("Wrog path or model not available")
                exit(-1)

    def predict(self, prev_date: str):
        """
        Predicts oil prices for next date
        """
        self.next_date = datetime.datetime(
            *list(map(lambda x: int(x), prev_date.split("-")))
        ) + datetime.timedelta(
            days=1
        )  # next date

        # preprocess date
        next_date_series = pd.DataFrame(
            {"ds": pd.date_range(start=self.next_date, end=self.next_date)}
        )

        pred = self.model.predict(next_date_series)
        return pred

    def get_next_date(self):
        """
        Returns the date to be predicted
        """
        return self.next_date.strftime("%y-%m-%d")

    def plot(self, pred):
        """
        Plot oil prices predicted
        """
        self.model.plot(pred)