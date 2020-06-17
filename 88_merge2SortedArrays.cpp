#fastest 1 ms
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int r1 = nums1.size()-1, l1 = m-1, r2 = n-1;
        while (r2>=0 && r1>=0) {
            if (l1 < 0) {
                while (r2 >=0) {
                    nums1[r2] = nums2[r2];
                    r2--;
                }
                return;                
            }
            
            if (nums2[r2] > nums1[l1]) {
                nums1[r1] = nums2[r2];
                r1--;
                r2--;
            } else {
                nums1[r1] = nums1[l1];
                r1--;
                l1--;
            }
        }
        return;
    }
};

#4 ms gap method

class Solution {
public:
    inline int nextgap(int gap){
    if(gap<=1) return 0;
    return (gap/2) + (gap%2);
}
   void merge(vector<int>& A, int n, vector<int>& B, int m) {
       
   int gap = n+m;
   gap = nextgap(gap);
   for(int g=gap;g>0;g=nextgap(g)){
       
       int i,j;
       for(i=0;i+g<n;i++){
           if(A[i]>A[i+g]) swap(A[i],A[i+g]);
       }
       for(j=g-n>0?g-n:0;i<n && j<m;i++,j++){
           if(A[i]>B[j]) swap(A[i],B[j]);
       }
       
       if(j<m){
           for(j=0;j+g<m;j++){
               if(B[j]>B[j+g]) swap(B[j],B[j+g]);
           }
       }
   }
   for(int i=n,j=0;i<m+n && j<m;i++,j++) A[i] = B[j];
}
};
