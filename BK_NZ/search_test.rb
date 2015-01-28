require 'test/unit'
#require 'rubygems'
require 'selenium-webdriver'

class NzSearchTest < Test::Unit::TestCase

  # Called before every test method runs. Can be used
  # to set up fixture information.
  def setup
    # Do nothing
    client = Selenium::WebDriver::Remote::Http::Default.new
    client.timeout = 400
    @driver = Selenium::WebDriver.for :ff, :http_client => client
    #@driver = Selenium::WebDriver.for :firefox
    @driver.manage.window.maximize
    @driver.manage.timeouts.implicit_wait = 300
    @wait = Selenium::WebDriver::Wait.new(timeout: 20)
    @nz_staging = 'http://ec2-54-85-128-13.compute-1.amazonaws.com'
    @nz_live = 'http://burgerking.co.nz/'
    @driver.get @nz_live
  end

  # Called after every test method runs. Can be used to tear
  # down fixture information.

  def test_sitesearch_found
    @driver.find_element(:css, 'li.hasForm.searchForm span.menuItem-medium').click
    assert @wait.until {@driver.find_element(:css, 'li.hasForm.searchForm form.formArea input.navInput').displayed?}
    @driver.find_element(:css, 'li.hasForm.searchForm form.formArea input.navInput').send_key('Chicken Nuggets')
    @driver.find_element(:css, 'li.hasForm.searchForm form.formArea button.navInputSubmit').click
    p @driver.title
    assert @driver.title.include?('Search')
    p @driver.find_element(:css, 'section.container-fluid.searchItems div.resultsNo').text
    assert_not_nil @driver.find_element(:tag_name, 'img')
    assert_not_nil @driver.find_element(:css, 'div.itemDetails')
  end

  def test_sitesearch_not_found
    @driver.find_element(:css, 'li.hasForm.searchForm span.menuItem-medium').click
    assert @wait.until {@driver.find_element(:css, 'li.hasForm.searchForm form.formArea input.navInput').displayed?}
    @driver.find_element(:css, 'li.hasForm.searchForm form.formArea input.navInput').send_key('Sandwich')
    @driver.find_element(:css, 'li.hasForm.searchForm form.formArea button.navInputSubmit').click
    p @driver.title
    assert @driver.title.include?('Search')
    p @driver.find_element(:css, 'section.container-fluid.searchItems div.resultsNo').text
    assert element_present?(:css, 'h3.sectionTitle')
    assert @driver.find_element(:css, 'div.resultsNo').text.include?'No results found'
  end

  def test_search
    assert @wait.until {@driver.find_element(:css, 'li.hasForm.searchForm span.menuItem-medium i.icon').displayed?}
    @driver.find_element(:css, 'li.hasForm.searchForm span.menuItem-medium i.icon').click
    @driver.find_element(:css, 'li.hasForm.searchForm form.formArea button.navInputSubmit').click
    assert @driver.title.include?'Search'
    assert @driver.find_element(:css, 'div.resultsNo').text.include?'No results found'
    @driver.find_element(:id, 'edit-term').send_key('Cheese')
    @driver.find_element(:css, 'form#views-exposed-form-search-page button.submit').click
    assert @wait.until {@driver.find_element(:css, 'section.container-fluid.searchItems ul.itemsList').displayed?}
    assert @driver.find_element(:css, 'section.container-fluid.searchItems ul.itemsList').text.include?'Cheese'
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