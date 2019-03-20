public void shellSort(int[] array){
    int i,j,temp;    //i,j分别为for循环中的控制变量 temp作用是临时记录数
    int length = array.length;
    int gap = length;
    do{
        gap = gap/2;    //步长， 假设length为10，则步长为5 2 1
        for(i = gap; i<length; i++){
            if(array[i] < array[i-gap]){
                temp = array[i];
                for(j = i-gap; j>=0 && array[j]>temp; j-=gap){
                    array[j+gap] = array[j];
                }
                array[j+gap] = temp;
            }
        }
        
    }while(gap>0);
}