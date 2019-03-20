public class Buble_sort{
    public void buble_sort(int[] array){
        int i = array.length-1
        while (i>=1) {
            for(int j = 0;j<i;j++){
                if(array[j]>array[j+1]){
                    int temp = array[j+1];
                    array[j+1] = array[i];
                    array[i] = temp;
                }
            }
            i--;
            
        }
    }
}