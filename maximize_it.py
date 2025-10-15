# question link: https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product
grand_liste = []

def find_max(liste):
    grand_liste.append(liste)

k, m = map(int, input().split())
n = 0
standart = 0
while n < k:
    girdi = list(map(int, input().split()))
    liste = [(j**2) % m for j in girdi[1:]] 
    find_max(liste)
    n+=1

for combo in product(*grand_liste):
    toplam = sum(combo)
    buyuk = toplam%m
    if buyuk >= standart:
        standart = buyuk
print(standart)
