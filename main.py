import time
import random
import requests
from utils.config import load_config  # Assuming a config loader exists
from scrapers.job_scraper import scrape_jobs  # Assuming job scraper exists
from notifications.notifier import send_notifications  # Assuming notification module exists

# Customizable delay range to avoid detection and rate-limiting
REQUEST_DELAY_MIN = 1  # Minimum delay in seconds
REQUEST_DELAY_MAX = 5  # Maximum delay in seconds

def main():
    print("Starting job search automation...")

    # Load configuration
    config = load_config()
    job_sites = config.get("job_sites", [])
    search_params = config.get("search_params", {})

    # Loop through job sites
    for site in job_sites:
        try:
            print(f"Scraping jobs from {site}...")
            
            # Scrape jobs
            job_listings = scrape_jobs(site, search_params)

            # Process and notify if new jobs are found
            if job_listings:
                send_notifications(job_listings)
            
            # Introduce a random delay between requests
            delay = random.uniform(REQUEST_DELAY_MIN, REQUEST_DELAY_MAX)
            print(f"Waiting for {delay:.2f} seconds before the next request...")
            time.sleep(delay)

        except requests.exceptions.RequestException as e:
            print(f"Error while scraping {site}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    print("Job search automation completed.")

if __name__ == '__main__':
    main()
