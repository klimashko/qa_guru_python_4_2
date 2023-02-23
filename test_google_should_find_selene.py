from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def set_size_browser_window():
    browser.config.window_width = 500
    browser.config.window_height = 626


def test_search_text(set_size_browser_window):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[class="serp__results js-serp-results"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_another_text_search(set_size_browser_window):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('oifviwurh834764786odkjfbwhi').press_enter()
    browser.element('[data-test-id="web-result-description"]').should(have.text('oifviwurh834764786odkjfbwhi'))


def test_text_random_search(set_size_browser_window):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('щавомрывшщармшг834678347ваомиодрм').press_enter()
    browser.element('[class="no-results__title"]').should(have.text('По запросу щавомрывшщармшг834678347ваомиодрм результаты не найдены.'))
