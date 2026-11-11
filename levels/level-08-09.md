# Level 8 -> Level 9

**Goal**
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

**Commands Used**
*  `sort`
*  `uniq`

**Thought Process**
1. Used `sort` to arrange the lines in lexicographical order.
2. Used a pipe (`|`) to pass the sorted output to `uniq -u`.
3. Used `uniq -u` to display the line that appears only once.

**Key Concepts**

- `sort`: Sorts lines in lexicographical order.
- `uniq -u`: Displays lines that occur only once.
