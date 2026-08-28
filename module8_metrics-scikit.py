import numpy as np
from sklearn.metrics import precision_score, recall_score


class MetricsCalculator:
    def __init__(self):
        self.y_true = np.array([], dtype=int)
        self.y_pred = np.array([], dtype=int)

    def insert(self, x, y):
        self.y_true = np.append(self.y_true, x)
        self.y_pred = np.append(self.y_pred, y)

    def precision(self):
        return precision_score(self.y_true, self.y_pred)

    def recall(self):
        return recall_score(self.y_true, self.y_pred)


def main():
    metrics = MetricsCalculator()

    n = int(input("Enter N (positive integer): "))

    for i in range(n):
        x = int(input(f"Enter x (ground truth, 0 or 1) for point #{i + 1}: "))
        y = int(input(f"Enter y (predicted, 0 or 1) for point #{i + 1}: "))
        metrics.insert(x, y)

    print(metrics.precision())
    print(metrics.recall())


if __name__ == "__main__":
    main()
