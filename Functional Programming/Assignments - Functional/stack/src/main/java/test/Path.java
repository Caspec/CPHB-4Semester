
package test;


public interface Path<T> {
    
    T getFirst();
    Path<T> getRest();
    
}
