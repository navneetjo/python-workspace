import subprocess
import logging
import sys

# service name which we want to check is running or not
svc = str(sys.argv[1])

# basic configuration for debugging and log file
logging.basicConfig(filename='svc_log',
                    format= '%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# checking info for service
logging.info('checking if process' + svc + 'is running')

# service_is_running variable contains the information about svc
service_is_running = subprocess.call('ps', '-C', svc)

# if service is not running then restart the service
if service_is_running == 1:
    logging.warning('process ' + svc + 'is not running !')
    logging.info('attempting to restart' + svc)

    # command to restart the service
    restart_sts = subprocess.call(['sudo', '/etc/init.d/%s' % svc, "start"])

    if restart_sts == 1:
        logging.error('unable to restart %s please check the logs' % svc)
    else :
        logging.info('%s successfully restarted' % svc)
# if service is already running
else:
    logging.info('service %s is running ' % svc)
