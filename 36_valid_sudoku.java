// mine

class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        int pos; int newpos;
        int[] rows = new int[n];
        int[] cols = new int[n];
        int[] boxes = new int[n];
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                pos = board[i][j];
                if (pos == '.') {
                    continue;
                }
                if ((rows[i] & (1<<pos))>0){
                    return false;
                }
                rows[i] |=(1<<pos);
                if ((cols[j] & (1<<pos))>0){
                    return false;
                }
                cols[j] |=(1<<pos);
                newpos = ((int)(i/3))*3 + (j/3);
                if ((boxes[newpos] & (1<<pos))>0){
                    return false;
                }
                boxes[newpos] |=(1<<pos);
            }
        }
        return true;
    }
}

// https://leetcode.com/problems/valid-sudoku/discuss/1488228/JAVA-100-prime-number-hashes-no-collections-no-additional-loops

class Solution {
    
    private static final int CHAR_TO_INT_ADJUSTMENT = 49;
    
    public boolean isValidSudoku(char[][] board) {
        
        // One prime for every non empty cell value
        int[] primeNumbers = new int[] {2,3,5,7,11,13,17,19,23};
        
        // Hashes for rows/columns/boxes
        long[] rows = new long[9];
        long[] columns = new long[9];
        long[] boxes = new long[9];
        
        // Initial hash value is 29 (prime number) 
        Arrays.fill(rows, 29);
        Arrays.fill(columns, 29);
        Arrays.fill(boxes, 29);
        
        // For every cell
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                
                char cell = board[i][j];
                
                if (cell == '.') {
                    continue; // Skip empty cells
                }
                
                // Get prime for current cell value
                int prime = primeNumbers[(int)cell - CHAR_TO_INT_ADJUSTMENT];
                int boxIndex = i / 3 * 3 + j / 3;
                
                // If current row/column/box is devisable by current prime - we already multiplied this cell by current prime
                if (rows[i] % prime == 0 || columns[j] % prime == 0 || boxes[boxIndex] % prime == 0) {
                    return false;
                }
                
                // Multiply hashes by current prime 
                rows[i] *= prime;
                columns[j] *= prime;
                boxes[boxIndex] *= prime;
            }
        }
        
        return true;
    }
}
