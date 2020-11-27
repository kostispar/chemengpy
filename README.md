# chemengpy
Basic concepts and computations in Chemical Engineering

<b> 1. Dimensions, units and conversions </b>
</br></br>

&nbsp;&nbsp;&nbsp;&nbsp; This chapter contains two main functionalities:<br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic SI Units</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Run `python basic.py si -i <physical-quantity>` in order to see the basic SI unit as well as the symbol and its definition of any physical quantity. For example you may run `python basic.py si energy`. This will print `joule, J, kg * (m^2) * (s^(-2))` </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Run `python basic.py si --options` to see available options </br> 
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic conversions</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python basic.py convert -i <quantity> -b <unit-1> -c <unit-2>` in order to convert the physical quantity from `unit-1` to `unit-2`. For example you may run `python basic.py convert 500 J kJ`. This will print `0.5 kJ`



<b> 2. Moles, density and concentration </b>
</br></br>
&nbsp;&nbsp;&nbsp;&nbsp; This chapter contains XXXX functionalities:</br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Atomic Weight and Atomic Number</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run  `python basic.py atom_weight -i element` in order to see the atomic weight of the element. For example you may run `python basic.py atomic_weight -i O`. This will print `O has atomic weight 15.9994u and atomic number 8` </br>

&nbsp;&nbsp;&nbsp;&nbsp; - <b>Molecular Weight calculation</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python basic.py mol_weight -i <compound>` in order to calculate the Mr of the compound. For example you may run `python basic.py mol_weight -i CH2`. This will print `14.02664`. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Do not forget to use parentheses on more complex compounds. For instance: </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `python basic.py mol_weight -i Ba(OH)2`. This will print `171.34168`.

&nbsp;&nbsp;&nbsp;&nbsp; - <b>Finding mass of moles and vice versa</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  You can calculate the mass (in g) of a specific amount of moles of a compound (or element). </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Run `python basic.py mol_to_mass -i <compound> -m <moles>`. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  For example you may run `python basic.py mol_to_mass -i O2 -m 3`. This will print `95.9964`. </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Likewise, you can run `python basic.py mass_to_mol <compound/element> <mass in g>` for calculating the moles of a given mass of a compound. For instance, `python basic.py moles_to_mass -i O2 -m 3 ` will print `1.0000375014063028`.
