import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'coursera'
    # allowed_domains = ['coursera.org']
    page_number = 2
    start_urls = ['https://www.coursera.org/search?query=free&index=prod_all_launched_products_term_optimization']

    def parse(self, response):

        baseurl = 'https://www.coursera.org'

        #notworking
        # links = response.css('.in-cell-link').css('::attr(href)')
        # for link in links:
        #     yield response.follow(link, callback=self.parse_catagory)

        # for link in response.css('.captionloaded_h a').css('::attr(href)'):
        #     # landing = baseurl + str()
        #     yield response.follow(link.get(), callback=self.parse_catagory)
        # links = .extract()
        # for link in links:
        #     yield {
        #         'link': baseurl + str(link)
        #     }
        # next_page = 'https://www.coursera.org/search?query=free&page=' + str(CourseraSpider.page_number) + '&index=prod_all_launched_products_term_optimization&allLanguages=English&topic=Computer%20Science&utm_source=linkshare&siteID=vedj0cWlu2Y-ey6KWQ8KbYLpf0U9zvzXuA&ranEAID=vedj0cWlu2Y&utm_content=10&ranMID=40328&ranSiteID=vedj0cWlu2Y-ey6KWQ8KbYLpf0U9zvzXuA&utm_campaign=vedj0cWlu2Y&utm_medium=partners'
        # if CourseraSpider.page_number < 9:
        #     CourseraSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)

        # yield {
        #     'links': baseurl + str(links)
        # }

    def parse_catagory(self, response):

        links = response.css("link").css("::attr(href)").extract()
        for link in links:
            if 'https://www.coursera.org/' in link:
                courselink = link
                break
        name = response.css('.banner-title-without--subtitle').css('::text').get()
        enrolled = response.css('#main #main ._1fpiay2 span').css('::text').get()
        rating = response.css('.rc-ReviewsOverview__totals__rating').css('::text').get()
        ratingNo = response.css('.rc-ReviewsOverview__totals__total-reviews').css('::text').get()
        description = response.css('.description p:nth-child(1)').css('::text').get()
        provider = response.css('.rc-Partner__title').css('::text').get()
        subCatagory = response.css('._1ruggxy~ ._1ruggxy+ ._1ruggxy .font-weight-bold').css('::text').get()
        catagory = response.css('._1ruggxy:nth-child(2) .font-weight-bold').css('::text').get()
        instructor = response.css('.instructor-title , .headline-3-text').css('::text').get()
        reviewer = response.css('.rc-TopReviewsListItem:nth-child(3) .rc-TopReviewsListItem__info span:nth-child(1) , '
                                '.section-title+ .rc-TopReviewsListItem .rc-TopReviewsListItem__info span:nth-child('
                                '1)').css('::text').extract()
        reviews = response.css('.rc-TopReviewsListItem:nth-child(3) .rc-TopReviewsListItem__comment , .section-title+ '
                               '.rc-TopReviewsListItem .rc-TopReviewsListItem__comment').css('::text').extract()

        instructorImage = str(response.css('._1dnm41i img').css('::attr(src)').get()).replace(
            '&blur=200&px=8&w=112&h=112', 'w=112&h=112&q=40&fit=crop')
        time = response.css('.m-b-0.m-t-1s').css('::text').get()
        # time =
        if name is not None:
            yield {'name': name,
                   'course': courselink,
                   'enrolled': enrolled,
                   'instructor': instructor,
                   'instructorImage': instructorImage,
                   'rating': rating,
                   'ratingNo': ratingNo,
                   'reviewer': reviewer,
                   'reviews': reviews,
                   'description': description,
                   'time': time,
                   'provider': provider,
                   'catagory': catagory,
                   'subCatagory': subCatagory
                   }
