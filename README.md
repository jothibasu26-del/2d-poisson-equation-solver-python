# 2D Poisson Equation Solver with Spatially Varying Source | Python

## Overview

A numerical solution of the two-dimensional Poisson equation with a spatially
varying source term using the Finite Volume Method (FVM) on a structured grid.

The resulting algebraic system is solved iteratively using the Successive
Over-Relaxation (SOR) method. The numerical solution is compared with the
analytical solution to verify the numerical implementation.

## Problem Definition

The governing Poisson equation is

```math
\nabla^2 T = 32\left[x(x-1)+y(y-1)\right]
```

or

```math
\frac{\partial^2 T}{\partial x^2}
+
\frac{\partial^2 T}{\partial y^2}
=
32\left[x(x-1)+y(y-1)\right]
```

The equation is solved over a two-dimensional structured domain with
prescribed zero-value boundary conditions.

## Numerical Method

The governing equation is integrated over individual control volumes using
the Finite Volume Method.

The diffusion fluxes across the control-volume faces are evaluated and the
resulting discretized equation is written in the form

```math
a_P T_P =
a_E T_E +
a_W T_W +
a_N T_N +
a_S T_S +
b
```

For the structured uniform grid used in this project, the discretization
involves the four neighboring control volumes.

The resulting algebraic equations are solved iteratively using the
Successive Over-Relaxation (SOR) method.

The SOR update is expressed as

```math
T_P^{new}
=
(1-\omega)T_P^{old}
+
\omega T_P^{*}
```

where $\omega$ is the relaxation factor.

The relaxation factor used in the computation is

```math
\omega = 1.95
```

The iterative solution is considered converged when the maximum change in
the solution between successive iterations falls below

```math
10^{-3}
```

## Computational Details

| Parameter | Value |
|---|---:|
| Grid | 39 × 39 |
| Grid spacing | $\Delta x = 1/(39+1)$ |
| Numerical method | Finite Volume Method |
| Grid type | Structured |
| Iterative solver | SOR |
| Relaxation factor | 1.95 |
| Convergence criterion | $10^{-3}$ |
| Boundary conditions | $T = 0$ |

## Analytical Solution

An analytical solution is used as a reference for verification of the
numerical solution.

For the prescribed source term and boundary conditions, the analytical
solution is

```math
T(x,y) = 16x(x-1)y(y-1)
```

The analytical solution satisfies the governing Poisson equation and the
prescribed zero-value boundary conditions.

It is evaluated over the computational domain and compared with the
numerical FVM solution.

## Solution Procedure

The numerical solution procedure consists of:

1. Defining the structured computational grid.
2. Evaluating the spatially varying source term.
3. Formulating the control-volume balance for each cell.
4. Calculating the neighboring-cell contributions.
5. Applying the SOR iterative scheme.
6. Monitoring the maximum change in the solution.
7. Continuing the iteration until the specified convergence criterion is
   satisfied.
8. Exporting the converged numerical solution for post-processing.

The numerical solver is implemented in Python.

MATLAB was used for post-processing and visualization of the analytical and
numerical solutions.

## Results

### Analytical Solution

The analytical solution obtained from the prescribed mathematical expression.

![Analytical Solution](analytical%20solution.png)

### Numerical Solution

The numerical solution obtained using the Python-based Finite Volume Method
and SOR solver.

![Numerical Solution](numerical%20solution.png)

### Temperature Distribution at y = 0.5

Comparison of the analytical and numerical solutions along the line
$y=0.5$.

![Temperature at y = 0.5](T%20vs%20y%3D0.5.png)

### Temperature Distribution at x = 0.5

Comparison of the analytical and numerical solutions along the line
$x=0.5$.

![Temperature at x = 0.5](Tvs%20x%3D0.5.png)

## Verification

The numerical FVM solution is compared with the analytical solution at
selected locations within the computational domain.

The agreement between the analytical and numerical solutions demonstrates
that the finite-volume discretization and SOR iterative solution correctly
reproduce the prescribed Poisson equation.

## Skills Demonstrated

- Finite Volume Method (FVM)
- Numerical methods for partial differential equations
- Poisson equation
- Control-volume discretization
- Structured-grid methods
- Successive Over-Relaxation (SOR)
- Iterative convergence analysis
- Numerical solution verification
- Python programming
- MATLAB post-processing and visualization

## Software

- Python
- MATLAB
