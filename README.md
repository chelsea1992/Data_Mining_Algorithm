#Object Oriented Design
========================================
<h2>RandomWalking</h2>
<p>•Implemented a graphics-based program to do a random walk, which simulates the wandering of an intoxicated person on a square street grid. The output displays the path of the drunkard as a sequence of line-segments in a frame.</p>
<p>•Tested the Drunkard class, ensure each function working well in every test cases.</p>
<img src="https://raw.githubusercontent.com/CarollChen/OOP/master/Drunkard/sreenShot.png" />
========================================
<h2>HashTable</h2>
<p>•Implemented a hash table with a client-specified hash size using dynamic array, and it uses chaining
via linked list.</p>

<p>•Realized table methods including insert, change, lookup, remove etc., and managed the complexity
by using some helper functions.</p>

<p>•Tested the Table Class in both command-based test driver and C++ version of concordance program.</p>

<p> Implemented following method fot this hashtable </p>
<p style="margin-left:100px">    1 .Table::lookup //looks up an element in hashtable return NULL when the element is not in this table</p>
<p style="margin-left:100px">    2 .Table::remove //remove a certain element in this table return true if success false is not</p>
<p style="margin-left:100px">    3 .Table::lookup //looks up an element in hashtable return NULL when the element is not in this table</p>
<p style="margin-left:100px">    4 .Table::insert //insert a certain element to this hashtable using hashCode(key) function to get the location</p>
<p style="margin-left:100px">    5 .Table::numEntries //return current entry number of this table</p>
<p style="margin-left:100px">    6 .Table::printAll  //print out the whole hashtable</p>
<p style="margin-left:100px">    7 .Table::hashStats //print out number of buckets, number of entries,number of non-empty buckets and longest chain (linkedlist to resolve hash code confliction)</p>
========================================
<h2>Maze</h2>
<p>•Created the Maze GUI as well as the movement of player with java.awt library.</p>

<p>•Used Depth-First-Search Algorithm to find the right route recursively.</p>

<p>•Displayed the final patch or return false if there is no way out.</p>

<p>•As the following image shows. We can find a way getting out of the Maze and the route is shown by a blue line
<img src="https://raw.githubusercontent.com/CarollChen/OOP/master/Maze/sreenShot.jpg" />
<p></p>
========================================
<h2>TextGen</h2>
<p>•Used a word-level Markov chain to generate random text with java tool, HashTable, using data from a text document.</p>

<p>•Designed, implemented and handled proper overrided exception classes</p>

<p>•Created debugging mode with producing some debugging outputs when it was activated.</p>
