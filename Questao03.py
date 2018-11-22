class Pilha:
      def __init__(self):
            self.lista = []
            qtdMax = 10
            

            print("A quantidade máxima é de 10 itens")

      def push(self, valor):
            if len(self.lista)<10:
                  self.lista.append(valor)

            else:
                  print("A quantidade máxima de itens já foi atiginda")

      def pop(self):
            if(not(self.isEmpty ())):
                  return self.lista.pop()

      def isEmpty(self):
            return len(self.lista)==0

      def length(self):
            return len(self.lista)

      def peek(self):
            if(not(self.isEmpty())):
                  return self.lista[-1]

pilha = Pilha()
pilha.push(10)
pilha.push(7)
pilha.push(5)
pilha.push(7)
pilha.push(7)
pilha.push(7)
pilha.push(7)
pilha.push(7)
pilha.push(7)
pilha.push(9)
pilha.push(100)
print (pilha.lista)
