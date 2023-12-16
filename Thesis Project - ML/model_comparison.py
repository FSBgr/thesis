import matplotlib.pyplot as plt

f1_scores = [56.7, 76.01, 53.86]
balanced_accuracy = [60.1, 72.96, 64.12]
precision = [54.3, 73.73, 54.86]
recall = [62.3, 79.2, 66.42]
classifiers = ['KNN', 'Random Forest', 'LSVM']

figure, axis = plt.subplots(2, 2, figsize=(15,15))
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
axis[0, 0].bar(classifiers, f1_scores, color=['black', 'red', 'green'])
axis[0,1].bar(classifiers, balanced_accuracy, color=['black', 'red', 'green'])
axis[1,0].bar(classifiers, precision, color=['black', 'red', 'green'])
axis[1,1].bar(classifiers, recall, color=['black', 'red', 'green'])
axis[0, 0].set_title("F1-scores")
axis[0,1].set_title("Balanced Accuracy")
axis[1,0].set_title("Precision")
axis[1,1].set_title("Recall")
#axis[i, j].set_title(columns[idx], fontsize='large')
#idx+=1
plt.savefig("modelComparison.png", bbox_inches='tight', pad_inches=0.2) # enable only if you want to save the image
plt.show()