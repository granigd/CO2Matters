# CO2 Matters

The aim of this project is to analyse the rise of CO2-levels and global temperature anomalies and confirm/visualize 
that there is indeed a correlation between them. 
To achieve this, temperature data from GISTEMP (Global Land-Ocean Temperature Index) and GCAG 
(Global component of Climate at a Glance) is set against data from CO2 PPM (Trends in Atmospheric Carbon Dioxide) 
and processed in a python script which also plots and exports the data for further investigation.

## Input Data




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