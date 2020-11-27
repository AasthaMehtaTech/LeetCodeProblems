# mine

class Solution {
    public boolean isMonotonic(int[] A) {
        int len = A.length;
        if (len == 1) return true;
        int i = 0;
        int j = 1;
        
        while(j<len-1 && A[i]==A[j]){
            i++;
            j++;
        }
        if (A[i]<A[j]){
            while(i<len && j<len){
                if (A[i] > A[j]) return false;
                i++;
                j++;                
            }            
        }
        else{
            while(i<len && j<len){
                if (A[i] < A[j]) return false;
                i++;
                j++;                
            }
        }
        return true;        
    }
}


# dimaag- check with last element instead of while loop in my soln

class Solution {
    public boolean isMonotonic(int[] A) {
        
        int len = A.length;
        if (A[0] >= A[len-1]) {
            for (int i=1; i< len; i++){
                if (A[i-1] >= A[i]) {
                    continue;
                }
                else 
                    return false;
            }
            return true;
        }
        else{
            for (int i= len-1; i> 0; i--){
                if (A[i-1] <= A[i]) {
                    continue;
                }
                else 
                    return false;
            }
            return true;
        }
    }
}

/*
 Check the first and last elements of the array. 
 have if condition and based on that have for loops starting from front (1st index) or the last element of the array.
 Compare A[i-1] and A[i] for both cases and return true or false appropriately.
*/


# bit manip
class Solution {
    public boolean isMonotonic(int[] A) {
        boolean increase = false;
        boolean decrease = false;
        for(int i = 1; i < A.length; i++) {
            if(A[i] > A[i-1])
                increase = true;
            else if(A[i] < A[i-1])
                decrease = true;
        }
        
        return !(increase && decrease);
    }
}

# different

class Solution {
    public boolean isMonotonic(int[] A) {
        return isIncreasing(A) || isDecreasing(A);
    }
    
    private boolean isIncreasing(int[] A) {
        return is(A, (a, b) -> a <= b);
    }
    
    private boolean isDecreasing(int[] A) {
        return is(A, (a, b) -> a >= b);
    }
    
    private boolean is(int[] A, BiPredicate<Integer, Integer> pred) {
        for (int i = 1; i < A.length; i++) {
            if (!pred.test(A[i-1], A[i]))
                return false;
        }
        return true;
    }
}
