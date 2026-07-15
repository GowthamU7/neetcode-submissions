class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i=0,sum=0,j=numbers.length-1;
        int res[] = new int[2];
        while(i<j){
            sum = numbers[i]+numbers[j];
            if(sum == target){ res[0]=i+1;res[1]=j+1;return res;}
            else if(sum < target) i++;
            else j--;
        }
        return res;
    }
}