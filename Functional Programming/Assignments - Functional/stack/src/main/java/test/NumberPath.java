
package test;



public class NumberPath<T> implements Path<Long>  {

    private T first;
    private NumberPath<T> rest = null;
    
    public NumberPath(Long first, NumberPath rest){
        this.first = (T) first;
        this.rest = rest;
    }

    @Override
    public Long getFirst() {
        return (Long) first;
    }

    @Override
    public Path<Long> getRest() {
        return rest;
    }
    
    @Override
    public String toString(){
        if(rest==null){
            return first+"";
        }
        String s = first+rest.toString();
        return s;
    }
    
 


    
}
