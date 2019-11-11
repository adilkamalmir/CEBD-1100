# Week 8 Project

Note: The following document is in reference to the wine dataset. 
        Wine dataset: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
        
Note: Full set of figures can be found at: https://github.com/adilkamalmir/python/tree/master/figures

In the following figures, the marker size denotes the amount of alcohol in the wine. 

Findings:

![Figure 1](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/ash_x_alcalinity_of_ash.png)

It can be observed that if the alcalinity of ash is below the order 1 polynomial it is very much likely the wine is from cultivar 1.

![Figure 2](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/ash_x_nonflavanoid_phenols.png)

It can be observed that if the nonfavanoid phenols are less than the order 1 polynomial it is very much likely the wine is from cultivar 1.

![Figure 3](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/ash_x_od280_od315_of_diluted_wines.png)

It can be observed that wines from cultivar 1 and 3 are differentiated based on their level of od280/od315 of diluted wines metric, i.e. if it is less than the order 1 polynomial the wine belongs to cultivar 3 and if it more than it belongs to cultivar 1.

![Figure 4](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/color_intensity_x_ash.png)

It can be observed that color intensity of wines increase from cultivar 2 to 1 to 3, in that order, for similar levels of ash.

![Figure 5](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/color_intensity_x_hue.png)

It can be observed that color intensity of wines increase from cultivar 2 to 1 to 3, in that order, for similar levels of hue.

Both of the above two observations also show that the alcohol is the highest for wines from cultivar 1.

![Figure 6](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/flavanoids_x_alcalinity_of_ash.png)

It can be observed that flavanoids increase as we move from cultivar 3 to 2 to 1, in that order. Also, the alcalinity of ash decreases for the same order as well.

![Figure 7](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/flavanoids_x_ash.png)

It can be observed that for similar levels of ash, the flavanoids increase from cultivar 3 to 2 to 1. 

![Figure 8](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/flavanoids_x_color_intensity.png)

It can be observer that when flavanoids are between 1 and 3, and alcohol levels are low, it is likely that the wine is from cultivar 2.

![Figure 9](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/flavanoids_x_hue.png)

It can be observed that the level of hue increases with flavanoids, and the level of flavanoids increases from cultivar 3 to 2 to 1. 

![Figure 10](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/flavanoids_x_magnesium.png)

It can be observed that for similar levels of ash, the flavanoids increase from cultivar 3 to 2 to 1. 

![Figure 11](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/flavanoids_x_nonflavanoid_phenols.png)

It can be observed that for similar levels of ash, the flavanoids increase from cultivar 3 to 2 to 1. 
Also the nonflavanoid phenols decrease as flavanoids increase.

![Figure 12](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/flavanoids_x_od280_od315_of_diluted_wines.png)

It can be observed the level of alcohol increases when both flavanoids and od280/od315 of diluted wines increase.

![Figure 13](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/magnesium_x_proline.png)

It can be observed if the level of proline is higher than the first order polynomial it is likely that the wine belongs to cultivar 1.

![Figure 14](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/malic_acid_x_flavanoids.png)


![Figure 15](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/nonflavanoid_phenols_x_color_intensity.png)

![Figure 16](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/nonflavanoid_phenols_x_proline.png)

![Figure 17](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/od280_od315_of_diluted_wines_x_alcalinity_of_ash.png)

![Figure 18](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/proanthocyanins_x_proline.png)

![Figure 19](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/proline_x_flavanoids.png)

![Figure 20](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/proline_x_hue.png)

![Figure 21](https://github.com/adilkamalmir/python/blob/master/figures/color_cultivars_size_alcohol/proline_x_od280_od315_of_diluted_wines.png)


Overall, wines from cultivar 1 have the highest alcohol content. 

More figures, where the marker size represents the color intensity of the wine can be found here:
https://github.com/adilkamalmir/python/tree/master/figures/color_cultivars_size_color_intensity

