# chemengpy
Basic concepts and computations in Chemical Engineering

<b> 1. Dimensions, units and conversions </b>
</br></br>

&nbsp;&nbsp;&nbsp;&nbsp; This chapter contains two main functionalities:<br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic SI Units</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py si <physical-quantity>` in order to see the basic SI unit as well as the symbol and its definition of any physical quantity. For example you may run `python chemeng.py si energy`. This will print `joule, J, kg * (m^2) * (s^(-2))` </br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic conversions</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py convert <quantity> <unit-1> <unit-2>` in order to convert the physical quantity from `unit-1` to `unit-2`. For example you may run `python chemeng.py convert 500 J kJ`. This will print `0.5 kJ`



<b> 2. Moles, density and concentration </b>
</br></br>
&nbsp;&nbsp;&nbsp;&nbsp; This chapter contains XXXX functionalities:<br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Atomic Weight and Atomic Number</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py atomic_weight <element>` in order to see the atomic weight of the element. For example you may run `python chemeng.py atomic_weight Ba`. This will print `137.34` </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py atomic_number <element>` in order to see the atomic number of the element. For example you may run `python chemeng.py atomic_number Cu`. This will print `16` </br>

&nbsp;&nbsp;&nbsp;&nbsp; - <b>Molecular Weight calculation</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py molecular_weight <compound>` in order to calculate the Mr of the compound. For example you may run `python chemeng.py molecular_weight H2O`. This will print `18`. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Do not forget to use parentheses on more complex compounds. For instance: </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `python chemeng.py molecular_weight Ba(OH)2`. This will print `171.34168`.
