# Lecture Note for Programming Challenges - 3/3/2019

## More advanced Python stuff

### For-Loop Revisited

```python
ar = [1, 3, 5, 7, 11]
total = 0
for i in range(len(ar)):
    if i % 2 == 0:
        total += ar[i]
print(total)
```
