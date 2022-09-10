import torch
from torch.nn import Linear as L


class MLP(torch.nn.Module):
    def __init__(self, m, n):
        super().__init__()
        self.act = torch.nn.ReLU()
        self.softmax = torch.nn.Softmax(dim=1)
        self.m = m
        self.n = n
        self.h1 = L(self.m, 25000)
        self.h2 = L(25000, 40000)
        self.h3 = L(40000, 3000)
        self.h4 = L(3000, 1500)
        self.output = L(1500, self.n)

    def forward(self, x):
        h1 = self.h1(x)
        r1 = self.act(h1)
        h2 = self.h2(r1)
        r2 = self.act(h2)
        h3 = self.h3(r2)
        r3 = self.act(h3)
        h4 = self.h4(r3)
        r4 = self.act(h4)
        output = self.output(r4)
        output = self.softmax(output)
        return output
