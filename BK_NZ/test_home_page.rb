require 'selenium-webdriver'
require 'test/unit'
#require 'phantomjs'

module Test
  class TestHomePage < Test::Unit::TestCase

    def setup
      @driver = Selenium::WebDriver.for :phantomjs
      @driver.navigate.to('http://www.burgerking.fi/')
      @driver.manage.timeouts.implicit_wait = 20
      @wait = Selenium::WebDriver::Wait.new :timeout => 20
    end

    def teardown
      @driver.quit
    end

    #def test_home_page_title
    #  assert_equal('BURGER KING®', @driver.title)
    #end

    def test_visible_carousel_big_image
      verify_visible_image(:css, '.owl-item:not(.cloned) .big-img')
    end

    def test_visible_carousel_mobile_image
      verify_visible_image(:css, '.owl-item:not(.cloned) .mobile-img')
    end

    def test_all_buttons_have_valid_link
      ary = Array.new
      https = 'https'
      buttonList = @driver.find_elements(:css, 'a.bk-btn')
      buttonList.each do |i|
        #puts i.attribute('href')
        getlink = i.attribute('href')

        begin
          if getlink != nil
            if getlink.include?(https) == false
              #p getlink
              ary.push(getlink)
            end
          end
        rescue NoMethodError
          p "Error #{i}"
          next
        end

      end
      ary.uniq.each do |a|
        #puts a
        res = Net::HTTP.get_response(URI(a))
        assert_not_equal('404', res.code, "This is error #{a}")
      end
    end

    def test_home_take_a_break
      verify_visible_image_in_css(:css, 'section.homeSocial .bg-left')
      verify_visible_image_in_css(:css, 'section.homeSocial .bg-right')
      assert_not_nil(@driver.find_element(:css, 'section.homeSocial .title .top').text)
      assert_not_nil(@driver.find_element(:css, 'section.homeSocial .title .bot').text)
      assert @wait.until {@driver.find_element(:css, 'ul#flick-inflickity-clone').displayed?}
      assert element_present?(:css, 'ul#flick-inflickity-clone') # Check image on Flick
      verify_visible_image_in_css(:css, '#flickWrapper .item:first-child .front')
      verify_visible_image_in_css(:css, '#flickWrapper .item:first-child .bgFlip')
      verify_visible_image_in_css(:css, '#flickWrapper .item:last-child .front')
      verify_visible_image_in_css(:css, '#flickWrapper .item:last-child .bgFlip')
      assert @driver.find_element(:css, 'h4.subtitle').text.include?'swipe it, flip it, share it'
    end

    def test_home_find_restaurant
      verify_visible_image_in_css(:css, 'section.homeMap')
      assert @driver.find_element(:css, 'div.swatch h4.title').text.include?'find a restaurant'
    end

    def test_home_our_story
      verify_visible_image_in_css(:css, 'section.ourStory')
      assert @driver.find_element(:css, 'section.ourStory h3.title').text.include?'SINCE 1954'
      assert_not_nil @driver.find_element(:css, 'section.ourStory h4.subtitle').text
    end

    def test_home_made_to_order
      verify_visible_image_in_css(:css, 'section.madeToOrder')
      assert @driver.find_element(:css, 'section.madeToOrder h3.title').text.include?'MADE TO ORDER'
      assert_not_nil @driver.find_element(:css, 'section.madeToOrder h4.subtitle').text
    end

    def test_home_bk_delivers
      verify_visible_image_in_css(:css, '.bkDelivers')
      assert @driver.find_element(:css, 'section.bkDelivers h3.title').text.include?'delivers'
      assert_not_nil @driver.find_element(:css, 'section.bkDelivers h4.subtitle').text
    end

    def test_home_bk_callouts
      #verify_visible_image_in_css(:css, '.bkCallouts')
      assert_equal(4, how_many_rows(:css, 'section.bkCallouts .row .col-sm-3'))
      @driver.find_elements(:css, 'section.bkCallouts .row .col-sm-3').each do |c|
        assert_not_nil c.text
      end
    end




    def verify_visible_image(how, what)
      imgList = @driver.find_elements(how, what)
      imgList.each do |i|
        #puts i.attribute('src')
        res = Net::HTTP.get_response(URI(i.attribute('src')))
        assert_equal('200', res.code, "This is error #{i.attribute('src')}")
      end
    end

    def verify_visible_image_in_css(how, what)
      imgListCSS = @driver.find_element(how, what)
      #puts imgListCSS.css_value('background-image')
      urlString = imgListCSS.css_value('background-image')
      urlArray = urlString.split('(')
      url = urlArray[1].split(')')
      res = Net::HTTP.get_response(URI(url[0]))
      assert_equal('200', res.code, "This is error #{url[0]}")
    end

    def how_many_rows(how, what)
      rowList = @driver.find_elements(how, what)
      rowList.size()
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


  end
end