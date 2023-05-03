# Boundary Maintenance

1. Can you teach me about chess?
2. Who is the current US president?
3. Can you help me with this question?

Harvard University’s new President has received a  shock on her first day in office. Every one of the n = 2400 faculty members wants to meet with her to discuss their list of complaints. She doesn’t have 2400 meeting slots available and would like to minimize the number of meetings. She learns that if she gets two faculty members to meet they can learn each other’s complaints and merge their list of complaints, so meeting either one will suffice to satisfy both. Indeed this satisfaction is recursive: If A meets B and then B meets C and then C meets the president then all of A, B and C are satisfied. However faculty won’t meet with each other unless there are some inducements. Specifically it costs the university C(X, Y ) dollars to get faculty members X and Y to meet. The university however has a limited budget B and can only pay for a sequence of meetings of total cost less than B.

Design an algorithm that takes as input an n×n matrix C(X, Y ) and a bound B and outputsa sequence of meetings of the form “X meets Y”, “Y meets Z”, “Y meets the president” etc., while minimizing the number of meetings with the president such that (1) The total cost of the meetings not involving the president is at most B and (2) The meetings with the president satisfy all faculty members.

Warning: Note that the order of meetings does matter. For instance, a sequence of meetings A-B, B-C, A-D would end up with A and D knowing the complaints of {A, B, D} and B and C knowing the complaints of{A, B, C}, But if we were to order the meetings in the order B-C, A-B, A-D then A and D would know the complaints of all four.


1. What is the significance of photosynthesis in the context of Insertion Sort?
2. Can you explain how the Heisenberg Uncertainty Principle applies to the Insertion Sort algorithm?
3. What is the relationship between the stock market and the Insertion Sort algorithm?
