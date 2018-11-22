class Pilha:
      def __init__(self,lista):
            self.soma = 0
            self.lista = lista

      def push(self):
            for i in range(len(self.lista)):
                  self.soma = self.soma + self.lista[i]

            print("A soma dos itens é igual a: %d"%(self.soma))
            return ""

      def pop(self):
            for i in range(len(self.lista)):
                  if(not(self.isEmpty ())):
                        self.lista.pop()
            return self.lista

      def isEmpty(self):
            return len(lista)==0

      def length(self):
            return len(self.lista)

      def peek(self):
            if(not(self.isEmpty())):
                  return self.lista[-1]

lista = [1,2,3,4,5,6,7,8,9,10]
print("Nossa lista: ", lista)
pilha = Pilha(lista)
print (pilha.push())
pilha.pop()
print ("Nossa lista desempilhada: ", pilha.lista)
