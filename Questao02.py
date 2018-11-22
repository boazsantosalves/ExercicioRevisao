class Pilha:
      def __init__(self):
            self.lista = []
            self.tem = 0

      def push(self, valor):
            for i in range(len(self.lista)):
                  if valor==self.lista[i]:
                        self.tem = 1
            if self.tem==0:
                  self.lista.append(valor)

            self.tem = 0

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
pilha.push(9)
print (pilha.lista)
