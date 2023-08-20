# Analysing Data using SQL


#### Task 1. How many values are there in the given dataset.
<pre>
select count(*) 
From patients;
</pre>

#### Task 2. Count the number of appointments for each day in the given dataset.
<pre>
SELECT AppointmentDay, COUNT(*) AS NumAppointments
FROM patients
GROUP BY AppointmentDay
ORDER BY AppointmentDay;
</pre>

#### Task 3. Calculate the average number of appointments(Set to nearest whole number) per day in the given dataset.
<pre>
SELECT ROUND(AVG(NumAppointments)) AS AvgAppointmentsPerDay
FROM (
    SELECT AppointmentDay, COUNT(*) AS NumAppointments
    FROM patients
    GROUP BY AppointmentDay
) AS AppointmentCounts;
</pre>

#### Task 4. Find the day with the highest number of appointments in the given dataset.
<pre>
SELECT AppointmentDay, COUNT(*) AS NumAppointments
FROM patients
GROUP BY AppointmentDay
ORDER BY NumAppointments DESC
LIMIT 1;
</pre>

#### Task 5. Calculate the monthly average number of appointments in the given dataset.
<pre>
SELECT Month, ROUND(AVG(NumAppointments)) AS AvgAppointmentsPerMonth
FROM (
    SELECT DATE_FORMAT(AppointmentDay, '%Y-%m') AS Month, COUNT(*) AS NumAppointments
    FROM patients
    GROUP BY Month
) AS MonthlyAppointmentCounts
GROUP BY Month;
</pre>

#### Task 6. Find the month with the highest number of appointments in the given dataset.
<pre>
SELECT DATE_FORMAT(AppointmentDay, '%Y-%m') AS Month, COUNT(*) AS NumAppointments
FROM patients
GROUP BY Month
ORDER BY NumAppointments DESC
LIMIT 1;
</pre>

#### Task 7. Calculate the weekly average number of appointments in the given dataset.
<pre>
SELECT YEAR(AppointmentDay) AS Year, WEEK(AppointmentDay) AS Week, COUNT(*) AS Appointments_Count
FROM patients
GROUP BY Year, Week
ORDER BY Year, Week;
</pre>

#### Task 8. Find the week with the highest number of appointments in the given dataset.
<pre>
SELECT YEAR(AppointmentDay) AS Year, WEEK(AppointmentDay) AS Week, COUNT(*) AS Appointments_Count
FROM patients
GROUP BY Year, Week
ORDER BY Appointments_Count DESC
LIMIT 1;
</pre>

#### Task 9. What is the distribution of appointments based on gender in the dataset?
<pre>
SELECT Gender, COUNT(*) AS Appointments_Count
FROM patients
GROUP BY Gender;
</pre>

#### Task 10. Calculate the number of appointments per weekday in the given dataset. Order the appointment counts in descending.
<pre>
SELECT DAYNAME(AppointmentDay) AS Weekday, COUNT(*) AS Appointments_Count
FROM patients
GROUP BY Weekday;
</pre>

#### Task 11. Calculate the average time between scheduling and the appointment day in the given dataset. Set to nearest whole number
<pre>
SELECT ROUND(AVG(DATEDIFF(AppointmentDay, ScheduledDay))) AS Avg_Days_Between_Appointments
FROM patients;
</pre>

