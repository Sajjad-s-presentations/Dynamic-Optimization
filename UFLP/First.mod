/*********************************************
 * OPL 22.1.0.0 Model
 * Author: User
 * Creation Date: Oct 20, 2023 at 12:28:31 PM
 *********************************************/
int nFacilities=3;
int nCustomers=4;

float FacilityFixedCosts[1..nFacilities];
float CustomerCosts[1..nFacilities][1..nCustomers];

// Sets
range Facilities = 1..nFacilities;
range Customers = 1..nCustomers;

// Parameters
float fixedCosts[i in Facilities] = FacilityFixedCosts[i];
float variableCosts[i in Facilities][j in Customers] = CustomerCosts[i][j];

// Decision variables
dvar boolean x[Facilities];
dvar boolean y[Facilities][Customers];

// Objective
minimize
  sum(i in Facilities) fixedCosts[i] * x[i] +
  sum(i in Facilities, j in Customers) variableCosts[i][j] * y[i][j];

// Constraints
subject to {
  // Each customer must be covered by at least one facility
  forall(j in Customers)
    sum(i in Facilities) y[i][j] >= 1;

  // Each facility can only be installed once
  forall(i in Facilities)
    sum(j in Customers) y[i][j] <= x[i];
}

// Solve the problem
execute {
  cp.solve();
}