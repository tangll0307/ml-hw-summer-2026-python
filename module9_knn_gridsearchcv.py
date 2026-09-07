import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, PredefinedSplit
from sklearn.metrics import accuracy_score


def read_pairs(n, set_name):
    X = np.empty(n, dtype=float)
    Y = np.empty(n, dtype=int)
    for i in range(n):
        x_val = float(input(f"{set_name} pair {i + 1}/{n} - enter x: "))
        y_val = int(input(f"{set_name} pair {i + 1}/{n} - enter y (non-negative integer class): "))
        X[i] = x_val
        Y[i] = y_val
    return X, Y


def main():
    n = int(input("Enter N, the size of the training set TrainS: "))
    x_train, y_train = read_pairs(n, "TrainS")

    m = int(input("Enter M, the size of the test set TestS: "))
    x_test, y_test = read_pairs(m, "TestS")

    X_train = x_train.reshape(-1, 1)
    X_test = x_test.reshape(-1, 1)

    X_all = np.vstack([X_train, X_test])
    y_all = np.concatenate([y_train, y_test])
    test_fold = np.concatenate([
        np.full(n, -1),
        np.full(m, 0),
    ])
    predefined_split = PredefinedSplit(test_fold)

    max_k = min(10, n)
    param_grid = {"n_neighbors": list(range(1, max_k + 1))}

    grid_search = GridSearchCV(
        estimator=KNeighborsClassifier(),
        param_grid=param_grid,
        cv=predefined_split,
        scoring="accuracy",
        refit=False,
    )
    grid_search.fit(X_all, y_all)

    best_k = grid_search.best_params_["n_neighbors"]

    best_model = KNeighborsClassifier(n_neighbors=best_k)
    best_model.fit(X_train, y_train)
    y_pred = best_model.predict(X_test)
    best_accuracy = accuracy_score(y_test, y_pred)

    print("\n--- kNN Hyperparameter Search Results (k = 1..10) ---")
    for k, score in sorted(zip(param_grid["n_neighbors"], grid_search.cv_results_["mean_test_score"])):
        print(f"k = {k:2d} -> test accuracy = {score:.4f}")

    print(f"\nBest k: {best_k}")
    print(f"Best test accuracy: {best_accuracy:.4f}")


if __name__ == "__main__":
    main()
