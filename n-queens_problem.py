'''
Created on 12-Dec-2021

@author: Lucifer
'''
import sys
sys.setrecursionlimit(10**8)
def issafe(row,col,n,board):
    i=row-1
    while i>=0:
        if board[i][col]==1:
            return False 
        i-=1
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False 
        i-=1
        j-=1
    j=col+1
    i=row-1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False 
        j+=1
        i-=1
    return True     
        
        
        
        
                
def nQueenshelper(row,n,board):
    if row==n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()
        print()    
        return 
    for col in range(n):
        if issafe(row,col,n,board):
            board[row][col]=1
            nQueenshelper(row+1, n, board)
            board[row][col]=0
    return                  
    
def nQueens(n):
    board=[[0 for j in range(n)] for i in range(n)]
    nQueenshelper(0,n,board)
n=int(input())
nQueens(n)