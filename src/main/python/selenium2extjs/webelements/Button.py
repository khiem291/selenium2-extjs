'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class Button(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.button_element = "btnEl"
        super(Button, self).__init__(driver, query_type, query, top_element)

    def get_element(self):
        element_id = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.id" % self.button_element
        )
        return self.driver.find_element_by_id(element_id)
