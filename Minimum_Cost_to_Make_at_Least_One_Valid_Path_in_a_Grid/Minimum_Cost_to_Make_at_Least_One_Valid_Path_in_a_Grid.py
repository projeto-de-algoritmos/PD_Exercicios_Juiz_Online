from collections import deque

class Solution:
    def minCost(self, grade):

        num_linhas, num_colunas = len(grade), len(grade[0])
        
        custos = [[float('inf')] * num_colunas for _ in range(num_linhas)]
        
        custos[0][0] = 0
        
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        fila = deque([(0, 0)])
        
        while fila:

            x, y = fila.popleft()
            
            for i, (dx, dy) in enumerate(direcoes):

                novo_x, novo_y = x + dx, y + dy
                
                if 0 <= novo_x < num_linhas and 0 <= novo_y < num_colunas:

                    custo = custos[x][y] if grade[x][y] == i + 1 else custos[x][y] + 1
                    
                    if custo < custos[novo_x][novo_y]:

                        custos[novo_x][novo_y] = custo
                        
                        if grade[x][y] == i + 1:
                            fila.appendleft((novo_x, novo_y))
                        else:
                            fila.append((novo_x, novo_y))
                            
        return custos[num_linhas - 1][num_colunas - 1]
