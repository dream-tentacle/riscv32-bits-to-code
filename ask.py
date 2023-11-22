from utils import getrules, explain, codes

rules = getrules(codes)

x = input()
while x != "":
    print(explain(rules, x, base=16))
    x = input()
