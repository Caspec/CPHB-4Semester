
package test;


public class ArrayStack2<T> implements Stack<T> {

    private T[] elements;
    private int top = 0;
    
    public ArrayStack2(int maxSize) {
        elements =  (T[]) new Object[maxSize];
    }
    
    @Override
    public void push(T element) {
        elements[top++] = element;
    }

    @Override
    public T pop() {
        return elements[--top];
    }

    @Override
    public boolean isEmpty() {
        return top == 0;
    }
    
}
