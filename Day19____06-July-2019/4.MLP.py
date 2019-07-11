from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
f=[[40,60],[50,50],[70,35],[35,65],[70,70],[70,90],[80,95],[85,75],[90,90]]
l=['P','P','P','P','G','G','G','G','G']

clf=MLPClassifier(hidden_layer_sizes=(5,4,3),random_state=1,max_iter=1000,solver='adam',learning_rate_init=0.001,activation='relu')
t=clf.fit(f,l)
res=t.predict([[60,45],[65,40],[85,90],[90,80],[60,65]])
print(res)
plt.plot(f)
plt.show()
