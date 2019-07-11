from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
f=[[40,60],[50,50],[70,35],[35,65],[70,70],[70,90],[80,95],[85,75],[90,90]]
l=['P','P','P','P','G','G','G','G','G']

clf=MLPClassifier(hidden_layer_sizes=(7,6,5,4,3,2),random_state=1,max_iter=1000,solver='adam',learning_rate_init=0.001,activation='relu',learning_rate='constant')
t=clf.fit(f,l)
res=t.predict(f)
print(res)
plt.plot(f)
plt.show()
