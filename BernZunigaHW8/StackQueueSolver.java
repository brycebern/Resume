/**
 * StackQueueSolver.java
 * @author Bryce Bern, Orlando Zuniga, 10-17-2017
 * This class implements 3 methods that use our stack
 * and queue implementations.
 * The 3 methods are reverstack(), testReverseStack(), 
 * and lastCustomer().
 */

public class StackQueueSolver {
    
    /**
    * Returns a new Stack that contains the items
    * in a reverse order.
    * @return The stack reversed.
    */
    public static Stack reverseStack(Stack s) {
        Stack tempStack = new LLStack(); // Creates a new stack to store the reversed items.
        if (s.isEmpty()) { // returns the Stack if it is empty
            return s;
        }
        while (!s.isEmpty()) { // loops through the original stack and inserts each element into the new stack.
            tempStack.push(s.pop());
        }
        return tempStack; // returns the new reverse stack.   
    }
    
    /**
    * This method creates a stack containing the numbers
    * 1,2, ..., m with m on top and prints the contents
    * of that stack.
    * uses reverseStack method to reverse the intgers 
    * and prints out that stack
    */
    public static void testReverseStack(int m) {
        Stack stack = new LLStack(); // Creates a new stack using LLStack implementation.
        for (int i = 1; i <= m; i++) { // loops through up till the integer specified and pushed the integers into the stack.
            stack.push(i);
        }
        System.out.println("Normal Stack: " + stack); // prints out the stack starting from 1,..., m.
        System.out.println("Reversed Stack: " + reverseStack(stack)); // prints out the stack in the reverse order from m,..., 1.
    }
    
    /** This method creates a queue with m students in line. 
    * The person at the front of the line is then told to go 
    * to the back of the line doing this n times
    * the person at the front then gets their food.
    * process repeats until the line is empty and returns the lastCustomer.
    * @return lastCustomer in line as an integer.
    */
    public static int lastCustomer(int m, int n) {
        Queue <Integer> queue = new ArrayQueue<Integer>(); // Creates a new integer queue using ArrayQueue implementation.
        int lastCustomer = 0; // creates a lastCustomer with a value of zero to be changed later.
        for (int i = 1; i <= m; i++){ // loops through and adds integers to teh queue with m at the rear of the queue.
            queue.enqueue(i);
        }
        while (queue.size() != 0) { // loops through until the line is empty
            if (queue.size() == 1) { // if statement checks for when the queue is at size one to get the last customer.
                lastCustomer = queue.peek();
            }
            for (int i = 0; i < n; i++) { // loops through and dequeues n number of times placing dequeued item at end.
                queue.enqueue(queue.dequeue());
            }
            queue.dequeue(); // dequeues after n amount of times.
        }
        return (lastCustomer); // returns the lastCustomer.
    } 
} // END StackQueueSolver class