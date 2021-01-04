from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from matplotlib.image import imread

import numpy as np
import pickle


def get_data(path, dir):
    data = []
    label = []

    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(' ')
            data.append(imread(dir + line[0]))
            label.append(line[1][:-1])

    return data, label

if __name__ == "__main__":
    directory = "D:/etc prof jang/Pytorch_Retinaface-master/results/"
    data, label = get_data(directory + "list.txt", directory)
    data = np.array(data * 10)
    data = data.reshape(data.shape[0], -1)
    label = np.array(label * 10)

    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.05, random_state=0)

    # sc = StandardScaler()
    # x_train_std = sc.fit_transform(x_train)
    # x_test_std = sc.transform(x_test)

    forest = RandomForestClassifier(n_estimators=1000, n_jobs=3, random_state=1)
    forest.fit(x_train, y_train)

    y_pred = forest.predict(x_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    save_path = "D:/etc prof jang/Pytorch_Retinaface-master/weights/random_forest.sav"
    pickle.dump(forest, open(save_path, 'wb'))




