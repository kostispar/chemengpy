# chemengpy
Basic concepts and computations in Chemical Engineering

<b> 1. Dimensions, units and conversions </b>
</br></br>

&nbsp;&nbsp;&nbsp;&nbsp; This chapter contains two main functionalities:<br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic SI Units</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python basic.py si <physical-quantity>` in order to see the basic SI unit as well as the symbol and its definition of any physical quantity. For example you may run `python basic.py si energy`. This will print `joule, J, kg * (m^2) * (s^(-2))` </br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic conversions</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python basic.py convert <quantity> <unit-1> <unit-2>` in order to convert the physical quantity from `unit-1` to `unit-2`. For example you may run `python basic.py convert 500 J kJ`. This will print `0.5 kJ`



<b> 2. Moles, density and concentration </b>
</br></br>
&nbsp;&nbsp;&nbsp;&nbsp; This chapter contains XXXX functionalities:<br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Atomic Weight and Atomic Number</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py atomic_weight <element>` in order to see the atomic weight of the element. For example you may run `python chemeng.py atomic_weight Ba`. This will print `137.34` </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py atomic_number <element>` in order to see the atomic number of the element. For example you may run `python chemeng.py atomic_number Cu`. This will print `16` </br>

&nbsp;&nbsp;&nbsp;&nbsp; - <b>Molecular Weight calculation</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python basic.py molecular_weight <compound>` in order to calculate the Mr of the compound. For example you may run `python basic.py molecular_weight H2O`. This will print `18`. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Do not forget to use parentheses on more complex compounds. For instance: </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `python basic.py molecular_weight Ba(OH)2`. This will print `171.34168`.

&nbsp;&nbsp;&nbsp;&nbsp; - <b>Finding mass of moles and vice versa</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  You can calculate the mass (in g) of a specific amount of moles of a compound (or element). </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Run `python basic.py moles_to_mass <compound/element> <moles>`. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  For example you may run `python basic.py moles_to_mass H2O 2`. This will print `36 g`. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Likewise, you can run `python basic.py mass_to_moles <compound/element> <mass>` for calculating the moles of a given mass of a compound. For instance, `python basic.py moles_to_mass H2O 36` will print `2 moles`.
