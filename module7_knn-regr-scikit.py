import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class KNNRegressor:
    def __init__(self):
        self.X = np.array([])
        self.Y = np.array([])

    def insert(self, x, y):
        self.X = np.append(self.X, x)
        self.Y = np.append(self.Y, y)

    def predict(self, x_query, k):
        n = len(self.X)
        if k > n:
            return None
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(self.X.reshape(-1, 1), self.Y)
        prediction = model.predict(np.array([[x_query]]))
        return prediction[0]

    def label_variance(self):
        return np.var(self.Y)


def main():
    model = KNNRegressor()

    n = int(input("Enter N (positive integer): "))
    k = int(input("Enter k (positive integer): "))

    for i in range(n):
        x = float(input(f"Enter x value for point #{i + 1}: "))
        y = float(input(f"Enter y value for point #{i + 1}: "))
        model.insert(x, y)

    x_query = float(input("Enter X: "))

    if k <= n:
        result = model.predict(x_query, k)
        print(result)
        print(model.label_variance())
    else:
        print("Error: k must be less than or equal to N.")


if __name__ == "__main__":
    main()
