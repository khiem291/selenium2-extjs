'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent
from selenium2extjs.webelements.TreeNode import TreeNode
from selenium2extjs.webelements import ExtJSQueryType


class Tree(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        super(Tree, self).__init__(driver, query_type, query, top_element)

    def contains(self, node_id):
        return self.exec_script_clean_return_bool(
            "return extCmp.nodeHash['%s'] != null" % node_id
        )

    def get_root_node(self):
        tree_node = TreeNode(
            self.driver, ExtJSQueryType.GetCmp, self.get_component_id()
        )
        return tree_node.get_root_node()

    def select(self, node_id):
        self.exec_script_clean(
            ".getSelectionModel().select('%s'.nodeHash['%s'])" % (
                self.get_expression(), node_id
            )
        )
        tree_node = TreeNode(
            self.driver, ExtJSQueryType.GetCmp, self.get_component_id()
        )

        return tree_node.get_selected_node()
