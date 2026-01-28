import allure
from allure_commons.types import AttachmentType


def add_screenshot(driver):
    png = driver.get_screenshot_as_png()
    allure.attach(
        png,
        name="Screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png"
    )


def add_logs(driver):
    try:
        log_text = "".join(f'{text}\n' for text in driver.execute("getLog", {'type': 'browser'})['value'])
        allure.attach(
            log_text,
            name="Browser logs",
            attachment_type=AttachmentType.TEXT,
            extension=".log"
        )
    except Exception:
        allure.attach(
            "Browser logs are not available for this driver.",
            name="Browser logs",
            attachment_type=AttachmentType.TEXT
        )


def add_html(driver):
    html = driver.page_source
    allure.attach(
        html,
        name="Page source",
        attachment_type=AttachmentType.HTML,
        extension=".html"
    )


def add_video(driver):
    video_url = (
        f"https://selenoid.autotests.cloud/video/{driver.session_id}.mp4"
    )
    html = (
        "<html><body>"
        f"<video width='100%' height='100%' controls>"
        f"<source src='{video_url}' type='video/mp4'>"
        "</video>"
        "</body></html>"
    )
    allure.attach(
        html,
        name="Video",
        attachment_type=AttachmentType.HTML,
        extension='.html'
    )
