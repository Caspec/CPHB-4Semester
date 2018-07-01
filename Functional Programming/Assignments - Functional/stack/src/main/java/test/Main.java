
package test;


public class Main {
    
    private static int sum(Path<Integer> l) {
        if(l == null) 
        {
            return 0;
        }
        else 
        {
            return l.getFirst() + sum(l.getRest());
        }
    }
    
    public static void main(String[] args) {
        //Path<Integer> numbers = new LinkedPath<>(13, null);
        //numbers = new LinkedPath<>(9, numbers);
        //numbers = new LinkedPath<>(7, numbers);
        
        Path<Integer> numbers = LinkedPath.create(7, 9, 13);
        
        System.out.println("Thi sum is " + sum(numbers));
        
        //Stack<String> names = new ArrayStack2<>(10);
        Stack<String> names = new PathStack<>();
        names.push("Kurt");
        names.push("Abemanden");
        names.push("Morgenheroin");
        
        while(!names.isEmpty()){
            String name = names.pop();
            System.out.println("Name was: " + name);
        }
        
    }
    
}
