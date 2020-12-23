# Author: EriK Cooke

from GameBoard import GameBoard


def fill_board(board):
	fill_chr = 'A'
	rows = board.get_num_rows()
	cols = board.get_num_columns()
	for row in range(rows):
		for col in range(cols):
			board.set_position(fill_chr, row, col)
			if fill_chr == 'z':
				fill_chr = 'A'
			else:
				fill_chr = (chr(ord(fill_chr) + 1))


def main():
	print("Create 9 X 9 board")
	board = GameBoard(9, 9)
	print("Print empty board")
	board.print_board()
	print("Set an X at position 2,2 ")
	board.set_position('X', 2, 2)
	print("Print board")
	board.print_board()
	print("Get number of rows: " + str(board.get_num_rows()))
	print("Get number of columns: " + str(board.get_num_columns()))
	print("Character at 2, 2 is: " + board.get_position(2, 2))
	print("Filling board and printing it")
	fill_board(board)
	board.print_board()

	board_list = board.get_row(1)
	print("Printing a row from board.")
	print(board_list)

	board_list = board.get_column(1)
	print("Printing a column from board as a list.")
	print(board_list)

	print("")

	board_list = board.get_diagonal(8, 0, 'ur', 'list')
	print("Printing a diagonal up right from board as a list")
	print(board_list)
	print("Printing a diagonal up right from board as a string")
	print(board.get_diagonal(8, 0, 'ur'))

	board_list = board.get_diagonal(0, 0, 'dr', 'list')
	print("Printing a diagonal down right from board as a list")
	print(board_list)
	print("Printing a diagonal down right from board as a string")
	print(board.get_diagonal(0, 0, 'dr'))

	board_list = board.get_diagonal(6, 6, 'ul', 'list')
	print("Printing a diagonal up left from board as a list")
	print(board_list)
	print("Printing a diagonal up left from board as a string")
	print(board.get_diagonal(6, 6, 'ul'))

	board_list = board.get_diagonal(0, 6, 'dl', 'list')
	print("Printing a diagonal down left from board as a list")
	print(board_list)
	print("Printing a diagonal down left from board as a string")
	print(board.get_diagonal(0, 6, 'dl'))




if __name__ == "__main__":
	main()
