### What

PyChemBalancer is a simple program that calculates and assigns stoichiometric coefficients to molecules taking part in a chemical reaction.

### Why

This program was developed originally in C++ as an university assignment. I wanted to rewrite it to Python as a learning experience.

### How

It takes a chemical reaction as an input (e.g. H2 + O2 -> H2O) _without_ assigned coefficients. The output is a balanced reaction (in our case 2H2 + O2 -> 2H2O).

Balancing is done using pure matrix operations. There's absolutely NO chemical knowledge required to balance any equation, even when doing this by hand!

#### Changelog