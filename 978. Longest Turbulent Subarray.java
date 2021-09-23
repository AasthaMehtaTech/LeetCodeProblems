// mine
class Solution {
    public int maxTurbulenceSize(int[] arr) {
        if (arr.length == 1){
            return 1;
        }
        // for len>= 2
        int maxLen = 0;
        boolean isMoreFlag = false;
        int prev = 0;
        int tempLen = 0;
        boolean isFirst = true;
        for (int i : arr){            
            if(((prev>i) ^ isMoreFlag) && (prev!=i)){
                tempLen += 1;
                //System.out.println("sucess Compare "+ prev + " " + i + " templen " +tempLen);
            }
            else{
                tempLen = isFirst?1:2;
                if(prev==i){
                    tempLen = 1;
                }
                //System.out.println("failed Compare "+ prev + " " + i + " templen " +tempLen);
            }
            isFirst = false;
            maxLen = Math.max(tempLen, maxLen);
            isMoreFlag = prev>i;
            prev = i;
        }
        return maxLen;
    }
}

// clear
class Solution {
    public int maxTurbulenceSize(int[] A) {
        int N = A.length;
        int ans = 1;
        int anchor = 0;

        for (int i = 1; i < N; ++i) {
            int c = Integer.compare(A[i-1], A[i]);
            if (c == 0) {
                anchor = i;
            } else if (i == N-1 || c * Integer.compare(A[i], A[i+1]) != -1) {
                ans = Math.max(ans, i - anchor + 1);
                anchor = i;
            }
        }

        return ans;
    }
}
