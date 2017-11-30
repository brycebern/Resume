import java.util.NoSuchElementException;

/**
 * LLStack.java
 * @author Bryce Bern, Orlando Zuniga, 10-17-2017
 * This class is an implementation of a stack that uses a
 * linked list.
 */

public class LLStack<E> implements Stack<E> {
    
    //Instance Variables
    private Node<E> head;
    private int numItems;
    
    private class Node<E> {
        private E data;
        private Node<E> next;

        public Node(E item) {
            data = item;
            next = null;
        }
    }//End Node Class
    
    
    /** Constructore creates a new instance of a
    * linked list stack.
    */
    public LLStack () {
        numItems = 0; // sets the number of items to zero.
        head = null; // makes the head null.
    } 
    
    /** Returns true if the stack is empty and false otherwise
    * @return boolean true or false depending on the number of items
    * in the stack.
    */
    public boolean isEmpty () {
        if (numItems == 0) { // if the number of items is zero returns true.
            return true;
        }
        return false; // Will return false if stack is not empty.   
    }
    
    /** Returns the size of the stack
    * @return size which checks the number of items.
    */
    public int size () {
        return numItems; // returns the number of items as the size.
    }
    
    /** Adds an item to the top of the stack
    * that works with any object.
    */
    public void push (E item) {
        Node<E> pushNode = new Node(item); // creates a new node to be inserted into the stack.
        if (numItems == 0) { // when the size is zero this sets the head of the LinkedList stack.
            head = pushNode; // the head is equal to the new node.
        }
        else {
            pushNode.next = head; // the previous head is now at the next position of the node to be inserted.
            head = pushNode; // the node inserted is now the head.
            
        }
        numItems++; // increments the number of items.
    }
    
    /** Removes and returns the item on the top of the stack.
    * If the stack is empty throws a NOSuchElementException.
    * @return The top item of the stack.
    */
    public E pop() {
        if (numItems == 0) { // Throws an exception if the method is called when the stack is empty.
            throw new NoSuchElementException ();
        }
        E topItem = head.data; // stores the current head.
        head = head.next; // sets the new head as the node after the old head.
        numItems--; // decreases the number of items by one.
        return topItem; //returns the previous head which was the item at the top.
    }
    
    /** Returns the item on the top of the stack without 
    * removing it and if the stack is empty 
    * throws a NoSuchElementException.
    * @return The top item of the stack without removing it.
    */
    public E peek() {
        if (numItems == 0) { // Throws an exception if the method is called whent he stack is empty.
            throw new NoSuchElementException ();
        }
        E topItem = head.data; //sets variable as the top of the stack.
        return topItem; //returns the top of the stack.
    }
    
    /** Returns a string representation of the stack
    * showing the top and bottom of the stack with the objects
    * in the order that they are in.
    * @return String containing all elements in the LLStack.
    */
    public String toString() {
        String returnString = ""; // creates a new string to be used.
        returnString = ("top ["); 
        Node<E> tempNode = head; // tempNode store head.
        while (tempNode != null) { // loops through the linked list until empty 
            returnString = (returnString + " " + tempNode.data); // puts stack objects in order as a string.
            tempNode = tempNode.next; // moves on to the next element in the stack.
        }
        returnString = (returnString + " ] bottom" + "   " + "(stack with " + size() + " elements)");
        return returnString; // returns a string representation of all the elements.
    }
} // End LLStack Class