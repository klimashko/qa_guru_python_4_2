from selene.support.shared import browser
from selene import be, have

browser.open('https://www.ecosia.org/')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
browser.element('[data-test-id="web-result-description"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
