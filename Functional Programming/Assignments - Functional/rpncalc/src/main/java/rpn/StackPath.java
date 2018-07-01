
package rpn;


public class StackPath {
    
    private NumberPath<Integer> data = null;
    private int counter = 0;

    public void push(Integer Element) {
        data = new NumberPath<Integer>(Element, data);
        counter++;
    }

    public Integer pop() {
        if (data == null) {
            return 0;
        }
        Integer returnValue = data.getFirst();
        data = (NumberPath<Integer>) data.getRest();
        counter--;
        return returnValue;
    }
    
    public Integer[] peekAll(){
        Integer[] list = new Integer[counter];        
        if(data==null){
            return null;
        } else {
            return data.peekAll(list, 0);
        }
    }
    
}
