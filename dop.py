def ten(num,b): #перевод из 10 сс
    newNum = ''
    while num > 0:
        newNum = str(num % b) + newNum
        num //= b
    return (newNum)
def per(a,v,iz):
        num=0
        s=[]
        for i in a: #делает список заменяя буквы числами
            if i in g:
               i = g[i]
            if int(i)>=iz:
                return "недопустимое число"
            s.append(i)
        s=s[::-1]
        for i in range(0,len(s)): #перевод в 10 cc
            num=num+int(s[i])*(int(iz)**i)
        return ten(num,v)
g={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
if __name__ == "__main__":
   a,iz,v=input("введите число и системы счисления (сначала из какой переводить потом в какую) через пробел ").split(" ")
   print(per(a,int(v),int(iz)))
