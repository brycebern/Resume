import java.util.NoSuchElementException;

/**
 * ArrayQueue.java
 * @author Bryce Bern, Orlando Zuniga, 10-17-2017
 * This class is an implementation of a Queue using a circular Array.
 */

public class ArrayQueue<E> implements Queue<E> {

	private E[] dataArray;
	private int front;  // index of first item to remove
	private int rear;   // index of next available position
	private int numElements; // for convenience
    private int capacity; // current capacity of array
    
    private static final int DEFAULT_CAPACITY = 1000;

    /**
     * Creates an empty ArrayQueue.
     */
	public ArrayQueue() {
        dataArray = (E[]) new Object[DEFAULT_CAPACITY];
        front = 0;
        rear = 0;
        numElements = 0;
        capacity = DEFAULT_CAPACITY;
	}
	
	/** Returns true if the queue is empty and false otherwise
    * @return boolean true or false depending on the number of items
    * in the stack.
    */
    public boolean isEmpty() {
        if (numElements == 0) {
            return true; // returns true if number of elements is zero.
        }
        return false;
    }
    
    /** Private method that doubles the size of the udnerlying array.
    * This method is only called in the enqueue method.
    */
    private void resizeArray() {
        E[] tempArray = (E[]) new Object[capacity * 2]; // creates a temporary array with double the capacity.
        int j = front; // saves the current position of the front.
        for (int i = 0; i < numElements; i++) { // loops through dataArray and sets objects into the new array starting at the front.
            tempArray[i] = dataArray[j];
            j = (j+1) % capacity; // changes the position of the front.
        }
        front = 0; // front of new array at 0.
        rear = numElements; // rear is at the next available position.
        capacity = capacity * 2; // doubles the capacity.
        dataArray = tempArray; // sets the temporary array as dataArray.
    }
    
    /** Returns the size of the array.
    * @return size of the array with number of elements.
    */
    public int size() {
        return numElements;
    }
    
    /** Adds item to the rear of the Queue
    * and works with any type E.
    */
    public void enqueue(E item) {
        if (numElements == capacity){ // Doubles array when number of elements equals the capacity.
            resizeArray();
        }
        dataArray[rear] = item; // inserts at at rear.
        rear = (rear + 1) % capacity; // changes the rear position.
        numElements++; // increments number of elements by one.
    }
    
    /** Removes and returns the item at the front of the Queue
    * and throws an exception if empty.
    * @return The item at front of queue and removes it.
    */
    public E dequeue() {
        if (isEmpty()) { //throws an exception if the queue is empty.
            throw new NoSuchElementException();
        }
        E returnItem = dataArray[front]; //stores the item at the front of the queue.
        numElements--; // decreases the number of elements by one.
        front = (front + 1) % capacity; // changes the position of the front.
        return returnItem; // returns the top of the queue.
    } 
    
    /** Returns the item at the front of the Queue
    * without removing it and throws an exception if empty.
    * @return The item at front of queue without removal.
    */
    public E peek() {
        if (isEmpty()) { // throws an exception if queue is empty.
            throw new NoSuchElementException();
        }
        E returnItem = dataArray[front]; 
        return returnItem; // returns the item at the front of the queue
    }
    
    /** Returns a string representation of the queue 
    * and shows the current position of the front and rear.
    * @return A string containing all elements in the queue.
    */
    public String toString() {
        String returnString = ("front: " + front + " rear: " + rear + "\nfront [ ");
        int j = front; // stores the position of the front of the queue.
        for (int i = 0; i < numElements; i++) { // loops through adding elements of the queue to the string.
            returnString = (returnString + dataArray[j] + " ");
            j = (j+1) % capacity; // changes the front.
        }
        returnString = returnString + "] rear";
        return returnString; // returns the string with all elements of the queue.
    }
} // End ArrayQueue class
