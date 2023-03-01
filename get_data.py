import hub
ds = hub.load('hub://activeloop/11k-hands')

# check out the first image and all of its details!
import matplotlib.pyplot as plt
plt.imshow(ds.images[0].numpy())
plt.title(f"aspect_of_hand : {ds.aspect_of_hand[0].numpy()}, id : {ds.id[0].numpy()}, age : {ds.age[0].numpy()}, irregularities : {ds.irregularities[0].numpy()}, accessories : {ds.accessories[0].numpy()}, nail_polish : {ds.nail_polish[0].numpy()},gender : {ds.gender[0].numpy()},skin_color : {ds.skin_color[0].numpy()}")
plt.show()

# # train a model in pytorch
# for sample in ds.pytorch():
#     # ... model code here ...
    
# # train a model in tensorflow
# for sample in ds.tensorflow():
#     # ... model code here ...

# print(ds)
# # prints: Dataset(path='hub://activeloop/11k-hands', read_only=True, tensors=['images', 'aspect_of_hand', 'id', 'age', 'irregularities', 'accessories', 'nail_polish', 'gender', 'skin_color'])