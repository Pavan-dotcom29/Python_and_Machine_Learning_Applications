import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy

df = pd.DataFrame({
	"x":[185,170,168,179,182,188,180,180,183,180,180,177],
	"y":[72,56,60,68,72,77,71,70,84,88,67,76]
	})

print("Step 1 : Initailsation -KMeans(Centroids) at generated at random")

print("Data set for training")
print(df)

np.random.seed(200)
k = 2

centroids = {
	i+1 : [np.random.randint(0,80),np.random.randint(0,80)]
	for i in range(k)
}

print("Random centroids generated")
print(centroids)

fig = plt.figure(figsize=(5,5))
plt.scatter(df["x"],df["y"],color="k")

colormap = {1:'red',2:'green'}
for i in centroids.keys():
	plt.scatter(*centroids[i],color=colormap[i])
	#print(ret1)

plt.title("Marvellous : Data set with random centroid")

ret2 = plt.xlim(0,80)
print(ret2)
ret3 = plt.ylim(0,80)
print(ret3)


def assignment(df,centroids):
	for i in centroids.keys():
		#sqrt
		df['distance_from_{}'.format(i)] = (
			np.sqrt(
				(df['x']-centroids[i][0])**2
				+(df['y']-centroids[i][1])**2
				)
			)

	centroids_distance_cols = ["distance_from_{}".format(i) for i in centroids.keys()]

	df['closest'] = df.loc[:,centroids_distance_cols].idxmin(axis=1)

	df['closest'] = df['closest'].map(lambda x : int(x.lstrip('distance_from_')))

	df['color'] = df['closest'].map(lambda x:colormap[x])
	return df


print("Step 2 : K-Cluster are created by associating each observation with the nearest centroid")

print("Before assignment dataset")
print(df)
df = assignment(df,centroids)

print("First centroid : red" )
print("Second centroid : green")

print("After assignment dataset")
print(df)

fig = plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroids.keys():
	plt.scatter(*centroids[i],color=colormap[i])
plt.xlim(0,80)
plt.ylim(0,80)
print("Marvellous : Dataset with clustering and random centroids")
plt.show()

old_centroids = copy.deepcopy(centroids)
print("Step3 Update : The centroid of the cluster become new mean assignment and update alternatively")

def update(k):
	print("Old values of centroids")
	print(k)

	for i in centroids.keys():
		centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
		centroids[i][1] = np.mean(df[df['closest'] == i]['y'])

	print("New values of centroids")
	print(k)
	return k

centroids = update(centroids)

fig = plt.figure(figsize=(5,5))
ax = plt.axes()
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroids.keys():
	plt.scatter(*centroids[i],color=colormap[i])
plt.xlim(0,80)
plt.ylim(0,80)

for i in old_centroids.keys():
	old_x = old_centroids[i][0]
	old_y = old_centroids[i][1]
	dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
	dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
	ax.arrow(old_x,old_y,dx,dy,head_width=2,head_length=3,fc=colormap[i],ec=colormap[i])

plt.title("Marvellous : Dataset with clustering and updated centroids")
plt.show()

fig = plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroids.keys():
	plt.scatter(*centroids[i],color=colormap[i])
plt.xlim(0,80)
plt.ylim(0,80)
plt.title("Marvellous : Dataset with clustering and updated centroids")
plt.show()

while True:
	closest_centroids = df['closest'].copy(deep=True)
	centroids = update(centroids)
	print("Before assignment dataset")
	print(df)
	df = assignment(df,centroids)
	print(df)
	if closest_centroids.equals(df['closest']):
		break

print("Final values of centroids")
print(centroids)
fig = plt.figure(figsize=(5,5))
plt.scatter(df['x'],df['y'],color=df['color'],alpha=0.5,edgecolor='k')
for i in centroids.keys():
	plt.scatter(*centroids[i],color=colormap[i])
plt.xlim(0,80)
plt.ylim(0,80)
plt.title("Marvellous : Final data set centroids")
plt.show()