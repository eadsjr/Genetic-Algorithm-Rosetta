Genetic-Algorithm-Rosetta
=========================

This project will be a sample genetic algorithm implemented in several languages. Initial module currently in progress.

A sample encoding mechanism for a genetic algorithm. This simplistic encoding can be represented with four bits per codon, interpreting 0-9 as digits and 10-13 as operations. The additional possible values are ignored.

To translate this information to a value, you permissively search for a mathematical expression from left to right in the collection of codons. In the correct form, this results in either no value, a number, or a number with a series of operator / number modifications to it. Division by zero results in no value, otherwise the resulting expression can be reduced to a single numeric value.

This kind of data can be mutated at the bit level, causing random variation. Because the meaning can change dramatically due to small changes in the value, in a way that is not itself completely random, a given value can be refined against while larger changes are still possible when needed.

Method Inspiration: http://www.ai-junkie.com/ga/intro/gat3.html