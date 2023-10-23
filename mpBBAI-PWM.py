#/**************************************************************************************/
#/*File : mpBBAI-PWM.py                                                               */
#/*Made by: Malav Patel                                                                */
#/*Company: Teksun Microsys Pvt Ltd                                                    */
#/*Topic:                                                                              */
#/*                                                                                    */
#/*       BBAI PIN P9_14 Configure as a PWM                                            */
#/*                                                                                    */
#/*E-Mail Id: malav.patel@teksun.in                                                    */
#/**************************************************************************************/  

import os

def setup():
    with open("/sys/class/pwm/pwm-0:0/enable", "w") as pwm:
        pwm.seek(0,0);
        pwm.write("1");
    with open("/sys/class/pwm/pwm-0:0/period", "w") as period:
        period.seek(0,0);
        period.write("2500");

def pwm_duty(the_duty_multiplier):

    with open("/sys/class/pwm/pwm-0:0/duty_cycle", "w") as duty:
        duty.seek(0,0);
        duty.write(str(100*the_duty_multiplier));

setup()
count =3;
while True:

   count += 1;
   pwm_duty(count)
   if (count > 24):
       count = 3
