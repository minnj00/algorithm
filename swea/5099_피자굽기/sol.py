import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    pizza = list(input().split())
    pizza_idx = [[i+1, pizza[i]] for i in range(len(pizza))]
    fire = []

    # while len(pizza):
    # for i in range(N):
    #     fire.append(pizza_idx[0])
    #     pizza_idx.remove(pizza_idx[0])
    # print(pizza_idx)
    # print(fire)
            

    while len(fire) != 1:
        while True:
            if fire[0] == 0:
                fire[0] = pizza_idx[0]
        
            fire[i]=fire[i-1]
                
            for i in range(len(fire)):
                    fire[i] = fire[i]//2




        
        
