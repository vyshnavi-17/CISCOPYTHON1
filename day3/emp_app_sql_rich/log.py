import logging

# Set up logging
logging.basicConfig(
    filename='employee_app_logs.log',  # use 'filename' not 'file'
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'  # remove extra space after % and fix typo
)