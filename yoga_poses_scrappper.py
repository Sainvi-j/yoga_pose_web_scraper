from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Set up the WebDriver
service = Service('D:/scrapping/chromedriver.exe')  # Update with the correct path to ChromeDriver
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    url = "https://www.ekhartyoga.com/resources/yoga-poses"
    driver.get(url)
    time.sleep(10)  # Allow the page to load

    # Locate all individual yoga pose cards
    cards_xpath = '//*[@id="contentPagelayout"]/div[4]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/a'
    card_elements = driver.find_elements(By.XPATH, cards_xpath)
    print(f"Number of cards found: {len(card_elements)}")  # Debugging

    # Prepare a list to hold the scraped data
    yoga_data = []

    # Iterate through each card and extract the title and description
    for index, card in enumerate(card_elements):
        try:
            # Find the title inside the current card
            title_xpath = './/div[@class="title"]'
            title_element = card.find_element(By.XPATH, title_xpath)
            title_text = title_element.text.strip()  # Extract the text of the title

            # Find the description inside the current card
            description_xpath = './/div[@class="card-content__description"]'  # Adjust this XPath based on structure
            try:
                description_element = card.find_element(By.XPATH, description_xpath)
                description_text = description_element.text.strip()  # Extract the text of the description
            except Exception:
                description_text = "No description available"

            # Append the title and description to the data list
            yoga_data.append({"Title": title_text, "Description": description_text})
            print(f"Card {index + 1}: {title_text} - {description_text}")  # Debugging
        except Exception as e:
            print(f"Error extracting data from card {index + 1}: {e}")

    # Save the data to a CSV file
    df = pd.DataFrame(yoga_data)
    df.to_csv("yoga_poses_with_descriptions.csv", index=False)
    print("Data saved to yoga_poses_with_descriptions.csv")

finally:
    # Close the browser
    driver.quit()
