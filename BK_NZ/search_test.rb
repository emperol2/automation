require 'test/unit'
require 'rubygems'
require 'selenium-webdriver'

class NzSearchTest < Test::Unit::TestCase

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    # Do nothing
    @driver = Selenium::WebDriver.for :firefox
    @driver.manage.window.maximize
    @wait = Selenium::WebDriver::Wait.new(timeout: '20')
    @nz_url = 'http://burgerking.co.nz/'
    @driver.get(@nz_url)
  end

  # Called after every test method runs. Can be used to tear
  # down fixture information.

  def test_search_found
    p @driver.title
    @driver.find_element(css: 'li.hasForm.searchForm span.menuItem-medium').click
    @driver.find_element(css: 'li.hasForm.searchForm form.formArea input.navInput').send_key('Chicken Nuggets')
    @driver.find_element(css: 'li.hasForm.searchForm form.formArea button.navInputSubmit').click
    assert @driver.title.include?('Search')
    p @driver.find_element(css: 'section.container-fluid.searchItems div.resultsNo').text
    assert_raise do
      @wait.until {@driver.find_element(tag_name: 'img')}
      @wait.until {@driver.find_element(css: 'div.itemDetails')}
    end
  end

  def test_search_not_found
    p @driver.title
    @driver.find_element(css: 'li.hasForm.searchForm span.menuItem-medium').click
    @driver.find_element(css: 'li.hasForm.searchForm form.formArea input.navInput').send_key('Sandwich')
    @driver.find_element(css: 'li.hasForm.searchForm form.formArea button.navInputSubmit').click
    assert @driver.title.include?('Search')
    p @driver.find_element(css: 'section.container-fluid.searchItems div.resultsNo').text
    #assert @driver.element_present?(tag_name: 'img')
    #assert @driver.element_present?(css: 'div.itemDetails')
  end

  def element_present?(how, what)
    found = @driver.find_element(how => what)
    if found
      true # return true if this element is found
    else
      false # return false if this element is not found
    end
  rescue Selenium::WebDriver::Error::NoSuchElementError # catch if NoSuchElementError appears
    false
  end

  def teardown
    # Do nothing
    @driver.quit
  end

  # Fake test
  #def test_fail
  #
  #  # To change this template use File | Settings | File Templates.
  #  fail('Not implemented')
  #end
end