import torch
a=torch.tensor([[          [[0,1],[2,3],[4,5]],
                [[6,7],[8,9],[10,11]],
                 [[12,13],[14,15],[16,17]]
                           ]])
print(a, a.shape)
a2=torch.transpose(a,0,3)
a3=torch.squeeze(a2)
print(a3,a3.shape)
