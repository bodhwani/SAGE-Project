# Task
For this assignment we need to find an automated way of getting the number of orbital launches in the 'Orbital launches' table in Wikipedia Orbital Launches if at least one of its payloads is reported as 'Successful', 'Operational', or 'En Route'. For each launch, listed by date, the first line is the launch vehicle and any lines below it correspond to the payloads, of which there could be more than one. Please note that there might be multiple launches on a single day with multiple payloads within a single launch (we are only interested in the number of distinct launches).

## Libraries used
- urllib
- BeautifulSoup
- pandas
- datetime

## Output
The output format is a .csv file where the first column is `date` and the second column is `value`. All dates should be formatted in the ISO 8601 format and all values should be integers. Include all dates in 2019 and fill in a 0 value for any date where there are no orbital launches.

Checkout output.csv