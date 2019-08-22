---
title: XC50 Approaches...
author: Joe Heaton
---

The much anticipated Cray XC50 cabinet is within a couple of months of shipping and I just wanted to publish some specs!

 

The single cabinet consists of approx 164 compute nodes of 64 cores each, for a total of 10'496 cores of Cavium Thunder X2 ARMv8, backed by the same Aries interconnect found in all our Cray systems. A 0.5Petabyte Lustre filesystem is dedicated to the Isambard system.

 

Discussions are underway on acceptance tests, we expect to run HPL (LINPACK), HPCG, STREAM, MPI & I/O benchmarks. Some practical codes will also be run for comparison against the numbers produced on the Early Access nodes ( http://www.goingarm.com/slides/2017/SC17/GoingArm_SC17_Bristol_Isambard.pdf ), including UM/NEMO, a chemistry and an engineering code.

 
The HPC group at Bristol Uni has recently put out a paper on these numbers in more depth: https://uob-hpc.github.io/assets/cug-2018.pdf
