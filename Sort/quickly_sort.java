public calss quickly_sort{
    public int Partition(int[] array,int first,int end){
        int i = first;
        int j = end;
        while (i<j) {
            while(i<j&array[i]<array[j]){
                j--;
            }
            if (i<j) {
                int temp = array[j];
                array[j] = array[i];
                array[i] = temp;
                i++;
            }

            while(i<j&array[i]<array[j]){
                i++;
            }
            if (i<j) {
                int temp = array[j];
                array[j] = array[i];
                array[i] = temp;
                j--;
            }
            
        }
        return j;
    }
    public void quickly_sort(int[] array,int first,int end){
        if(first<end){
            int pivot = Partition(array,first,end);
            quickly_sort(array,first,pivot-1);
            quickly_sort(array,pivot+1,end);
        }
    }
}