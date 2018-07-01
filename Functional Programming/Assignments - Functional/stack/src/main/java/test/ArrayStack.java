
package test;


public class ArrayStack<T> {
    
    private T[] data = null;
    private int top = 0;
    private int size;

    public ArrayStack(int size) {
        data = (T[]) new Object[size];
        this.size = size;
    }
    
    public void push(T element) {
      data[top] = element;
      top++;
    }
    
    public T pop(){
        if(top == 0) return null;
        top--;
        T element = data[top];
        data[top] = null;
        return element;
    }
    
    public boolean isEmpty(){
        return top == 0;
    }
    
}
