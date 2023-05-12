# CO2 Matters
[![DOI](https://zenodo.org/badge/639773723.svg)](https://zenodo.org/badge/latestdoi/639773723)
[![DOI](https://test.researchdata.tuwien.ac.at/badge/DOI/10.70124/4s85p-g0w08.svg)](https://doi.org/10.70124/4s85p-g0w08)

The aim of this project is to analyse the rise of CO2-levels and global temperature anomalies and confirm/visualize 
that there is indeed a correlation between them. 
To achieve this, temperature data from GISTEMP (Global Land-Ocean Temperature Index) and GCAG 
(Global component of Climate at a Glance) is set against data from CO2 PPM (Trends in Atmospheric Carbon Dioxide) 
and processed in a python script which also plots and exports the data for further investigation.

## Input Data
- [Annual Global Temperature Time Series](https://datahub.io/core/global-temp) 
- [Trends in Atmospheric Carbon Dioxide](https://datahub.io/core/co2-ppm) 

Both the temperature anomalies and CO2 levels are time series. 
Temperature data is available from 1880 - 2016 in yearly resolution. CO2 level data is available 
from 1958-03-01 - 2018-09-01 in monthly resolution. To load and transform the data, 
a python script which utilizes pandas is being used. The main transformation is changing the resolution 
of the CO2 Levels to also be in yearly format and then trimming both series to start from 1959 so they can be 
compared against each other.

## Output Graphics
![Global Temperature Anomaly (GCAG) and CO2 Levels Over Time.png](output%2FGlobal%20Temperature%20Anomaly%20%28GCAG%29%20and%20CO2%20Levels%20Over%20Time.png)

![Global Temperature Anomaly (GISTEMP) and CO2 Levels Over Time.png](output%2FGlobal%20Temperature%20Anomaly%20%28GISTEMP%29%20and%20CO2%20Levels%20Over%20Time.png)


## Output Data

temp_anomaly_co2.csv with 4 columns:
- Year \
The year as an integer.
- Temp Anomaly GCAG \
Average global mean temperature anomalies in degrees Celsius relative to a base period. GCAG base period: 20th century average.
- Temp Anomaly GISTEMP \
Average global mean temperature anomalies in degrees Celsius relative to a base period. GISTEMP base period: 1951-1980. 
- Average CO2 \
The interpolated and seasonally corrected yearly mean CO2 mole fraction determined from daily averages. 