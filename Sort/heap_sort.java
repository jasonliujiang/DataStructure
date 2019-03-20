    /*
      * 要知道什么是堆这种数据结构
      *         堆是一颗完全二叉树。分为大顶堆和小顶堆，
      *         大顶堆，每个父结点都比自己的子节点大，也就是根结点为最大
      *         小顶堆，每个父结点都比自己的子节点小，也就是根结点最小。
      * 按照大顶堆和小顶堆这种特点，将一个无序的n个记录的序列构建成大顶堆,将根节点上的数与最后一个
      * 结点n进行交换，然后在对n-1个记录进行构建大顶堆，继续把根节点与最后一个结点(n-1)互换，继续上面的操作。
      *         从小到大排序，则使用大顶堆
      *         从大到小排序，则使用小顶堆
      *     从小到大
      */
public class heap_sort{
    public void HeapSort(int[] array){
        //第一步：构建一个大顶堆
        int length = array.length;
        //遍历完全二叉树的每一个父节点
        for(int i = length/2-1;i>=0;i--){
            adjustMaxheap(array,i,length);
            //构建一个大顶堆
        }
        ////第二步：构建好了大顶堆后，将第一个数与最后一个进行互换,互换后继续调整大顶堆，
        for(int i = length-1;i>0;i--){
            wrap(array,0,i);
            adjustMaxheap(array,0, i);//从上往下，因为基本上都已经有序了，没必要在从下往上重新进行构建堆了，这就利用了前面比较的结果，减少了很多次比较。
        }
    }
    public void wrap(int[] array,int i, int j){
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
     /**
      *             构建大顶堆的操作，
      *         父节点和其左右子节点的大小比较和互换，每次将父结点的位置和数组传进来，
      *         就能构建出大顶堆了。
      * 
      * @param array    排序数组
      * @param s    当前所指父节点在数组中位置(下标)
      * @param length 数组的长度。用来判断父节点的两个子节点是否存在。
      *         父节点和左子结点的关系： 2s+1
      *         父结点和右子结点的关系： 2s+2
      */
    public void adjustMaxheap(int[] array,int s,int length){
        int child;
        int temp = array[s];
        for(int child = 2*s+1;child = <= length-1;child = child*2+1){
            if (child<length-1&&array[child]<  array[child+1]) {
                child++;
            }
            if(array[child]>temp){
                array[s] = array[child];
            }else{
                break;
            }
            array[child] = temp;
            s = child;//因为子节点的值变了，那么就不知道这个子节点在他自己的两个子节点中是否还是最大，所以需要将该子节点的数组下标给s，去重新检测一遍。只有当父节点为最大时，才会执行break退出循环。
        }
    }

    
}

