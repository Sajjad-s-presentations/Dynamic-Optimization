The UFLP (Uncapacitated Facility Location Problem) or Facility Coverage Problem is a problem in which a number of facilities must be placed in different locations and the cost of this placement must be minimized. In this problem, each facility can cover one or multiple customers, and each customer must be covered by one facility.

Problem formulation:
In this problem, a set   F   of facilities and a set   C   of customers are given. Additionally,   f_i    represents the installation cost of facility   i   , and    c_{ij}    represents the cost of covering customer    j    by facility    i   . The objective is to minimize the total cost of installation and coverage of facilities.

Constraints:
- Each customer must be covered by at least one facility:
- Each facility can only be installed once:

Data file:
The required data file for this code includes two matrices. The first matrix represents the installation costs of facilities, and the second matrix represents the cost of covering each customer by each facility. Additionally, the number of facilities and customers is specified in this file.

nFacilities = 3;
nCustomers = 4;

FacilityFixedCosts = [1 2 3];

CustomerCosts = [
  [1 2 3 4],
  [2 3 4 1],
  [3 4 1 2]
];


Explanation:

In this code, the variable    nFacilities     represents the number of facilities, and the variable     nCustomers     represents the number of customers. Additionally, the matrix     FacilityFixedCosts     includes the installation costs of facilities, and the matrix     CustomerCosts     includes the cost of covering each customer by each facility. Finally, the constraints of the problem are implemented using the    sum    and    forall    functions.
