from sklearn.cluster import KMeans

f=[[1,100,5],[2,200,8],[4,500,2],[8,400,3],[9,500,9]]
cls=KMeans(n_clusters=2)
t=cls.fit(f)
res=t.predict(f)
print(cls.labels_)
print(cls.cluster_centers_)
print(res)
