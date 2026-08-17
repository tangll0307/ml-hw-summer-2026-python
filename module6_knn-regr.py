import numpy as np


class KNNRegressor:
    """k-NN Regression using NumPy for data storage and computation."""

    def __init__(self, n_points):
        # Data initialization
        self.n_points = n_points
        self.X = np.empty(n_points, dtype=float)
        self.Y = np.empty(n_points, dtype=float)
        self._count = 0

    def insert(self, x, y):
        # Data insertion
        if self._count >= self.n_points:
            raise ValueError("All N points have already been inserted.")
        self.X[self._count] = x
        self.Y[self._count] = y
        self._count += 1

    def predict(self, x_query, k):
        # Data calculation (k-NN regression prediction)
        if k > self.n_points:
            raise ValueError(f"k ({k}) cannot be greater than N ({self.n_points}).")

        distances = np.abs(self.X - x_query)  # Euclidean distance in 1D
        nearest_indices = np.argsort(distances)[:k]
        prediction = np.mean(self.Y[nearest_indices])
        return prediction


def main():
    n = int(input("Enter N (positive integer): "))
    k = int(input("Enter k (positive integer): "))

    regressor = KNNRegressor(n)

    for i in range(n):
        x = float(input(f"Enter x value for point #{i + 1}: "))
        y = float(input(f"Enter y value for point #{i + 1}: "))
        regressor.insert(x, y)

    x_query = float(input("Enter X: "))

    if k <= n:
        result = regressor.predict(x_query, k)
        print(result)
    else:
        print("Error: k cannot be greater than N.")


if __name__ == "__main__":
    main()
