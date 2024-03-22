# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def remq(a,p):
    a.pop(p+1)
    a.pop(p)
    a.pop(p-1)
    return a
q=input()
s="9*8/7+6*5-4*2+9/3"
print(s)
a=[]
k=0
for i in range(len(s)):
    if not s[i].isnumeric():
        a.append(str(s[k:i]))
        a.append(str(s[i]))
        k=i+1
    if i==len(s)-1:
        a.append(str(s[k:]))

while "*" in a:
    p=a.index("*")
    res=float(a[p-1])*float(a[p+1])
    a=remq(a,p)
    a.insert(p-1,res)
    print(res,a)
while "/" in a:
    p=a.index("/")
    res=float(a[p-1])/float(a[p+1])
    print(float(a[p-1])%float(a[p+1]))
    a = remq(a, p)
    a.insert(p-1,res)
    print(res,a)
res=a[0]
for i in range(len(a)):
    if a[i]=="+":
        res+=a[i+1]
        print(res)
    if a[i]=="-":
        res-=a[i+1]
        print(res)
print(res)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
