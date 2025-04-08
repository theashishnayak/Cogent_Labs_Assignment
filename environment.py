# environment.py
import logging
import os
from datetime import datetime
from playwright.sync_api import sync_playwright

LOG_DIR = "logs"
SCREENSHOT_DIR = "screenshots"
VIDEO_DIR = "videos"

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)
    return logger

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=1000)
    context.page = context.browser.new_page(record_video_dir=VIDEO_DIR) # Removed record_video_size for now

    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_name = f"{scenario.name.replace(' ', '_')}_{timestamp}.log"
    log_file_path = os.path.join(LOG_DIR, log_file_name)
    context.logger = setup_logger('playwright_automation', log_file_path) # Ensure this line is reached
    context.logger.info(f"Starting scenario: {scenario.name}")
    context.scenario_name_for_logs = scenario.name.replace(' ', '_')

def after_scenario(context, scenario):
    context.logger.info(f"Finished scenario: {scenario.name} - Status: {scenario.status.name.upper()}")
    video_path = context.page.video.path() if context.page and context.page.video else None
    if video_path:
        context.logger.info(f"Video recording saved to: {video_path}")
    context.page.close()
    context.browser.close()
    context.playwright.stop()


def after_step(context, step):
    try:
        if step.status == "failed":
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # Use step.name instead of step.step_id
            screenshot_name = f"{context.scenario_name_for_logs}_step_{step.name.replace(' ', '_')}_{timestamp}.png"
            screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
            context.page.screenshot(path=screenshot_path)
            context.logger.error(f"Step '{step.name}' failed. Screenshot saved to: {screenshot_path}")
    except Exception as e:
        print(f"Error in after_step: {e}")