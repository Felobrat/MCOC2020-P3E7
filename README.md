# MCOC2020-P3E7
Para poder obtener los gráficos, primer lugar se debió cambiar el código a 3D, esto añadiendo una dimension de volumen, la que se difinió como ce, ya que "c" estaba ocupada por
uno de los parámetros. Luego, se definieron subdivisiones del espacio que se necesita en z, la cual se denominó Nz, de tal manera que el diferencial en z dz= c/Nz y este sea igual
al diferencial en dx y dy, quedando dx=dy=dz.
Luego, se agregó una dimension al arreglo u_k, añadiendo Nz+1. Luego se añadieron dos condiciones de borde que representan las caras frontal y trasera y se modificarion las
anteriores agregandoles la tercera dimension.Para el loop en el espacion se agrego un tercer "for" que recorre la tercera dimensión y se añadieron dos terminos al laplaciano,
ademas de agregar la tercera dimensión a los terminos exstentes. A la variable u_kml que se modifica en cada ciclo para formar el "Fordwar Euler" se le añade la función que
representa el calor de hidratacion (q(t)).
Finalmente, se identifican los sensores para graficar los cambios de temperatura que fueron registrados.

el codigo entregado, permite crear las figuras, las que luego se deben ensamblar con el codigo gif.py. con eso entrega los resultados pedidos.
