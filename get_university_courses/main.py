import requests
from bs4 import BeautifulSoup
import urllib.parse


class GetSemester:
    COURSES_URL = 'https://secure2.mnsu.edu/courses/selectform.asp'

    def __init__(self, department):
        self.param_dict_list = []
        self.department = department
        self.user_request_encode = None

        self.course_list = []

        self.request_headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Origin': "https://secure2.mnsu.edu",
            'Referer': "https://secure2.mnsu.edu/courses/Default.asp",
            'cache-control': "no-cache",
            'Postman-Token': "6f1fa71c-c6fa-4fc4-b7df-e3cefe723179"
        }

        self.web_scrap_param()

    def web_scrap_param(self):
        page_response = requests.get(self.COURSES_URL, verify=False)
        web_courses_parser = BeautifulSoup(page_response.content, "html.parser")

        scraping_param_dict = dict()
        for option in web_courses_parser.find_all('option'):
            search_option = (option.text.replace(" ", "")).upper()
            if search_option[0:4] == "FALL":
                scraping_param_dict[search_option] = option['value']
            if search_option[0:4] == "SPRI":
                scraping_param_dict[search_option] = option['value']
            for department in self.department:
                if department == search_option:
                    scraping_param_dict[search_option] = option['value']
        self.param_dict_list.append(scraping_param_dict)
        for dictionary in self.param_dict_list:
            for key in dictionary:
                print(" ")
                print("Getting data for " + key + "...")
                self.get_university_courses(self.COURSES_URL, dictionary.get(key))

    def get_university_courses(self, course_url, key):
        params = {
            'semester': key,
            'campus': '1,2,3,4,5,6,7,9,A,B,C,I,L,M,N,P,Q,R,S,T,W,U,V,X,Y,Z',
            'startTime': '0600',
            'endTime': '2359',
            'days': 'ALL',
            'All': 'All Sections',
            'undefined': ''
        }

        def transfer_params(parse_params):
            """Urlparse"""
            parse_params = urllib.parse.urlencode(parse_params)
            params_list = [parse_params]
            return params_list

        self.user_request_encode = transfer_params(params)

        response = requests.request("POST", course_url, data=self.user_request_encode[0],
                                    headers=self.request_headers)

        self.get_data(response)

    def get_data(self, web_response):
        data_html_parser = BeautifulSoup(web_response.text, 'html.parser')

        for table_data in data_html_parser.find_all("tr"):
            course_titles_list = []
            course_data_list = []

            course_title_raw = table_data.find(color="#ffffff")
            if course_title_raw is not None:
                for course_title in course_title_raw("b"):
                    title_text = course_title.get_text()
                    course_titles_list.append(title_text)
            if (table_data["bgcolor"] == "#E1E1CC") or (table_data["bgcolor"] == "#FFFFFF"):
                for course_data in table_data("td"):
                    course_data_text = course_data.get_text()
                    course_data_list.append(course_data_text)

            if course_titles_list:
                self.course_list.append(course_titles_list)
            if course_data_list:
                if len(course_data_list[0]) == 6:
                    self.course_list.append(course_data_list)
        self.return_data()

    def return_data(self):
        for i in range(len(self.course_list)):
            print(self.course_list[i])


print("Please wait, the process might take several minututes.")

GetSemester("Business")
