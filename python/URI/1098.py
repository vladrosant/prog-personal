def format_float(num):
    return f"{num:.1f}".rstrip("0").rstrip(".")

x=0
y=1

while x<=2:
    for i in range(3):
        print(f"I={format_float(x)} J={format_float(y)}")
        y+=1
    x+=0.2
    y+=0.2
    y-=3