n=int(input(' nhap n: ')
for i in range(0,n+1):
      def fibonaci(i):
          if(i == 1 or i == 2 ):
              return 1
          if i == 0:
              return 0
          return fibonaci(i-1) + fibonaci(i-2)
      l.append(fibonaci(i))
print(l)
          
