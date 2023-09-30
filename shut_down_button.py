import time
import asyncio
import subprocess
import RPi.GPIO as GPIO

# Specify the GPIO Pin where the shut down button is connected to
shutdown_btn = 27
# Button state monitor interval (set every 1 second to avoid intense loop)
t_interval = 1
# Counter to be considered as shutdown (set to 3 seconds)
t_shutdown = 3

# Setting the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(shutdown_btn, GPIO.IN)

# Command for shutdown
shutdown_cmd = ['sudo', 'shutdown', '-h', 'now']
# Command for reboot
reboot_cmd = ['sudo', 'shutdown', '-r', 'now']


def shutdown_reboot(action_name, command):
    # Printing the action (Shutting down... or Rebooting...) to the STDOUT
    print (f'{action_name}...')
    # Executing the shut down or reboot
    subprocess.run(command)


def main(shutdown_btn, t_interval=1, t_shutdown=3):
    
    while True:

        # Wait to avoid intense loop
        time.sleep(t_interval)

        if GPIO.input(shutdown_btn) == False:
            # Button is pressed. Initialize the time counter
            time_count = 0

            while GPIO.input(shutdown_btn) == False:
                # Start counting the press time
                time.sleep(t_interval)
                time_count += 0.5

                # Shut down if the press time is more than t_shutdown
                if time_count >= t_shutdown:
                    shutdown_reboot('Shutting Down...', shutdown_cmd)
            
            # Reboot
            shutdown_reboot('Rebooting...', reboot_cmd)
            # Break the loop anyway
            break
                     

if __name__ == '__main__':
    main(shutdown_btn=shutdown_btn, t_interval=t_interval, t_shutdown=t_shutdown)