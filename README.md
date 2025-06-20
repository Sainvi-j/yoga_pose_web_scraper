# Yoga Poses Web Scraper

This project is a web scraping script that collects yoga poses and their descriptions from [EkhartYoga](https://www.ekhartyoga.com/resources/yoga-poses) using Selenium. The scraped data is saved in a CSV file for easy access and further use.

## Features

- Uses Selenium to interact with a dynamic website
- Extracts titles and descriptions of yoga poses
- Saves the scraped data into a CSV file
- Basic error handling for missing or broken data

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Python Libraries:
  - `selenium`
  - `pandas`

## Installation

1. Install required packages:
    ```bash
    pip install selenium pandas
    ```

2. Download ChromeDriver and place it in a known directory. Update the path in the script accordingly:

   
## Usage

1. Run the script:
    ```bash
    python yoga_poses_scrappper.py
    ```

2. The output will be saved to:
    ```
    yoga_poses_with_descriptions.csv
    ```

## Output Format (CSV)

| Title                  | Description                        |
|------------------------|-------------------------------------|
| Downward Dog           | A foundational pose in yoga...      |
| Warrior I              | Strengthens legs and opens hips... |

## Notes
- Ensure your internet connection is active while running the scraper.
- If the website structure changes, the XPath selectors might need updating.

