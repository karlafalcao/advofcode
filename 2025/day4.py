input_t = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''

file = open('day4input.txt')
input = file.read()
file.close()
input_parsed = input.split('\n')


rolls_of_paper_matrix_orig = input_parsed[:-1]
print(rolls_of_paper_matrix_orig)

def nav_matrix(rolls_of_paper_matrix):
  totalSum = 0
  rolls_of_paper_matrix_trans = rolls_of_paper_matrix.copy()
  for i,row in enumerate(rolls_of_paper_matrix):
    colsCount = len(row)
    for j,col in enumerate(row):
      if col == '.' or col == 'x': continue

      surroundWords = []

      for dir in directions:
        wordChars = []

        # print(xC, yC, directions[dir])
        xC = i + directions[dir][0]
        yC = j + directions[dir][1]

        if xC < 0 or xC > colsCount-1 or yC < 0 or yC > colsCount-1: continue

        # check if it has a paper roll
        if rolls_of_paper_matrix[xC][yC] == '@':
          surroundWords.append(rolls_of_paper_matrix[xC][yC])
      
      # rolls of papers surrounding
      
      if len(surroundWords) < 4:
        
        totalSum += 1
        print(f"\nBEFORE:surroundWords:{row}", surroundWords, len(surroundWords))
        rolls_of_paper_matrix_trans[i] = ''.join(rolls_of_paper_matrix_trans[i][:j] + 'x' + rolls_of_paper_matrix_trans[i][j+1:])
        print(f"\nAFTER:surroundWords:{rolls_of_paper_matrix_trans[i]}", surroundWords, len(surroundWords))
        # print(rolls_of_paper_matrix_trans)
        # store idxs

  # print(totalSum)
  return totalSum, rolls_of_paper_matrix_trans



directions = {
  'up': [ -1, 0 ],
  'down': [ 1, 0 ],
  'left': [ 0, -1 ],
  'right': [ 0, 1 ],
  'upleft': [ -1, -1 ],
  'upright': [ -1, 1 ],
  'downleft': [ 1, -1 ],
  'downright': [ 1, 1 ]
}
if __name__ == '__main__':
  total_sum = 0

  total_sum_matrix, rolls_of_paper_matrix = nav_matrix(rolls_of_paper_matrix_orig)
  print(total_sum_matrix, [print(f'\n{row}') for row in rolls_of_paper_matrix])
  total_sum += total_sum_matrix

  total_sum_matrix, rolls_of_paper_matrix = nav_matrix(rolls_of_paper_matrix)
  print(total_sum_matrix)
  total_sum += total_sum_matrix

  while total_sum_matrix != 0:
    total_sum_matrix, rolls_of_paper_matrix = nav_matrix(rolls_of_paper_matrix)
    print(total_sum_matrix)
    total_sum += total_sum_matrix
  

  print('total_removed:', total_sum)

