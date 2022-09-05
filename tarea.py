class Vertice:
  def __init__(self, i):
    self.id = i
    self.visitado = False
    self.nivel = -1
    self.padre = None
    self.vecinos = []

  def agregaVecino(self, v):
    if v not in self.vecinos:
      self.vecinos.append(v)

class Grafica:
  def __init__(self):
    self.vertices = {}

  def agregaVertice(self,v):
    if v not in self.vertices:
      self.vertices[v] = Vertice(v)

  def agregarArista(self,a,b):
    if a in self.vertices and b in self.vertices:
      self.vertices[a].agregaVecino(b)
      self.vertices[b].agregaVecino(a)

  def dfs(self,r):
    if r in self.vertices:
      self.vertice[r].visitado = True


      for nodo in self.vertices[r].vecinos:
        if self.vertices[nodo].visitado == False:
          self.vertices[nodo].padre = r
          print("(" + str(nodo) + "," + str(r) + ")")
          self.dfs(nodo)

def main():
  g = Grafica()

  l = [1,2,3,4,5,6,7,8]

  for v in l:
    g.agregaVertice(v)

  l = [1,2,1,5,1,8,2,3,2,5,2,6,3,4,3,6,3,7,4,7,4,8,8,1]
  for i in range (0,len(l) -1,2):
    g.agregarArista(l[i],l[i+1])

  print("(1,NULL)")
  g.dfs(1)
  
main()