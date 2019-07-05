from sklearn.cluster import KMeans

f=[[1],[2],[4],[8],[9]]
cls=KMeans(n_clusters=2)
t=cls.fit(f)
res=t.predict(f)
print(cls.labels_)
print(cls.cluster_centers_)
print(res)
