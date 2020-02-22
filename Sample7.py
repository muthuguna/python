from Calculator import Calculate
import sys

cal = Calculate(72, 36)
print(cal.add())
print(cal.sub())
print(cal.multipy())
print(cal.div())

for p in sys.path:
    print(p)