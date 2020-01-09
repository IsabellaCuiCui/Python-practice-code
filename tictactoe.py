"""
建立一个超简易版井字棋游戏
source：《python编程快速上手-繁琐工作自动化》
"""
#初始化九宫格名称
theboard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
		'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
		'low-L':' ', 'low-M':' ', 'low-R':' '}

#初始化井字棋盘
def printBoard(board):
	print('\t' + board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']) #加t的原因是不希望井字格显示太靠边
	print('\t' + '-+-+-')
	print('\t' + board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('\t' + '-+-+-')
	print('\t' + board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
  
#正式开始游戏
theboard = {'top-L':'O', 'top-M':' ', 'top-R':' ',
		'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
		'low-L':' ', 'low-M':'X', 'low-R':' '} 

printBoard(theboard)
