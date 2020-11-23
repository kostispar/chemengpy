# chemengpy
Basic concepts and computations in Chemical Engineering

<b> 1. Dimensions, units and conversions </b>
</br></br>

&nbsp;&nbsp;&nbsp;&nbsp; This chapter contains two main functionalities:<br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic SI Units</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py si <physical-quantity>` in order to see the basic SI unit as well as the symbol and its definition of any physical quantity. For example you may run `python chemeng.py si energy`. This will print `joule, J, kg * (m^2) * (s^(-2))` </br>
&nbsp;&nbsp;&nbsp;&nbsp; - <b>Basic conversions</b> </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Run `python chemeng.py convert <quantity> <unit-1> <unit-2>` in order to convert the physical quantity from `unit-1` to `unit-2`. For example you may run `python chemeng.py convert 500 J kJ`. This will print `0.5 kJ`
