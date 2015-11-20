## pyhistuples

This is pyhistuples, a set of python modules containing easy-to-use,
pure-python classes representing histograms and NTuples.
NTuples are a data structure well known in high-energy physics,
where this project had its origins. It has been released within the DaVinci
software project of the LHCb experiment at CERN. As far as I know,
it hasn't been extensively used.
See release.notes for more information.

The rationale here has been to provide intuitive and extensible classes for simple
data processing and manipulation. Performance has not been a consideration so far,
but it is on the to-do list. There is a simple persistency mechanism using python pickle.
Among things to inversigate is the use of the shelve module for ntuples that are
too large to keep in memory.

### License:

Lesser GPL, see COPYING and COPYING.LESSER.

### Dependencies: 

* `nose` for all unit tests.
* `matplotlib` for histogram plotting.

### Installation:

This assumes `matplotlib` has already been installed into the system. 

Clone repoo and pip install from source:

```shell
git clone https://github.com/juanchopanza/pyhistuples.git
pip install pyhistuples 
```

Pip install from repo

```shell
pip install git+https://github.com/juanchopanza/pyhistuples.git
```

### Status:

* Completely experimental.

### Examples:

* The unit tests give a good indication of how to use the different components.
Documentation will follow some time in the future.

---
Juan Palacios 14/05/2011
