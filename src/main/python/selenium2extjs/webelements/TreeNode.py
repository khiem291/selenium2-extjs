'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class TreeNode(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type, query):
        '''
        Constructor
        '''
        self.function_get_ui = ".getUI()"
        self.node_expression = ""
        self.node_ui_expression = ""
        self.tree_expression = ""

        super(TreeNode, self).__init__(driver, query_type, query)

        self.tree_expression = self.get_expression()

    def get_root_node(self):
        self.node_expression = ".getRootNode()"
        self.exec_script_clean(
            "%s.%s" % (self.tree_expression, self.node_expression)
        )
        return self

    def get_selected_node(self):
        self.node_expression = ".getSelectionModel().getSelectedNode()"
        self.exec_script_clean(self.tree_expression + self.node_expression)
        return self

    def collapse_node(self):
        self.node_expression = ".getSelectionModel().getSelectedNode()"
        self.exec_script_clean("%s.collapse()" % self.node_expression)

    def collapse_root_node(self):
        self.exec_script_clean("%s.collapse()" % self.get_root_node())

    def expand(self):
        self.get_selected_node()
        self.exec_script_clean(
            "%s%s.expand()" % (self.tree_expression, self.node_expression)
        )

    def expand_node(self):
        self.node_expression = ".getSelectionModel().getSelectedNode()"
        self.exec_script_clean("%s.expand()" % self.node_expression)

    def expand_root_node(self):
        self.exec_script_clean("%s.expand()" % self.get_root_node())

    def find_child(self, attribute=None, value=None):
        if attribute:
            self.exec_script_clean(
                "%s.getRootNode().findChild('%s', '%s', true).select()" % (
                    self.tree_expression, attribute, value
                )
            )

        else:
            if not self.node_expression:
                self.get_root_node()

            self.exec_script_on_extjs_cmp(
                "%s.findChild('name' , '%s', true ).select()" % (
                    self.node_expression, value
                )
            )

        return self

    def has_child_nodes(self, params):
        return self.exec_script_on_extjs_cmp_return_bool(
            "%s.hasChildNodes()" % self.node_expression
        )

    def is_checked(self):
        return self.exec_script_on_extjs_cmp_return_bool(
            "%s.isChecked()" % self.tree_expression + self.function_get_ui
        )

    def is_first(self):
        return self.exec_script_on_extjs_cmp_return_bool(
            "%s.isFirst()" % self.node_expression
        )

    def is_leaf(self):
        return self.exec_script_on_extjs_cmp_return_bool(
            "%s.isLeaf()" % self.node_expression
        )

    def is_selected(self):
        return self.exec_script_on_extjs_cmp_return_bool(
            "%s.isSelected()" % self.node_expression
        )

    def select(self, node_id):
        self.exec_script_clean(
            ".getSelectionModel().select('%s'.nodeHash['%s'])" % (
                self.get_expression(), node_id
            )
        )
        return self.get_selected_node()

    def toggle_check(self, check, attribute=None, value=None):
        if attribute and value:
            self.find_child(attribute, value)
            self.get_selected_node()
            self.exec_script_clean(
                "%s%s%s.toggleCheck(%s)" % (
                    self.tree_expression,
                    self.node_expression,
                    self.function_get_ui,
                    check
                )
            )
        else:
            self.exec_script_clean(
                "%s.getSelectionModel().getSelectedNode().getUI().toggleCheck(%s)" % (
                    self.tree_expression, check
                )
            )
