import time
import os
import subprocess

def shutdown():
    # Shutdown routine
    os.system('sudo shutdown -h now')
    subprocess.run(['sudo', 'shutdown', '-h', 'now'])

def main():
    try:
        # The main program can be written here
        print ('sleeping...')
        time.sleep(3)
        raise Exception ('shutting down')

    except:
        print ('Exception. Shutting down')
        shutdown()


if __name__ == '__main__':
    main()