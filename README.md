# Electric motor temperature estimation

## In this notebook:
- **About the dataset**
    - Background
    - Inspiration
    - Dataset characteristics
    - License
- **Theory**
    - Construction of a synchronous motor
    - Parks transformation
- **Project**
    - Libraries
    - Loading data
    - Data analysis
    - Visualisation
    - Correlation heatmap
    - Molding data
    - Splitting data
    - Building the model
    - Model evaluation
    - Application of moving average
    - Saving the model
    - Conclusion

        


# About the dataset


### Background

The data set comprises several sensor data collected from a permanent magnet synchronous motor (PMSM) deployed on a test bench. The PMSM represents a german OEM's prototype model. Test bench measurements were collected by the LEA department at Paderborn University.
This data set is mildly anonymized.

The motor is excited by hand-designed driving cycles denoting a reference motor speed and a reference torque.
Currents in d/q-coordinates (columns "id" and iq") and voltages in d/q-coordinates (columns "ud" and "uq") are a result of a standard control strategy trying to follow the reference speed and torque.
Columns "motor_speed" and "torque" are the resulting quantities achieved by that strategy, derived from set currents and voltages.

Most driving cycles denote random walks in the speed-torque-plane in order to imitate real world driving cycles to a more accurate degree than constant excitations and ramp-ups and -downs would.

## Inspiration

The most interesting target features are rotor temperature ("pm"), stator temperatures ("stator_*") and torque.
Especially rotor temperature and torque are not reliably and economically measurable in a commercial vehicle.

Being able to have strong estimators for the rotor temperature helps the automotive industry to manufacture motors with less material and enables control strategies to utilize the motor to its maximum capability.
A precise torque estimate leads to more accurate and adequate control of the motor, reducing power losses and eventually heat build-up.