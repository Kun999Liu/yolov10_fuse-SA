import numpy as np

m0 = np.array([[1,2,3],[4,5,6]])
gt_classes = [0,0,0]
for i, gc in enumerate(gt_classes):
    j = m0 == i
    print('i',i)
    print('m0',m0)
    print('j',j)
    print('sum(j)',sum(j))