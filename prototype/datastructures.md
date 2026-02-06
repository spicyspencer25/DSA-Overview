KEY CONCEPTS:
    Abstract Data Types
        ADTs are conceptual descriptions/blueprints that outline the functionality of
        operations that process information. It's an interface that is meant to be expanded upon to
        different implementations that can effectively carry their behavior.

        Maps - operates via key value pairs that allow for very fast access
               to insert, delete, or edit. each key is unique, but values can be duplicated
        Sets - operates via a collection of unique elements that does not allow
               duplicates. it interacts well with itself, and there's many
               functions such as checking the intersection between two sets
               that allow for very easy/convenient analysis/comparisons
        Lists - operates via a collection of elements that allows duplicates. it's
                extremely versatile and very useful for ordering data or frequently
                accessing data
        Queues - operates via a collection of elements sorted by the order they were
                 added to the list. The first elements in a queue are the first to be
                 interacted with (FIFO, First In First Out)
        Stacks - operates via a collection of elements sorted by the order they were
                 added to the list. The last elements in a stack are the first to be
                 interacted with (LIFO, Last In First Out)

    Abstract Data Structures
        Abstract Data Structures are general frameworks that encapsulate an item's ability to
        process information. They utilize underlying data types by implementing their functionality
        to formats with specific rules for organization, enabling proper implementation of ADTs.


        Arrays - Organizes itself through indexes, with each index referencing a place
                 that holds some type of data. Elements are stored sequentially/contiguously and size is fixed.
        Linked Lists - Organizes itself through nodes referencing data and pointers to
                       other nodes that links them. Memory is dynamic that allows for fast insertion/deletion.

        Trees - Organizes itself hierarchically with nodes that have parent-child relationships
                with other nodes. Very useful for storing and searching sorted data efficiently.

        Hash Tables - Organizes itself using hash functions to access elements it contains. It's
                      very quick in accessing data. Very dynamic functionality.

    Time Complexity/Runtime
        Within the many different implementations of Data Structures, there's a lot of variation,
        even between different implementations of the same abstract data structure or different structures that
        share the same underlying data type, in time. Different structures are more suited to different problems,
        and a large part of this course was remaining mindful of what structures to use in certain situations
        for max optimization. We used different types of analysis to determine how fast certain
        structures or pieces of code executed in terms on n. iteration through different
        structures varies greatly, with some structures requiring extra code to iterate through it.

        There's no end all be all structure thats the best, and there was testing in this class to
        find out how fast certain structures were in differentiation situations. There were different
        types of analysis, such as amortized analysis, worst-case analysis, and instruction counting
        to get O(n) notation that were all measures of speed. There's many factors affecting speed, and
        different operations cost different amounts of time.

    Ex of Implementations:
        ArrayList
        ArrayStack or Queues
        Singly Linked Lists
        Doubly Linked Lists
        Circularly Linked Lists
        Binary Trees
        Binary Search Trees
        AVL Trees
        TreeSets
        HashMaps
        HashSets