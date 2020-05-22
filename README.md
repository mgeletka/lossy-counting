# Implementation of the lossy-counting algorithm
Implementation of the lossy counting algorithm for purposes of the Data Stream class on FCUP at University of Porto


## How to work with the implementation
The whole algorithm is implemented in the single python file lossy_counting.py. The example of use of the LossyCounting class can be seen in the demo.py file
General use of the implementation:
* create LossyCounting class with parameters: 
    * minSupport - minimal support of all items in the results
    * error - maximal error in the results
* process stream by calling LossyCounting().processNextElement(element)
* get results by calling the method LossyCounting().getFrequentItems()
 
 
 
### Included demos:
- exponential demo - with samples drawn from the exponential distribution 
- warehouse demo -  with samples from anonymized retail market basket data from an anonymous Belgian retail store
- Romeo and Juliet demo - with word frequencies from the Romeo and Juliet drama
