'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class Field(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        super(Field, self).__init__(driver, query_type, query, top_element)

    def get_raw_value(self):
        return self.exec_script_on_extjs_cmp("return extCmp.getRawValue()")

    def get_value(self):
        return self.exec_script_on_extjs_cmp("return extCmp.getValue()")

    def reset(self):
        self.exec_script_on_extjs_cmp("extCmp.reset()")

    def reset_value(self):
        self.exec_script_on_extjs_cmp("extCmp.setValue( '' )")

    def send_keys(self, value):
        self.top_element.send_keys(value)

    def set_value(self, value):
        return self.exec_script_on_extjs_cmp(
            "extCmp.setValue('%s')" % value
        )
