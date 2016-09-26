
import java.util.Set;

class SudokuSolver {

	static main(args) {
		new SudokuSolver().doWork()
	}
	
	def doWork() {
		def result
		def easy = new Sudoku()
		easy.cell = 
			[[5,8,0,2,7,0,0,3,4],
			 [0,0,2,5,9,0,6,0,0],
			 [0,0,0,0,0,8,0,0,0],
			 [0,0,5,0,0,0,0,1,9],
			 [1,4,0,0,0,0,0,7,6],
			 [8,9,0,0,0,0,5,0,0],
			 [0,0,0,4,0,0,0,0,0],
			 [0,0,4,0,3,7,1,0,0],
			 [3,6,0,0,1,9,0,5,2]]
		easy.show()

		result = easy.solve()

		result.show()

		def hard = new Sudoku()
		hard.cell =
			[[0,0,1,9,0,7,5,0,0],
			 [0,6,0,1,0,8,0,4,0],
			 [8,0,0,0,4,0,0,0,7],
			 [5,8,0,0,0,0,0,1,4],
			 [0,0,3,0,0,0,7,0,0],
			 [4,9,0,0,0,0,0,8,3],
			 [9,0,0,0,7,0,0,0,6],
			 [0,7,0,6,0,3,0,9,0],
			 [0,0,4,2,0,9,8,0,0]]
		hard.show()
		result = hard.solve()
		result.show()
	}
}

class CellData {
	int row
	int col
	
	CellData(int row, int col) {
		this.row = row
		this.col = col
	}
}

class Sudoku {	
	int[][] cell = new int [9][9]
	
	void setCell(CellData cd, int value) {
		cell[cd.row][cd.col] = value
	}
		
	Set getOptionsFor(CellData c) {
		Set options = [1,2,3,4,5,6,7,8,9]
		(0..8).each() { i -> options.remove(cell[c.row][i]) }
		(0..8).each() { i -> options.remove(cell[i][c.col]) }
		int blockRowOffset = (c.row.intdiv(3)) * 3
		int blockColOffset = (c.col.intdiv(3)) * 3
		(0..2).each() { int bRow ->
			(0..2).each() { int bCol ->
				options.remove(cell[blockRowOffset + bRow][blockColOffset + bCol])
			}
		}
		return options
	}

	boolean hasEmptyCell() {
		return getFirstEmpty() != null
	}
	
	CellData getFirstEmpty() {
		for(int row = 0; row <= 8; row++ ) {
			for (int col = 0; col <=8; col++) {
				if (cell[row][col] == 0) {
					return new CellData(row, col)
				}
			}
		}
		return null
	}

	Sudoku solve() {
		CellData firstEmpty = getFirstEmpty()
		Set options = getOptionsFor(firstEmpty)
		if (options.size() == 0) {
			return null // empty cell(s), but no possible solution anymore.
		} else {
			for (int optionIndex = 0; optionIndex < options.size(); optionIndex++) {
				int option = options[optionIndex]
				Sudoku nextTry = clone()
				nextTry.setCell(firstEmpty, option)
				if (nextTry.hasEmptyCell()) {
					Sudoku solution = nextTry.solve()
					if (solution != null) {
						return solution // found one!
					}
				} else return nextTry // filled the last cell, this is a solution.
			}
		}
	}
			
	def show() {
		println "    0 1 2  3 4 5  6 7 8\n"
		(0..8).each() { int row ->
			print "$row  "
			(0..8).each() {int col ->
				def c = cell[row][col]				
				def val = ". "
				if(c != 0) {
					val = "${cell[row][col]} "
				}
				if (col % 3 == 0) { print " " }
				print val
			}
			println ""
			if ((row + 1) % 3 == 0) { println "" }
		 }
	}
	
	def clone() {
		def theClone = new Sudoku()
		(0..8).each() { int row ->
			(0..8).each() {int col ->
				theClone.cell[row][col] = cell[row][col]
			}
		 }
		theClone
	}
}