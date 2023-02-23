from selene.support.shared import browser
from selene import be, have


def test_search_text(set_size_browser_window):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[class="serp__results js-serp-results"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_another_text_search(set_size_browser_window):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('oifviwurh834764786odkjfbwhi').press_enter()
    browser.element('[class="serp__results js-serp-results"]').should(have.text('oifviwurh834764786odkjfbwhi'))


def test_text_random_search(set_size_browser_window):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('щавомрывшщармшг834678347ваомиодрм').press_enter()
    browser.element('[class="no-results__title"]').should(have.text('По запросу щавомрывшщармшг834678347ваомиодрм результаты не найдены.'))
