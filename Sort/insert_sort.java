pulic class insert_sort{
    public void insert_sort(int[] array){
        int j,temp;
        for(int i = 1;i<array.length;i++){
            if (array[i] < array[i-1]) {
                temp = array[i]
                for(j = i-1;j>=0&array[j]>temp;j--){
                    array[j+1] = array[j]
                }
                array[j] = temp
                
            }
        }
    }
}