'''
Created on Jun 10, 2015
'''
from selenium2extjs.webelements.Field import Field


class FileField(Field):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.input_element = "fileInputEl"
        super(Field, self).__init__(driver, query_type, query, top_element)

    def get_element(self):
        element_id = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.id" % self.input_element
        )
        return self.driver.find_element_by_id(element_id)

    def get_input_el(self):
        element_id = self.exec_script_on_extjs_cmp(
            "return extCmp.id"
        )
        return self.driver.find_element_by_id(element_id)
