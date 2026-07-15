class Solution {
    public int[] productExceptSelf(int[] nums) {
        int z_index=-1,zeros =0,t_prod=1;
        for(int i=0; i<nums.length; i++){
            if( nums[i] != 0) t_prod*=nums[i];
            else {z_index=i;zeros++;}
        }
        System.out.println(t_prod+" , "+zeros+" , "+z_index);
        if ( zeros == 0 ){
            for(int i=0; i<nums.length; i++) nums[i] = t_prod/nums[i]; 
        }else if ( zeros == 1){
            nums = new int[nums.length];
            nums[z_index] = t_prod;
        }else{
            nums = new int[nums.length];
        }
        return nums;
    }
}