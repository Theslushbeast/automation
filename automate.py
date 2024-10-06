import multiprocessing
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure options for incognito mode and headless mode
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (necessary for some environments)
chrome_options.add_argument("--window-size=1920,1080")  # Set window size (necessary for some environments)

# Specify the path to the chromedriver
driver_path = 'C:/Users/admin/Desktop/voting automation/chromedriver.exe'

def automate_process():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Open the specific link
        driver.get('https://www.menti.com/alemag95vn33?source=qr-page&fbclid=IwZXh0bgNhZW0CMTAAAR2sQfhQs0I786BYOfKVeJjAwzvNHoAx5C4bVCh0Sd6obAtt1GtBgdKYrWk_aem_UtVYku27X4fEW1kxk4G_eQ')

        # Wait for the page to load
        time.sleep(2)  # Adjust the sleep time as necessary

        # Click on the radio button (adjust the selector as necessary)
        radio_button = driver.find_element(By.ID, '1')
        radio_button.click()

        # Submit the form using the button type
        submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

        # Wait for the form to submit and process
        time.sleep(1)  # Adjust the sleep time as necessary

        logging.info("Process completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    try:
        while True:
            # Number of processes to run concurrently
            num_processes = 100

            # Create a list to hold process objects
            processes = []

            # Start each process
            for _ in range(num_processes):
                process = multiprocessing.Process(target=automate_process)
                processes.append(process)
                process.start()

            # Wait for all processes to complete
            for process in processes:
                process.join()

            logging.info("All automation processes completed. Restarting...")

    except KeyboardInterrupt:
        logging.info("Process stopped by user")
    finally:
        logging.info("Script terminated.")
