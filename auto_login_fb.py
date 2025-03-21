from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


def login_facebook(driver, email, password):
    """Logs into Facebook and posts a status update."""
    try:
        driver.get("https://www.facebook.com/")
        time.sleep(3)

        # Enter email and password
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.NAME, "login").click()
        time.sleep(5)

        # Post a status update
        status = "Hello, this is an automated post from Selenium!"
        driver.find_element(By.XPATH, "//textarea[contains(@aria-label, 'on your mind')]").click()
        time.sleep(2)
        driver.switch_to.active_element.send_keys(status)
        time.sleep(1)
        driver.switch_to.active_element.send_keys(Keys.RETURN)

        print("✅ Facebook post successful!")
    except Exception as e:
        print(f"❌ Facebook Error: {e}")


def login_instagram(driver, username, password, image_path, caption):
    """Logs into Instagram and uploads a photo with a caption."""
    try:
        # Open new tab for Instagram
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(20)

        # Enter username and password
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(20)

        # Click the "+" button to create a new post
        driver.get("https://www.instagram.com/")
        time.sleep(20)
        driver.find_element(By.XPATH, "//div[@aria-label='New post']").click()
        time.sleep(20)

        # Upload image
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(image_path)
        time.sleep(20)

        # Click "Next"
        driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
        time.sleep(20)

        # Enter caption
        caption_field = driver.find_element(By.XPATH, "//textarea[contains(@aria-label, 'Write a caption')]")
        caption_field.send_keys(caption)
        time.sleep(20)

        # Click "Share"
        driver.find_element(By.XPATH, "//button[contains(text(),'Share')]").click()
        time.sleep(20)

        print("✅ Instagram post successful!")
    except Exception as e:
        print(f"❌ Instagram Error: {e}")


if __name__ == "__main__":
    # Set your login credentials
    fb_email = "chandu.chilukamary@gmail.com"
    fb_password = "*38anDU#"

    ig_username = "chandu.chilukamary@gmail.com"
    ig_password = "*38anDU#"

    # Set Instagram image path & caption
    image_path = os.path.abspath(r"G:\python001.jpg")  # Replace with an actual image path
    caption = "This is an automated Instagram post! 📸"

    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Log in and post on Facebook & Instagram
    login_facebook(driver, fb_email, fb_password)
    time.sleep(20)  # Wait before opening the next tab
    login_instagram(driver, ig_username, ig_password, image_path, caption)

    # Keep the browser open
    input("Press ENTER to close browser...")
    driver.quit()
